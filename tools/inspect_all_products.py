"""
Inspects productos-nuevos.js and catalogo.js to extract all real products and images
"""

import re
import json

def parse_file(path):
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    # Find blocks of objects
    # Find all { ... } containing id, titulo, precio, imagen
    matches = re.findall(r'id:\s*"([^"]+)",[\s\S]*?titulo:\s*"([^"]+)",[\s\S]*?imagen:\s*"([^"]+)",[\s\S]*?precio:\s*([0-9.]+)', text)
    print(f"File {path}: matched {len(matches)} products")
    for m in matches[:10]:
        print(f"  ID: {m[0]} | Title: {m[1]} | Price: {m[3]} | Img: {m[2]}")
    return matches

print("=== CATALOGO.JS ===")
m1 = parse_file(r"C:\Users\edicz\Documents\proyecto_pelitos\pelitos_veterinaria\js\catalogo.js")

print("\n=== PRODUCTOS-NUEVOS.JS ===")
m2 = parse_file(r"C:\Users\edicz\Documents\proyecto_pelitos\pelitos_veterinaria\js\productos-nuevos.js")
