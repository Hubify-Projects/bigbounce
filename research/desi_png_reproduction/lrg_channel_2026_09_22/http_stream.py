"""Ledger row 4 LRG channel: HTTP range-read streaming I/O.

Pattern reused from pipelines/p4prime_chirality_test/row16_indomain_d180_2026_09_22/
run_indomain_rotations.py (lane bb-LS10): pull only the bytes needed, decode in
memory, drop them -- so no bulk catalogue is ever written to disk.

Two surfaces:
  RangeFile  -- a seekable read-only file-like object over an HTTPS URL, used to
                open remote HDF5 (official DESI window/spectrum/covariance
                products) with h5py's fileobj driver: zero bytes on disk.
  stream_fits_bintable -- sequential chunked reader for a FITS binary table that
                yields only the requested columns, never materialising the file.

Every byte fetched is counted in BYTES_STREAMED so the Q2 manifest can report
the real network volume.
"""
import io
import os
import struct
import urllib.request

import numpy as np

BYTES_STREAMED = {"n": 0}


def _get(url, start=None, end=None, retries=4):
    req = urllib.request.Request(url)
    if start is not None:
        req.add_header("Range", f"bytes={start}-{'' if end is None else end}")
    last = None
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(req, timeout=300) as r:
                b = r.read()
            BYTES_STREAMED["n"] += len(b)
            return b
        except Exception as e:  # transient network -- retry, never fabricate
            last = e
    raise RuntimeError(f"range fetch failed after {retries}: {url} [{start}:{end}] {last}")


def content_length(url):
    req = urllib.request.Request(url, method="HEAD")
    with urllib.request.urlopen(req, timeout=120) as r:
        return int(r.headers["Content-Length"])


class RangeFile(io.RawIOBase):
    """Minimal seekable file-like object backed by HTTP range requests, with a
    simple block cache so h5py's many small reads do not become many round
    trips."""

    def __init__(self, url, block=4 << 20, max_blocks=96):
        self.url = url
        self.size = content_length(url)
        self.block = block
        self.max_blocks = max_blocks
        self._cache = {}
        self._order = []
        self._pos = 0

    def readable(self):
        return True

    def seekable(self):
        return True

    def _block(self, i):
        if i in self._cache:
            return self._cache[i]
        start = i * self.block
        end = min(start + self.block, self.size) - 1
        b = _get(self.url, start, end)
        self._cache[i] = b
        self._order.append(i)
        if len(self._order) > self.max_blocks:
            self._cache.pop(self._order.pop(0), None)
        return b

    def seek(self, off, whence=0):
        if whence == 0:
            self._pos = off
        elif whence == 1:
            self._pos += off
        else:
            self._pos = self.size + off
        return self._pos

    def tell(self):
        return self._pos

    def read(self, n=-1):
        if n is None or n < 0:
            n = self.size - self._pos
        n = min(n, self.size - self._pos)
        out = bytearray()
        while n > 0:
            i = self._pos // self.block
            off = self._pos - i * self.block
            b = self._block(i)
            take = min(n, len(b) - off)
            out += b[off:off + take]
            self._pos += take
            n -= take
            if take == 0:
                break
        return bytes(out)

    def readinto(self, buf):
        data = self.read(len(buf))
        buf[:len(data)] = data
        return len(data)


def h5_remote(url):
    """Open a remote HDF5 file with h5py, streaming, nothing on disk."""
    import h5py
    return h5py.File(RangeFile(url), "r")


# ---------------------------------------------------------------- FITS reader

_FITS_TYPES = {
    "D": ("f8", 8), "E": ("f4", 4), "J": ("i4", 4), "K": ("i8", 8),
    "I": ("i2", 2), "B": ("u1", 1), "L": ("u1", 1), "A": ("S1", 1),
}


def _parse_header(block):
    """Parse 80-char FITS cards out of a header block; returns dict."""
    hdr = {}
    for i in range(0, len(block), 80):
        card = block[i:i + 80].decode("ascii", "replace")
        key = card[:8].strip()
        if key == "END":
            hdr["__END__"] = True
            break
        if "=" in card[8:10]:
            val = card[10:].split("/")[0].strip().strip("'").strip()
            hdr[key] = val
    return hdr


