"""
Test Suite: test_commercial_core.py
Framework: pytest
Purpose: Verification of integer-cents arithmetic, domain routing, schema conformity,
and zero-trust integrity contracts across PetShop, Estética, and Servicios.
"""

import os
import json
import re
from collections import Counter
import pytest

CANONICAL_CHANNELS = {
    "RECEPCION": "51927301122",
    "CONSULTORIO": "51939356376",
    "ESTETICA": "51948426656"
}

def to_cents(soles: float) -> int:
    return int(round(soles * 100))

def apply_discount(base_cents: int, cut_cents: int, discount_pct: float) -> int:
    subtotal = base_cents + cut_cents
    discount = int(round(subtotal * (discount_pct / 100.0)))
    return subtotal - discount

class TestFinancialCalculus:
    def test_float_precision_immunity(self):
        # Traditional IEEE-754 error: 0.1 + 0.2 != 0.3
        # In cents: 10 + 20 == 30
        c1 = to_cents(0.10)
        c2 = to_cents(0.20)
        assert c1 + c2 == 30

    def test_estetica_combo_discount(self):
        # Service base: 45.00 (4500 cents), Cut: 20.00 (2000 cents), 10% discount
        base = 4500
        cut = 2000
        final_cents = apply_discount(base, cut, 10.0)
        # subtotal: 6500 cents -> 10% is 650 cents -> total: 5850 cents (S/ 58.50)
        assert final_cents == 5850

class TestDomainRouting:
    def test_routing_matrix_integrity(self):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        json_path = os.path.join(base_dir, "data", "catalogo_maestro.json")
        with open(json_path, "r", encoding="utf-8") as f:
            catalog = json.load(f)

        assert len(catalog) == 23

        for item in catalog:
            area = item["area"]
            phone = item["telefono"]

            if area in ["Pet Shop", "Farmacia"]:
                assert phone == CANONICAL_CHANNELS["RECEPCION"], f"Item {item['codigo']} misrouted to {phone}"
            elif area == "Consultorio":
                assert phone == CANONICAL_CHANNELS["CONSULTORIO"], f"Item {item['codigo']} misrouted to {phone}"
            elif area == "Estética":
                assert phone == CANONICAL_CHANNELS["ESTETICA"], f"Item {item['codigo']} misrouted to {phone}"
            else:
                pytest.fail(f"Unknown area: {area}")

    def test_quick_replies_integrity(self):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        json_path = os.path.join(base_dir, "data", "respuestas_rapidas.json")
        with open(json_path, "r", encoding="utf-8") as f:
            replies = json.load(f)

        codes = [r["codigo"] for r in replies]
        assert "/horario" in codes
        assert "/ubicacion" in codes
        assert "/cita_medica" in codes
        assert "/estetica_cotizar" in codes
        assert "/farmacia" in codes
        assert "/petshop" in codes
        assert len(codes) >= 11

    def test_catalog_image_uniqueness_and_phone_isolation(self):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        
        test_cases = [
            ("catalogo_recepcion.html", CANONICAL_CHANNELS["RECEPCION"], "../pelitos_veterinaria/pages/productos.html", 125),
            ("catalogo_consultorio.html", CANONICAL_CHANNELS["CONSULTORIO"], "../pelitos_veterinaria/pages/servicios.html", 14),
            ("catalogo_estetica.html", CANONICAL_CHANNELS["ESTETICA"], "../pelitos_veterinaria/pages/estetica.html", 28),
        ]

        for filename, expected_phone, expected_link, expected_min_items in test_cases:
            filepath = os.path.join(base_dir, filename)
            assert os.path.exists(filepath), f"Missing file: {filename}"
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()

            # 1. Zero duplicate images within catalog
            imgs = re.findall(r'src=["\'](assets/images/[^"\']+)["\']', content)
            assert len(imgs) >= expected_min_items, f"{filename} has {len(imgs)} items, expected at least {expected_min_items}"
            counts = Counter(imgs)
            dupes = {k: v for k, v in counts.items() if v > 1}
            assert len(dupes) == 0, f"Duplicate images in {filename}: {dupes}"

            # 2. Strict phone isolation (zero cross-contamination)
            phones = set(re.findall(r'519\d{8}', content))
            assert phones == {expected_phone}, f"Phone isolation breach in {filename}: expected {{{expected_phone}}}, found {phones}"

            # 3. Direct web link present
            assert expected_link in content, f"Direct link {expected_link} missing in {filename}"

            # 4. All referenced images exist physically on disk
            for img_rel in imgs:
                img_path = os.path.join(base_dir, img_rel)
                assert os.path.exists(img_path), f"Asset {img_rel} missing on disk referenced in {filename}"

    def test_hub_portal_integrity(self):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        hub_path = os.path.join(base_dir, "index.html")
        assert os.path.exists(hub_path), "index.html missing"
        with open(hub_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Check links to all 3 catalogs
        assert "catalogo_recepcion.html" in content
        assert "catalogo_consultorio.html" in content
        assert "catalogo_estetica.html" in content

        # Check links to official web pages
        assert "../pelitos_veterinaria/index.html" in content
        assert "../pelitos_veterinaria/pages/productos.html" in content
        assert "../pelitos_veterinaria/pages/servicios.html" in content
        assert "../pelitos_veterinaria/pages/estetica.html" in content

        # Check all 3 canonical phones exist in the hub
        for phone in CANONICAL_CHANNELS.values():
            assert phone in content, f"Canonical phone {phone} missing in index.html"

        # Check link center elements
        assert "urlHub" in content
        assert "urlRec" in content
        assert "urlMed" in content
        assert "urlEst" in content
