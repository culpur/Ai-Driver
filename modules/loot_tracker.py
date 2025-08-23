# /opt/ai_driver/modules/loot_tracker.py

import json
from pathlib import Path

LOOT_FILE = "loot.json"

def _get_loot_path(target):
    return Path("results") / target / LOOT_FILE

def _load_loot(target):
    path = _get_loot_path(target)
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text())
    except Exception:
        return {}

def _save_loot(target, loot):
    path = _get_loot_path(target)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(loot, indent=2))

def add_loot(target, category, value):
    loot = _load_loot(target)
    if category not in loot:
        loot[category] = []
    if value not in loot[category]:
        loot[category].append(value)
        _save_loot(target, loot)

def get_loot(target, category):
    loot = _load_loot(target)
    return loot.get(category, [])