def fits_bintable_header(url, maxprobe=64):
    """Read the primary + first-extension headers of a remote FITS file.
    Returns (data_start_byte, nrows, rowbytes, columns) where columns maps
    NAME -> (byte_offset_in_row, numpy_dtype, itemsize, repeat)."""
    pos = 0
    hdr = {}
    # primary HDU
    for _ in range(maxprobe):
        blk = _get(url, pos, pos + 2879)
        h = _parse_header(blk)
        hdr.update(h)
        pos += 2880
        if h.get("__END__"):
            break
    # primary data size (usually 0 for these tables)
    naxis = int(hdr.get("NAXIS", "0"))
    npix = 1
    for a in range(1, naxis + 1):
        npix *= int(hdr.get(f"NAXIS{a}", "1"))
    if naxis == 0:
        npix = 0
    bitpix = abs(int(hdr.get("BITPIX", "8")))
    dsize = npix * bitpix // 8
    pos += ((dsize + 2879) // 2880) * 2880
    # extension header
    ehdr = {}
    for _ in range(maxprobe):
        blk = _get(url, pos, pos + 2879)
        h = _parse_header(blk)
        ehdr.update(h)
        pos += 2880
        if h.get("__END__"):
            break
    assert ehdr.get("XTENSION", "").upper().startswith("BINTABLE"), ehdr.get("XTENSION")
    rowbytes = int(ehdr["NAXIS1"])
    nrows = int(ehdr["NAXIS2"])
    tfields = int(ehdr["TFIELDS"])
    cols, off = {}, 0
    for j in range(1, tfields + 1):
        name = ehdr[f"TTYPE{j}"].strip()
        tform = ehdr[f"TFORM{j}"].strip()
        rep = ""
        k = 0
        while k < len(tform) and tform[k].isdigit():
            rep += tform[k]
            k += 1
        rep = int(rep) if rep else 1
        code = tform[k]
        if code not in _FITS_TYPES:
            raise ValueError(f"unsupported TFORM {tform} for {name}")
        dt, isz = _FITS_TYPES[code]
        if code == "A":  # character string column: one item of `rep` bytes
            cols[name] = (off, f"S{rep}", rep, 1)
            off += rep
        else:
            cols[name] = (off, dt, isz, rep)
            off += isz * rep
    assert off == rowbytes, (off, rowbytes)
    return pos, nrows, rowbytes, cols


def stream_fits_bintable(url, columns, chunk_rows=200000, row_filter=None,
                          progress=None):
    """Stream a remote FITS binary table sequentially and return a dict of
    numpy arrays holding ONLY `columns` (optionally filtered per chunk by
    `row_filter(chunkdict) -> bool mask`). Nothing is written to disk."""
    data_start, nrows, rowbytes, cols = fits_bintable_header(url)
    for c in columns:
        if c not in cols:
            raise KeyError(f"{c} not in {sorted(cols)}")
    acc = {c: [] for c in columns}
    done = 0
    while done < nrows:
        n = min(chunk_rows, nrows - done)
        start = data_start + done * rowbytes
        raw = _get(url, start, start + n * rowbytes - 1)
        arr = np.frombuffer(raw, dtype=np.uint8).reshape(n, rowbytes)
        chunk = {}
        for c in columns:
            off, dt, isz, rep = cols[c]
            sub = arr[:, off:off + isz * rep]
            v = sub.copy().view(dt if dt.startswith("S") else f">{dt}")
            chunk[c] = v[:, 0] if rep == 1 else v
        if row_filter is not None:
            m = row_filter(chunk)
            for c in columns:
                chunk[c] = chunk[c][m]
        for c in columns:
            acc[c].append(np.ascontiguousarray(chunk[c].astype(chunk[c].dtype.newbyteorder("="))))
        done += n
        del raw, arr, chunk
        if progress:
            progress(done, nrows)
    return {c: np.concatenate(acc[c]) if acc[c] else np.array([]) for c in columns}, nrows


def stream_fits_sequential(url, columns, row_filter=None, chunk=32 << 20,
                            progress=None):
    """Single strictly-sequential pass over a remote FITS binary table.

    Reads byte 0 -> EOF exactly once, so the returned sha256 is the sha256 of
    the WHOLE file at no extra network cost, while only `columns` are kept in
    memory (optionally filtered per chunk). Nothing is written to disk.
    """
    import hashlib

    size = content_length(url)
    h = hashlib.sha256()
    pos = 0
    hdr_buf = bytearray()
    data_start = nrows = rowbytes = None
    cols = None
    acc = {c: [] for c in columns}
    rem = b""
    rows_done = 0
    while pos < size:
        end = min(pos + chunk, size) - 1
        blk = _get(url, pos, end)
        h.update(blk)
        if data_start is None:
            hdr_buf += blk
            try:
                data_start, nrows, rowbytes, cols = fits_bintable_header_from_bytes(bytes(hdr_buf))
            except _NeedMore:
                pos = end + 1
                continue
            for c in columns:
                if c not in cols:
                    raise KeyError(f"{c} not in {sorted(cols)}")
            blk = bytes(hdr_buf)[data_start:]
        body = rem + blk
        nfull = min(len(body) // rowbytes, nrows - rows_done)
        if nfull > 0:
            arr = np.frombuffer(body[:nfull * rowbytes], dtype=np.uint8).reshape(nfull, rowbytes)
            chunkd = {}
            for c in columns:
                off, dt, isz, rep = cols[c]
                sub = arr[:, off:off + isz * rep].copy()
                v = sub.view(dt if dt.startswith("S") else f">{dt}")
                chunkd[c] = v[:, 0] if rep == 1 else v
            if row_filter is not None:
                m = row_filter(chunkd)
                for c in columns:
                    chunkd[c] = chunkd[c][m]
            for c in columns:
                acc[c].append(np.ascontiguousarray(
                    chunkd[c].astype(chunkd[c].dtype.newbyteorder("="))))
            rows_done += nfull
            del arr, chunkd
        rem = body[nfull * rowbytes:]
        del body
        pos = end + 1
        if progress:
            progress(rows_done, nrows, pos, size)
    assert rows_done == nrows, (rows_done, nrows)
    out = {c: (np.concatenate(acc[c]) if acc[c] else np.array([])) for c in columns}
    return out, dict(nrows=nrows, rowbytes=rowbytes, bytes=size,
                     sha256=h.hexdigest())


class _NeedMore(Exception):
    pass


def fits_bintable_header_from_bytes(buf):
    """Same parse as fits_bintable_header but over an in-memory prefix."""
    pos = 0
    hdr = {}
    while True:
        if pos + 2880 > len(buf):
            raise _NeedMore()
        h = _parse_header(buf[pos:pos + 2880])
        hdr.update(h)
        pos += 2880
        if h.get("__END__"):
            break
    naxis = int(hdr.get("NAXIS", "0"))
    npix = 1
    for a in range(1, naxis + 1):
        npix *= int(hdr.get(f"NAXIS{a}", "1"))
    if naxis == 0:
        npix = 0
    bitpix = abs(int(hdr.get("BITPIX", "8")))
    pos += ((npix * bitpix // 8 + 2879) // 2880) * 2880
    ehdr = {}
    while True:
        if pos + 2880 > len(buf):
            raise _NeedMore()
        h = _parse_header(buf[pos:pos + 2880])
        ehdr.update(h)
        pos += 2880
        if h.get("__END__"):
            break
    assert ehdr.get("XTENSION", "").upper().startswith("BINTABLE")
    rowbytes = int(ehdr["NAXIS1"])
    nrows = int(ehdr["NAXIS2"])
    cols, off = {}, 0
    for j in range(1, int(ehdr["TFIELDS"]) + 1):
        name = ehdr[f"TTYPE{j}"].strip()
        tform = ehdr[f"TFORM{j}"].strip()
        rep, k = "", 0
        while k < len(tform) and tform[k].isdigit():
            rep += tform[k]
            k += 1
        rep = int(rep) if rep else 1
        code = tform[k]
        dt, isz = _FITS_TYPES[code]
        if code == "A":
            cols[name] = (off, f"S{rep}", rep, 1)
            off += rep
        else:
            cols[name] = (off, dt, isz, rep)
            off += isz * rep
    assert off == rowbytes, (off, rowbytes)
    return pos, nrows, rowbytes, cols
