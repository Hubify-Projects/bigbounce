#!/usr/bin/env python3
"""
Pull DR8 per-galaxy morphology for the 3.2M P4 spirals from NOIRLab Astro Data
Lab (ls_dr8.tractor), fetching ONLY our exact spirals per query via the proven
pattern:
    WHERE brickid IN (<small brick set>)
      AND (brickid*30841.0 + objid) IN (<exact float keys>)
This returns exactly our spirals (no whole-brick dump), so each response is tiny.
Small brick batches keep each query under DL's 60s nginx gateway timeout.
Anonymous sync only (async/upload need a DL account we don't have).

Resumable (skips done batches, reloads _partial). Heavy exponential backoff so
it rides out DL 504 overload windows. Self-terminating; writes final parquet
and, if morphology present, auto-runs the extended forward model.

Output: /workspace/dr8morph/out/spiral_morphology.parquet
NEVER fabricate. Real DL results only.
"""
import os, io, sys, time, threading, urllib.request, urllib.parse
import numpy as np, pandas as pd
from concurrent.futures import ThreadPoolExecutor

t0=time.time()
def log(m): print(f"[{time.time()-t0:8.1f}s] {m}",flush=True)

WORK="/workspace/dr8morph"; os.makedirs(f"{WORK}/out",exist_ok=True)
OUT=f"{WORK}/out/spiral_morphology.parquet"
PART=f"{WORK}/out/_dl_partial.parquet"
DONE=f"{WORK}/out/_dl_done_batches.txt"
TAP="https://datalab.noirlab.edu/tap/sync"
COLS="brickid,objid,type,fracdev,shapedev_r,shapedev_e1,shapedev_e2,shapeexp_r,shapeexp_e1,shapeexp_e2"
F=30841  # objid < 30841 for all spirals -> brickid*F+objid is a unique float key

keys=pd.read_parquet(f"{WORK}/spiral_keys.parquet")
assert keys.OBJID.max() < F, keys.OBJID.max()
log(f"spiral keys {len(keys):,}")
want_key=np.unique((keys.BRICKID.values.astype(np.int64)<<24)|(keys.OBJID.values.astype(np.int64)&0xFFFFFF))
bricks=sorted(keys.BRICKID.unique().tolist())
# group keys by brick for fast per-batch key-list assembly
by_brick=keys.groupby("BRICKID")
brick_to_objids={int(b):g.OBJID.values.astype(np.int64) for b,g in by_brick}
log(f"unique bricks {len(bricks):,}")

BATCH=int(os.environ.get("BRICK_BATCH","40"))     # small -> fast query
NWORK=int(os.environ.get("NWORK","3"))            # gentle concurrency
batches=[bricks[i:i+BATCH] for i in range(0,len(bricks),BATCH)]
log(f"{len(batches)} batches of {BATCH} bricks, {NWORK} workers")

done=set()
if os.path.exists(DONE): done=set(int(x) for x in open(DONE).read().split() if x.strip())
lock=threading.Lock()
parts=[]
if os.path.exists(PART):
    try: parts=[pd.read_parquet(PART)]; log(f"resume partial {len(parts[0]):,}")
    except Exception: pass
state={"kept":sum(len(p) for p in parts),"n":len(done),"fail":0}

def run_batch(bi, blist, retries=10):
    brickset=",".join(str(b) for b in blist)
    fkeys=[]
    for b in blist:
        for o in brick_to_objids[int(b)]:
            fkeys.append(f"{int(b)*F+int(o)}.0")
    keyset=",".join(fkeys)
    q=(f"SELECT {COLS} FROM ls_dr8.tractor WHERE brickid IN ({brickset}) "
       f"AND (brickid*{F}.0 + objid) IN ({keyset})")
    data=urllib.parse.urlencode({"REQUEST":"doQuery","LANG":"ADQL","FORMAT":"csv","QUERY":q}).encode()
    for a in range(retries):
        try:
            raw=urllib.request.urlopen(TAP,data=data,timeout=120).read()
            if raw[:20].lstrip().startswith(b"<?xml") or b"QUERY_STATUS" in raw[:400]:
                raise RuntimeError("TAP:"+raw[:120].decode('latin1','ignore'))
            df=pd.read_csv(io.BytesIO(raw)) if raw.strip() else pd.DataFrame()
            if len(df): df.columns=[c.upper() for c in df.columns]
            return df, len(fkeys)
        except Exception as e:
            wait=min(90,4*(2**a))
            if a>=3: log(f"  b{bi} retry {a+1}/{retries} {wait}s: {str(e)[:70]}")
            time.sleep(wait)
    return None, len(fkeys)

def worker(item):
    bi,blist=item
    df,nreq=run_batch(bi,blist)
    with lock:
        state["n"]+=1
        if df is None:
            state["fail"]+=1; log(f"  b{bi} FAILED (total fails {state['fail']})")
            open(DONE,"a").write(f"{bi}\n"); return
        if len(df): parts.append(df)
        state["kept"]+=len(df); open(DONE,"a").write(f"{bi}\n")
        if state["n"]%50==0:
            log(f"[{state['n']}/{len(batches)}] kept_cum={state['kept']:,} fails={state['fail']}")
        if state["n"]%200==0 and parts:
            pd.concat(parts,ignore_index=True).drop_duplicates(["BRICKID","OBJID"]).to_parquet(PART,index=False)
            log(f"  checkpoint rows={state['kept']:,}")

todo=[(bi,bl) for bi,bl in enumerate(batches) if bi not in done]
log(f"processing {len(todo)} remaining batches")
with ThreadPoolExecutor(max_workers=NWORK) as ex:
    list(ex.map(worker, todo))

if not parts:
    log("NO MATCHES -- abort (not writing empty)"); sys.exit(2)
allm=pd.concat(parts,ignore_index=True).drop_duplicates(["BRICKID","OBJID"]).reset_index(drop=True)
allm.to_parquet(OUT,index=False)
log(f"WROTE {OUT}: {len(allm):,} matched ({100*len(allm)/len(keys):.1f}% of {len(keys):,}); fails={state['fail']}")
log("DONE_PULL")

# auto-run forward model if we got a healthy match fraction
if len(allm) >= 0.5*len(keys):
    log("match fraction >=50% -> auto-running extended forward model")
    os.system("cd /workspace/dr8morph && python3 systematic_l1_forward_model_dr8morph.py >> /workspace/dr8morph/fwd.log 2>&1")
    log("forward model done -> see out/systematic_l1_forward_model_dr8morph.json")
