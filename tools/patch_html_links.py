"""
Patch script for hardcoded links in servicios.html and productos.html
"""

def patch_html():
    # 1. Patch servicios.html
    servicios_path = r"C:\Users\edicz\Documents\proyecto_pelitos\pelitos_veterinaria\pages\servicios.html"
    with open(servicios_path, "r", encoding="utf-8") as f:
        servicios_html = f.read()

    old_farmacia = 'href="https://api.whatsapp.com/send?phone=51939356376&text=Hola%20Pelitos%2C%20quiero%20solicitar%20una%20cita%20de%20Farmacia%20veterinaria."'
    new_farmacia = 'href="https://api.whatsapp.com/send?phone=51927301122&text=Hola%20Pelitos%2C%20quiero%20consultar%20disponibilidad%20y%20precios%20en%20Farmacia%20veterinaria."'
    if old_farmacia in servicios_html:
        servicios_html = servicios_html.replace(old_farmacia, new_farmacia)
        print("Updated farmacia link in servicios.html")

    with open(servicios_path, "w", encoding="utf-8", newline="") as f:
        f.write(servicios_html)

    # 2. Patch productos.html
    productos_path = r"C:\Users\edicz\Documents\proyecto_pelitos\pelitos_veterinaria\pages\productos.html"
    with open(productos_path, "r", encoding="utf-8") as f:
        productos_html = f.read()

    old_fab = 'href="https://api.whatsapp.com/send?phone=51939356376&amp;text=Hola%20Pelitos%2C%20quiero%20hacer%20un%20pedido%20de%20PetShop."'
    new_fab = 'href="https://api.whatsapp.com/send?phone=51927301122&amp;text=Hola%20Pelitos%2C%20quiero%20hacer%20un%20pedido%20de%20PetShop."'
    if old_fab in productos_html:
        productos_html = productos_html.replace(old_fab, new_fab)
        print("Updated floating button in productos.html")

    with open(productos_path, "w", encoding="utf-8", newline="") as f:
        f.write(productos_html)

if __name__ == "__main__":
    patch_html()
