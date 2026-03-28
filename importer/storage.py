import os
import json

# Disco mounts a volume at /data; CI should set IMPORTER_STATE_FILE to a writable path.
FILENAME = os.environ.get("IMPORTER_STATE_FILE", "/data/db.json")


def _ensure_parent_dir(path: str) -> None:
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)


def load_since() -> str | None:
    if not os.path.isfile(FILENAME):
        return None
    with open(FILENAME, "r", encoding="utf-8") as f:
        db_json = f.read()
    db = json.loads(db_json)
    return db["since"]


def save_since(since: str) -> None:
    _ensure_parent_dir(FILENAME)
    db = {"since": since}
    db_json = json.dumps(db)
    with open(FILENAME, "w", encoding="utf-8") as f:
        f.write(db_json)
