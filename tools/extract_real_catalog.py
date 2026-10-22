"""
Extracts the exact products and their data from pelitos_veterinaria/js/catalogo.js
"""

import json
import re

with open(r"C:\Users\edicz\Documents\proyecto_pelitos\pelitos_veterinaria\js\catalogo.js", "r", encoding="utf-8") as f:
    text = f.read()

# Locate PRODUCTOS = [ ... ];
start = text.find("var PRODUCTOS = [")
if start != -1:
    end = text.rfind("];")
    json_like = text[start + len("var PRODUCTOS = ["):end]

# Let's inspect titles and images
titles = re.findall(r'titulo:\s*"([^"]+)"', text)
images = re.findall(r'imagen:\s*"([^"]+)"', text)
prices = re.findall(r'precio:\s*([0-9.]+)', text)
categories = re.findall(r'categoria:\s*"([^"]+)"', text)

print(f"Found {len(titles)} products in catalogo.js:")
for t, img, p in zip(titles[:15], images[:15], prices[:15]):
    clean_img = img.replace("../images/productos/", "").replace("images/productos/", "")
    print(f"- {t} | S/ {p} | {clean_img}")
