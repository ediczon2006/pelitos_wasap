"""
Production patch script for pelitos_veterinaria code base:
1. Re-routes WhatsApp channels to 3-tier architecture (recepcion, consultorio, estetica).
2. Fixes PetShop cart dispatch destination from consultorio to recepcion.
3. Fixes Estética quotation floating point calculus to integer cents.
"""

import os
import re

def patch_main_js(main_path):
    with open(main_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update SITE.whatsapp
    target_site = """const SITE = {
  nombre: "Pelitos Veterinaria",
  whatsapp: {
    consultorio: "51939356376",   // consultas, citas medicas y PetShop
    estetica: "51948426656",      // Pelitos Estetica y Spa Canino
  },
};"""

    replacement_site = """const SITE = {
  nombre: "Pelitos Veterinaria",
  whatsapp: {
    recepcion: "51927301122",     // Orientacion general, PetShop y Farmacia (Diego)
    consultorio: "51939356376",   // Consultas medicas, cirugias, vacunas y triaje (Dra. Julia)
    estetica: "51948426656",      // Pelitos Estetica, Grooming y Spa Canino (Antonella)
  },
};

function normalizarCanalWhatsapp(destino) {
  if (!destino) return SITE.whatsapp.recepcion;
  if (SITE.whatsapp[destino]) return SITE.whatsapp[destino];
  const digitos = String(destino).replace(/\\D/g, "");
  return digitos.length >= 9 ? digitos : SITE.whatsapp.recepcion;
}"""

    if target_site in content:
        content = content.replace(target_site, replacement_site)
        print("Updated SITE.whatsapp in main.js")
    else:
        # Try regex with CRLF tolerance
        pattern = re.compile(
            r'const SITE = \{\s*nombre: "Pelitos Veterinaria",\s*whatsapp: \{\s*consultorio: "51939356376",\s*//[^\n]*\s*estetica: "51948426656",\s*//[^\n]*\s*\},\s*\};',
            re.MULTILINE
        )
        if pattern.search(content):
            content = pattern.sub(replacement_site, content, count=1)
            print("Updated SITE.whatsapp in main.js via regex")
        else:
            print("SITE.whatsapp already updated or pattern not found in main.js")

    # 2. Update enlaceWhatsapp signature in main.js
    old_enlace = 'function enlaceWhatsapp(texto, numero = SITE.whatsapp.consultorio) {'
    new_enlace = 'function enlaceWhatsapp(texto, canalODestino = SITE.whatsapp.consultorio) {\n  const numero = normalizarCanalWhatsapp(canalODestino);'
    if old_enlace in content:
        content = content.replace(old_enlace, new_enlace)
        print("Updated enlaceWhatsapp signature in main.js")

    # 3. Fix float math in recalcularCotizador (Bloque 9)
    # const montoDescuento = aplicaDescuentoCombo ? ((precioBase + costoCorte) * 0.10) : 0;
    old_discount = 'const montoDescuento = aplicaDescuentoCombo ? ((precioBase + costoCorte) * 0.10) : 0;'
    new_discount = '// Precision numerica: calculo exacto en centimos para prevenir deriva IEEE-754\n    const subtotalCentimos = Math.round((precioBase + costoCorte) * 100);\n    const montoDescuento = aplicaDescuentoCombo ? (Math.round(subtotalCentimos * 0.10) / 100) : 0;'
    if old_discount in content:
        content = content.replace(old_discount, new_discount)
        print("Updated float math in recalcularCotizador to integer cents")

    with open(main_path, 'w', encoding='utf-8', newline='') as f:
        f.write(content)

def patch_productos_js(prod_path):
    with open(prod_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Update WHATSAPP fallback in productos.js
    old_wa = 'var WHATSAPP = (window.SITE && window.SITE.whatsapp && window.SITE.whatsapp.consultorio) || "51939356376";'
    new_wa = 'var WHATSAPP = (window.SITE && window.SITE.whatsapp && (window.SITE.whatsapp.recepcion || window.SITE.whatsapp.consultorio)) || "51927301122";'

    if old_wa in content:
        content = content.replace(old_wa, new_wa)
        print("Updated WHATSAPP routing in productos.js to recepcion (51927301122)")
    else:
        print("WHATSAPP in productos.js already patched or not found")

    with open(prod_path, 'w', encoding='utf-8', newline='') as f:
        f.write(content)

if __name__ == "__main__":
    base_dir = r"C:\Users\edicz\Documents\proyecto_pelitos\pelitos_veterinaria\js"
    patch_main_js(os.path.join(base_dir, "main.js"))
    patch_productos_js(os.path.join(base_dir, "productos.js"))
