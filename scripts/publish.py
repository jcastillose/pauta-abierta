#!/usr/bin/env python3
"""Publica archivos del tablero en GitHub con la API de contenidos.

Uso: python3 publish.py <ruta-token> <carpeta-local-del-repo> [archivo ...]
Por defecto publica data.json y runs.json. Nunca imprime el token.
"""
import base64, json, sys, urllib.error, urllib.request
from datetime import date

OWNER, REPO, BRANCH = "jcastillose", "pauta-abierta", "main"
token = open(sys.argv[1]).read().strip()
folder = sys.argv[2].rstrip("/")
files = sys.argv[3:] or ["data.json", "runs.json"]


def api(path, method="GET", data=None):
    req = urllib.request.Request(
        f"https://api.github.com{path}",
        data=json.dumps(data).encode() if data is not None else None,
        headers={"Authorization": f"Bearer {token}", "Accept": "application/vnd.github+json",
                 "User-Agent": "pauta-abierta-publisher"}, method=method)
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read().decode())


ok = True
for name in files:
    raw = open(f"{folder}/{name}", "rb").read()
    if name.endswith(".json"):
        json.loads(raw)
    body = {"message": f"Actualiza {name} - {date.today().isoformat()}",
            "content": base64.b64encode(raw).decode(), "branch": BRANCH}
    try:
        body["sha"] = api(f"/repos/{OWNER}/{REPO}/contents/{name}?ref={BRANCH}")["sha"]
    except urllib.error.HTTPError as e:
        if e.code != 404:
            print(name, "FALLO al leer sha:", e.code); ok = False; continue
    try:
        res = api(f"/repos/{OWNER}/{REPO}/contents/{name}", "PUT", body)
        print(name, "-> commit", res["commit"]["sha"][:12])
    except urllib.error.HTTPError as e:
        print(name, "FALLO:", e.code, e.read().decode()[:200]); ok = False
print("ALL_OK" if ok else "SOME_FAILED")
sys.exit(0 if ok else 1)
