#!/usr/bin/env python3
"""
runpod_ctl.py — minimal, reusable RunPod GraphQL control for BigBounce pods.

Auth: RUNPOD_API_KEY from <repo-root>/.env.local, Bearer header (REST GraphQL;
the python "runpod" SDK errors with this key but REST works — see .env.local note).

Commands:
  python3 tools/runpod_ctl.py status               # list all pods + SSH coords
  python3 tools/runpod_ctl.py resume <podId> [gpuCount]
  python3 tools/runpod_ctl.py wait <podId> [timeout_s]   # poll until RUNNING + SSH:22 public
  python3 tools/runpod_ctl.py ssh <podId>          # print ssh command
  python3 tools/runpod_ctl.py stop <podId>         # podStop (only after /backup-3plus)
"""
import json
import os
import sys
import time
import urllib.request

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _api_key():
    env = os.path.join(REPO, '.env.local')
    for line in open(env):
        if line.startswith('RUNPOD_API_KEY='):
            return line.strip().split('=', 1)[1].strip().strip('"').strip("'")
    raise SystemExit("ERROR: RUNPOD_API_KEY not in .env.local")


def graphql(query, key=None):
    key = key or _api_key()
    req = urllib.request.Request(
        'https://api.runpod.io/graphql',
        data=json.dumps({'query': query}).encode(),
        headers={'Content-Type': 'application/json',
                 'Authorization': f'Bearer {key}',
                 # Cloudflare on api.runpod.io blocks the default Python-urllib UA
                 # (intermittent 403); a browser-like UA passes reliably.
                 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
                               'AppleWebKit/537.36 (KHTML, like Gecko) '
                               'Chrome/124.0 Safari/537.36'},
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        out = json.loads(resp.read())
    if out.get('errors'):
        raise RuntimeError(json.dumps(out['errors']))
    return out['data']


def ssh_coords(pod):
    rt = pod.get('runtime')
    if not rt or not rt.get('ports'):
        return None
    for p in rt['ports']:
        if p['privatePort'] == 22 and p.get('isIpPublic'):
            return {'ip': p['ip'], 'port': p['publicPort']}
    return None


def cmd_status(args):
    data = graphql(
        'query{myself{pods{id name desiredStatus machine{gpuDisplayName} '
        'costPerHr runtime{ports{ip isIpPublic publicPort privatePort}}}}}')
    for pod in data['myself']['pods']:
        c = ssh_coords(pod)
        sshtxt = (f"ssh root@{c['ip']} -p {c['port']} -i ~/.ssh/id_ed25519"
                  if c else "(no ssh yet)")
        print(f"{pod['id']}  {pod['name']:<28} {pod['desiredStatus']:<8} "
              f"{pod['machine']['gpuDisplayName']:<12} ${pod['costPerHr']}/h  {sshtxt}")


def cmd_resume(args):
    pod_id = args[0]
    gpu = args[1] if len(args) > 1 else '1'
    data = graphql(f'mutation{{podResume(input:{{podId:"{pod_id}",gpuCount:{gpu}}})'
                   '{id desiredStatus}}')
    print(json.dumps(data['podResume']))


def cmd_stop(args):
    pod_id = args[0]
    data = graphql(f'mutation{{podStop(input:{{podId:"{pod_id}"}}){{id desiredStatus}}}}')
    print(json.dumps(data['podStop']))


def cmd_wait(args):
    pod_id = args[0]
    timeout = int(args[1]) if len(args) > 1 else 420
    t0 = time.time()
    while time.time() - t0 < timeout:
        data = graphql('query{myself{pods{id desiredStatus '
                       'runtime{ports{ip isIpPublic publicPort privatePort}}}}}')
        for pod in data['myself']['pods']:
            if pod['id'] == pod_id:
                c = ssh_coords(pod)
                if pod['desiredStatus'] == 'RUNNING' and c:
                    print(f"READY ssh root@{c['ip']} -p {c['port']} -i ~/.ssh/id_ed25519")
                    print(json.dumps(c))
                    return
                print(f"  {int(time.time()-t0)}s: status={pod['desiredStatus']} "
                      f"ssh={'yes' if c else 'no'}")
        time.sleep(15)
    raise SystemExit(f"TIMEOUT after {timeout}s — pod {pod_id} not SSH-ready")


def cmd_ssh(args):
    pod_id = args[0]
    data = graphql('query{myself{pods{id runtime{ports{ip isIpPublic '
                   'publicPort privatePort}}}}}')
    for pod in data['myself']['pods']:
        if pod['id'] == pod_id:
            c = ssh_coords(pod)
            if c:
                print(f"ssh root@{c['ip']} -p {c['port']} -i ~/.ssh/id_ed25519")
                return
    raise SystemExit("no ssh coords")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    {'status': cmd_status, 'resume': cmd_resume, 'wait': cmd_wait,
     'ssh': cmd_ssh, 'stop': cmd_stop}[sys.argv[1]](sys.argv[2:])
