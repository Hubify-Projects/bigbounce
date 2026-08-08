#!/usr/bin/env python3
"""
Pull DR8 per-galaxy morphology for the 3.2M P4 spirals via the NOIRLab
Astro Data Lab TAP service (ls_dr8.tractor) -- NO 780GB sweep download.

The tractor table IS the source catalog the sweeps are built from; it carries
the identical morphology columns keyed by (brickid, objid) == dr8_id. We batch
by brickid (the table is brickid-indexed), fetch morphology columns, and keep
only rows whose (brickid,objid) is in our spiral set.

Output: /workspace/dr8morph/out/spiral_morphology.parquet
  BRICKID, OBJID, TYPE, FRACDEV, SHAPEDEV_R/E1/E2, SHAPEEXP_R/E1/E2
NEVER fabricate. Real DL query results only.
"""
import os, time, io, sys, urllib.request, urllib.parse
import numpy as np, pandas as pd

t0=time.time()
def log(m): print(f"[{time.time()-t0:7.1f}s] {m}",flush=True)

WORK="/workspace/dr8morph"; os.makedirs(f"{WORK}/out",exist_ok=True)
OUT=f"{WORK}/out/spiral_morphology.parquet"
PART=f"{WORK}/out/_dl_partial.parquet"
DONE=f"{WORK}/out/_dl_done_batches.txt"
TAP="https://datalab.noirlab.edu/tap/sync"
COLS="brickid,objid,type,fracdev,shapedev_r,shapedev_e1,shapedev_e2,shapeexp_r,shapeexp_e1,shapeexp_e2"

# --- spiral keys (regenerate from HF if missing/partial) ---
keys_path=f"{WORK}/spiral_keys.parquet"
if not (os.path.exists(keys_path) and os.path.getsize(keys_path)>100_000_000):
    log("regenerating spiral keys from HF")
    from huggingface_hub import hf_hub_download
    cat=hf_hub_download("bamfai/galaxy-chirality-catalog","catalog_production.parquet",
                        repo_type="dataset",token=os.environ.get("HF_TOKEN"))
    df=pd.read_parquet(cat,columns=["dr8_id","ra","dec","class_eq"])
    df=df[df["class_eq"].isin(["CW","CCW"])].reset_index(drop=True)
    bo=df["dr8_id"].str.split("_",expand=True)
    df["BRICKID"]=bo[0].astype("int64"); df["OBJID"]=bo[1].astype("int64")
    df.rename(columns={"ra":"cat_ra","dec":"cat_dec"})[["BRICKID","OBJID","cat_ra","cat_dec","class_eq"]].to_parquet(keys_path,index=False)
keys=pd.read_parquet(keys_path)
log(f"spiral keys {len(keys):,}")
want_key=np.unique((keys.BRICKID.values.astype(np.int64)<<24) | (keys.OBJID.values.astype(np.int64)&0xFFFFFF))
assert keys.OBJID.max()<(1<<24)
bricks=sorted(keys.BRICKID.unique().tolist())
log(f"unique bricks {len(bricks):,}")

BATCH=int(os.environ.get("BRICK_BATCH","1500"))
batches=[bricks[i:i+BATCH] for i in range(0,len(bricks),BATCH)]
log(f"{len(batches)} brick-batches of up to {BATCH}")

done=set()
if os.path.exists(DONE): done=set(int(x) for x in open(DONE).read().split())

def query_batch(bi, blist, retries=4):
    inlist=",".join(str(b) for b in blist)
    q=f"SELECT {COLS} FROM ls_dr8.tractor WHERE brickid IN ({inlist})"
    data=urllib.parse.urlencode({"REQUEST":"doQuery","LANG":"ADQL","FORMAT":"csv","QUERY":q}).encode()
    for a in range(retries):
        try:
            raw=urllib.request.urlopen(TAP,data=data,timeout=400).read()
            if raw[:20].lstrip().startswith(b"<?xml") or b"QUERY_STATUS" in raw[:400]:
                raise RuntimeError("TAP error: "+raw[:200].decode('latin1',"ignore"))
            df=pd.read_csv(io.BytesIO(raw))
            df.columns=[c.upper() for c in df.columns]
            pk=(df.BRICKID.values.astype(np.int64)<<24)|(df.OBJID.values.astype(np.int64)&0xFFFFFF)
            idx=np.clip(np.searchsorted(want_key,pk),0,len(want_key)-1)
            return df[want_key[idx]==pk].reset_index(drop=True), len(df)
        except Exception as e:
            log(f"  batch {bi} retry {a+1}: {e}")
            time.sleep(4*(a+1))
    return None, 0

import threading
from concurrent.futures import ThreadPoolExecutor
NWORK=int(os.environ.get("NWORK","10"))
lock=threading.Lock()
parts=[]
if os.path.exists(PART):
    parts=[pd.read_parquet(PART)]; log(f"resume: partial {len(parts[0]):,} rows")
state={"kept":sum(len(p) for p in parts),"n":len(done)}
todo=[(bi,bl) for bi,bl in enumerate(batches) if bi not in done]
log(f"processing {len(todo)} batches x {NWORK} workers")

def worker(item):
    bi,blist=item
    sub,nfetch=query_batch(bi,blist)
    with lock:
        state["n"]+=1
        if sub is None:
            log(f"  batch {bi} FAILED"); open(DONE,"a").write(f"{bi}\n"); return
        if len(sub): parts.append(sub)
        state["kept"]+=len(sub); open(DONE,"a").write(f"{bi}\n")
        if state["n"]%5==0 or len(sub):
            log(f"[{state['n']}/{len(batches)}] b{bi} fetched={nfetch:,} kept={len(sub):,} cum_kept={state['kept']:,}")
        if state["n"]%20==0 and parts:
            pd.concat(parts,ignore_index=True).drop_duplicates(["BRICKID","OBJID"]).to_parquet(PART,index=False)
            log(f"  checkpoint rows={state['kept']:,}")

with ThreadPoolExecutor(max_workers=NWORK) as ex:
    list(ex.map(worker, todo))

if not parts:
    log("NO MATCHES -- abort"); sys.exit(2)
allm=pd.concat(parts,ignore_index=True).drop_duplicates(["BRICKID","OBJID"]).reset_index(drop=True)
allm.to_parquet(OUT,index=False)
log(f"WROTE {OUT}: {len(allm):,} matched ({100*len(allm)/len(keys):.1f}% of {len(keys):,})")
log("DONE_PULL")
