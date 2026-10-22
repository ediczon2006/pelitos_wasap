"""
Generador de Enlaces Directos de WhatsApp (wa.me) con mensajes URL-encoded
y directorio de integración digital para Pelitos Veterinaria.
"""

import os
import json
import urllib.parse

ENLACES_DATA = [
    {
        "id": "REC-01",
        "canal": "Recepción",
        "telefono": "51927301122",
        "formato_legible": "927 301 122",
        "responsable": "Diego",
        "titulo": "Atención General e Información",
        "mensaje": "¡Hola Pelitos Veterinaria! 🐾 Deseo información general sobre sus servicios y horarios de atención.",
        "categoria": "General",
        "destino_web": "Botón Flotante Principal / Menú Contacto"
    },
    {
        "id": "REC-02",
        "canal": "Recepción",
        "telefono": "51927301122",
        "formato_legible": "927 301 122",
        "responsable": "Diego",
        "titulo": "Consulta de Farmacia Veterinaria",
        "mensaje": "¡Hola Pelitos! 💊 Quisiera consultar disponibilidad y precio de un producto en su farmacia veterinaria.",
        "categoria": "Farmacia",
        "destino_web": "Sección Farmacia Web / Catálogo Farmacia"
    },
    {
        "id": "REC-03",
        "canal": "Recepción",
        "telefono": "51927301122",
        "formato_legible": "927 301 122",
        "responsable": "Diego",
        "titulo": "Consulta de Pet Shop (Alimentos y Accesorios)",
        "mensaje": "¡Hola Pelitos! 🛍️ Deseo información sobre alimentos, snacks o accesorios disponibles en su Pet Shop.",
        "categoria": "Pet Shop",
        "destino_web": "Sección Pet Shop Web / Catálogo Pet Shop"
    },
    {
        "id": "MED-01",
        "canal": "Consultorio",
        "telefono": "51939356376",
        "formato_legible": "939 356 376",
        "responsable": "Dra. Julia",
        "titulo": "Reserva de Consulta Médica Veterinaria",
        "mensaje": "¡Hola Consultorio Pelitos! 🩺 Deseo agendar una cita médica veterinaria para evaluar la salud de mi mascota.",
        "categoria": "Medicina General",
        "destino_web": "Página de Servicios Médicos / Botón 'Agendar Cita Médica'"
    },
    {
        "id": "MED-02",
        "canal": "Consultorio",
        "telefono": "51939356376",
        "formato_legible": "939 356 376",
        "responsable": "Dra. Julia",
        "titulo": "Vacunación y Desparasitación Preventiva",
        "mensaje": "¡Hola Consultorio Pelitos! 💉 Deseo información sobre el calendario de vacunación y desparasitación para mi mascota.",
        "categoria": "Medicina Preventiva",
        "destino_web": "Campaña de Vacunación / Afiche Digital QR"
    },
    {
        "id": "MED-03",
        "canal": "Consultorio",
        "telefono": "51939356376",
        "formato_legible": "939 356 376",
        "responsable": "Dra. Julia",
        "titulo": "Consulta Quirúrgica y Esterilización",
        "mensaje": "¡Hola Consultorio Pelitos! 🏥 Quisiera consultar requisitos, costos y disponibilidad para esterilización / cirugía veterinaria.",
        "categoria": "Cirugía",
        "destino_web": "Página Web Cirugía / Tríptico Informativo QR"
    },
    {
        "id": "EST-01",
        "canal": "Estética",
        "telefono": "51948426656",
        "formato_legible": "948 426 656",
        "responsable": "Antonella",
        "titulo": "Cotización y Reserva de Estética / Spa",
        "mensaje": "¡Hola Estética Pelitos! ✂️🛁 Deseo consultar disponibilidad y cotizar una experiencia de baño / estética para mi engreído.",
        "categoria": "Estética General",
        "destino_web": "Página de Estética / Botón 'Reserva tu Baño'"
    },
    {
        "id": "EST-02",
        "canal": "Estética",
        "telefono": "51948426656",
        "formato_legible": "948 426 656",
        "responsable": "Antonella",
        "titulo": "Reserva de Spa Pelitos Relajante",
        "mensaje": "¡Hola Antonella! 🌿 Deseo consentir a mi peludito con la experiencia Spa Pelitos Relajante (hidromasaje y aromaterapia). ¿Qué horarios tienen disponibles?",
        "categoria": "Experiencias Spa",
        "destino_web": "Afiche Promocional Spa / Redes Sociales"
    },
    {
        "id": "EST-03",
        "canal": "Estética",
        "telefono": "51948426656",
        "formato_legible": "948 426 656",
        "responsable": "Antonella",
        "titulo": "Corte de Raza (Experiencia Momento Real)",
        "mensaje": "¡Hola Estética Pelitos! 👑 Deseo consultar precio y reservar un corte de raza especializado (Momento Real) para mi mascota.",
        "categoria": "Cortes y Estilo",
        "destino_web": "Galería de Fotos Web / Banner Instagram"
    }
]

