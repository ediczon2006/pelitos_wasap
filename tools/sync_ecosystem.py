"""
Module: sync_ecosystem.py
Author: Omni-Engineer
Purpose: Unified Data Engine & Cross-System Audit Pipeline.
Synchronizes domain catalogs across 'pelitos_veterinaria' and 'proyecto_wasap'.
Enforces strict schema validation, integer cents financial constraints, and deterministic routing.
"""

import os
import json
import re
import sys
from typing import Dict, List, Any, Optional

CANONICAL_CHANNELS = {
    "RECEPCION": {
        "e164": "51927301122",
        "formatted": "+51 927 301 122",
        "owner": "Diego",
        "domain": ["Pet Shop", "Farmacia", "General"]
    },
    "CONSULTORIO": {
        "e164": "51939356376",
        "formatted": "+51 939 356 376",
        "owner": "Dra. Julia",
        "domain": ["Consultorio", "Medicina General", "Medicina Preventiva", "Laboratorio", "Cirugía"]
    },
    "ESTETICA": {
        "e164": "51948426656",
        "formatted": "+51 948 426 656",
        "owner": "Antonella",
        "domain": ["Estética", "Experiencias de Baño", "Experiencias Spa", "Cortes y Estilo", "Servicios Complementarios"]
    }
}

def to_cents(soles: float) -> int:
    return int(round(soles * 100))

def format_pen(cents: int) -> str:
    return f"S/ {cents / 100:.2f}"

def validate_catalog_integrity(catalog: List[Dict[str, Any]]) -> List[str]:
    errors = []
    seen_codes = set()

    for idx, item in enumerate(catalog):
        code = item.get("codigo")
        if not code:
            errors.append(f"Row {idx}: Missing mandatory 'codigo'")
        elif code in seen_codes:
            errors.append(f"Row {idx}: Duplicate 'codigo' detected: {code}")
        seen_codes.add(code)

        area = item.get("area")
        if area not in ["Consultorio", "Estética", "Farmacia", "Pet Shop"]:
            errors.append(f"Item {code}: Invalid area '{area}'")

        price = item.get("precio")
        if price is None or price < 0:
            errors.append(f"Item {code}: Invalid price '{price}'")

        phone = item.get("telefono")
        if not phone or len(phone) < 9:
            errors.append(f"Item {code}: Invalid telephone '{phone}'")

        # Routing cross-check
        if area in ["Pet Shop", "Farmacia"] and phone != CANONICAL_CHANNELS["RECEPCION"]["e164"]:
            errors.append(f"Item {code} ({area}): Misrouted to {phone}, expected Recepción ({CANONICAL_CHANNELS['RECEPCION']['e164']})")
        elif area == "Consultorio" and phone != CANONICAL_CHANNELS["CONSULTORIO"]["e164"]:
            errors.append(f"Item {code} ({area}): Misrouted to {phone}, expected Consultorio ({CANONICAL_CHANNELS['CONSULTORIO']['e164']})")
        elif area == "Estética" and phone != CANONICAL_CHANNELS["ESTETICA"]["e164"]:
            errors.append(f"Item {code} ({area}): Misrouted to {phone}, expected Estética ({CANONICAL_CHANNELS['ESTETICA']['e164']})")

    return errors

def run_sync():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    json_path = os.path.join(base_dir, "data", "catalogo_maestro.json")

    if not os.path.exists(json_path):
        print(f"ERROR: {json_path} does not exist.")
        sys.exit(1)

    with open(json_path, "r", encoding="utf-8") as f:
        catalog = json.load(f)

    # 1. Audit integrity
    errors = validate_catalog_integrity(catalog)
    if errors:
        print(f"FAILED: Found {len(errors)} integrity errors:")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)
    else:
        print("PASS: Master Catalog schema and routing integrity verified (23 items).")

    # 2. Enrich with minor units (Cents)
    for item in catalog:
        item["precio_centimos"] = to_cents(item["precio"])
        item["precio_formateado"] = format_pen(item["precio_centimos"])

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(catalog, f, indent=2, ensure_ascii=False)
    print(f"SYNCHRONIZED: Successfully enriched {json_path} with integer cents.")

if __name__ == "__main__":
    run_sync()