def generar_enlaces():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.makedirs(os.path.join(base_dir, "data"), exist_ok=True)
    os.makedirs(os.path.join(base_dir, "05_integracion_digital"), exist_ok=True)

    lista_enlaces = []
    for item in ENLACES_DATA:
        encoded_text = urllib.parse.quote(item["mensaje"])
        url = f"https://wa.me/{item['telefono']}?text={encoded_text}"
        item_copy = dict(item)
        item_copy["url_directa"] = url
        item_copy["url_codificada"] = encoded_text
        lista_enlaces.append(item_copy)

    # Guardar en data/enlaces_whatsapp.json
    json_path = os.path.join(base_dir, "data", "enlaces_whatsapp.json")
    with open(json_path, mode="w", encoding="utf-8") as f:
        json.dump(lista_enlaces, f, indent=2, ensure_ascii=False)
    print(f"Generado JSON de Enlaces: {json_path}")

    # Generar directorio Markdown
    md_path = os.path.join(base_dir, "05_integracion_digital", "directorio_enlaces_wame.md")
    with open(md_path, mode="w", encoding="utf-8") as f:
        f.write("# PELITOS VETERINARIA — DIRECTORIO OFICIAL DE ENLACES WA.ME Y CÓDIGOS QR\n\n")
        f.write("> **Proyecto N.° 03:** Pelitos Conecta Comercial 2026  \n")
        f.write("> **Responsable:** EDICZON (Practicante) | **Supervisión:** Gerencia General  \n")
        f.write("> **Fecha:** 21 de octubre de 2026\n\n")
        f.write("Este directorio centraliza los enlaces directos oficiales con mensajes predeterminados codificados para conectar campañas publicitarias, códigos QR en clínica y botones de la página web institucional con las 3 cuentas de WhatsApp Business.\n\n")
        f.write("## 1. Relación de Enlaces Directos Oficiales\n\n")
        f.write("| ID | Canal / Número | Responsable | Servicio / Propósito | Enlace Directo (Clic para probar) |\n")
        f.write("|---|---|---|---|---|\n")
        for e in lista_enlaces:
            f.write(f"| **{e['id']}** | {e['canal']}<br>`{e['formato_legible']}` | {e['responsable']} | **{e['titulo']}** | [Abrir WhatsApp]({e['url_directa']}) |\n")
        
        f.write("\n\n## 2. Detalle de Mensajes Precargados por Canal\n\n")
        for e in lista_enlaces:
            f.write(f"### `{e['id']}` — {e['titulo']} ({e['canal']})\n")
            f.write(f"- **Número:** `+{e['telefono']}` (Atiende: {e['responsable']})\n")
            f.write(f"- **Categoría:** {e['categoria']}\n")
            f.write(f"- **Ubicación web/física:** {e['destino_web']}\n")
            f.write(f"- **Mensaje precargado:**\n")
            f.write(f"  > \"{e['mensaje']}\"\n")
            f.write(f"- **URL oficial:**\n")
            f.write(f"  ```text\n  {e['url_directa']}\n  ```\n\n")

    print(f"Generado Directorio Markdown: {md_path}")

if __name__ == "__main__":
    generar_enlaces()
