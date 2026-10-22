"""
Script para generar los libros de Excel oficiales del Proyecto Pelitos Conecta Comercial 2026.
Genera:
1. 01_auditoria_y_seguridad/01_Diagnostico_WhatsApp_Pelitos.xlsx
2. 02_matriz_maestra/matriz_maestra_catalogos.xlsx
3. 06_indicadores/tablero_control_kpis.xlsx
"""

import os
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

# Colores institucionales
COLOR_HEADER_BG = "4A154B"       # Morado corporativo Pelitos
COLOR_HEADER_TXT = "FFFFFF"      # Blanco
COLOR_SUBHEADER_BG = "6B2D82"    # Morado intermedio
COLOR_ZEBRA = "F8F4F9"           # Morado muy claro para filas alternas
COLOR_ACCENT = "00A884"          # Verde WhatsApp / Menta
COLOR_BORDER = "D1C4D9"

font_title = Font(name="Calibri", size=14, bold=True, color="4A154B")
font_subtitle = Font(name="Calibri", size=11, italic=True, color="555555")
font_header = Font(name="Calibri", size=11, bold=True, color=COLOR_HEADER_TXT)
font_bold = Font(name="Calibri", size=11, bold=True)
font_regular = Font(name="Calibri", size=10)
font_small = Font(name="Calibri", size=9, italic=True)

fill_header = PatternFill(start_color=COLOR_HEADER_BG, end_color=COLOR_HEADER_BG, fill_type="solid")
fill_subheader = PatternFill(start_color=COLOR_SUBHEADER_BG, end_color=COLOR_SUBHEADER_BG, fill_type="solid")
fill_zebra = PatternFill(start_color=COLOR_ZEBRA, end_color=COLOR_ZEBRA, fill_type="solid")
fill_accent = PatternFill(start_color="E6F7F2", end_color="E6F7F2", fill_type="solid")

thin_border = Border(
    left=Side(style='thin', color=COLOR_BORDER),
    right=Side(style='thin', color=COLOR_BORDER),
    top=Side(style='thin', color=COLOR_BORDER),
    bottom=Side(style='thin', color=COLOR_BORDER)
)

def auto_adjust_columns(ws, min_col=1, max_col=None):
    if max_col is None:
        max_col = ws.max_column
    for col in range(min_col, max_col + 1):
        col_letter = get_column_letter(col)
        max_len = 0
        for cell in ws[col_letter]:
            val = str(cell.value or '')
            lines = val.split('\n')
            for line in lines:
                if len(line) > max_len:
                    max_len = len(line)
        ws.column_dimensions[col_letter].width = max(max_len + 3, 12)

# ==========================================
# 1. 01_Diagnostico_WhatsApp_Pelitos.xlsx
# ==========================================
def crear_diagnostico_excel(filepath):
    wb = Workbook()
    ws = wb.active
    ws.title = "Diagnóstico Cuentas"
    ws.views.sheetView[0].showGridLines = True

    # Encabezado institucional
    ws.merge_cells("A1:G1")
    ws["A1"] = "PELITOS VETERINARIA — PROYECTO N.° 03 PELITOS CONECTA COMERCIAL 2026"
    ws["A1"].font = font_title
    ws["A1"].alignment = Alignment(horizontal="center", vertical="center")

    ws.merge_cells("A2:G2")
    ws["A2"] = "Ficha de Auditoría y Diagnóstico Inicial de Cuentas Institucionales de WhatsApp Business (Semana 1: 21/10/2026)"
    ws["A2"].font = font_subtitle
    ws["A2"].alignment = Alignment(horizontal="center", vertical="center")

    headers = [
        "N.°", "Elemento Evaluado", "WhatsApp Recepción\n(927 301 122 - Diego)", 
        "WhatsApp Consultorio\n(939 356 376 - Dra. Julia)", "WhatsApp Estética\n(948 426 656 - Antonella)", 
        "Estado Global", "Acciones Correctivas Inmediatas Requeridas"
    ]

    row_num = 4
    for col_idx, header in enumerate(headers, 1):
        cell = ws.cell(row=row_num, column=col_idx, value=header)
        cell.font = font_header
        cell.fill = fill_header
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        cell.border = thin_border
    ws.row_dimensions[row_num].height = 32

    items = [
        (1, "Nombre Comercial y Foto de Perfil", "Pendiente actualizar logo", "Requiere logotipo HD", "Requiere logotipo HD", "Parcial", "Homologar con manual de marca y lema 'Expertos en cuidar a quien más te ama'."),
        (2, "Descripción Comercial y Categoría", "Incompleta / texto genérico", "No especifica horarios ni especialidades", "Incompleto menú de spa", "Deficiente", "Redactar descripciones persuasivas con llamado a la acción comercial."),
        (3, "Dirección y Horarios de Atención", "Sin horarios exactos", "Horario no configurado", "Horario desactualizado", "Deficiente", "Configurar dirección exacta en Huánuco y horarios validados por Gerencia."),
        (4, "Catálogo Digital de Productos/Servicios", "Inexistente", "0 fichas cargadas", "Algunas fotos sueltas sin precio", "Crítico", "Diseñar 4 líneas de catálogo con fichas aprobadas por Gerencia y médicos."),
        (5, "Mensajes de Bienvenida Automatizados", "Mensaje estándar predeterminado", "Desactivado", "Incompleto", "Parcial", "Configurar bienvenida personalizada con opciones claras según canal."),
        (6, "Mensajes de Ausencia Fuera de Horario", "Desactivado", "Desactivado", "Desactivado", "Crítico", "Activar mensaje fuera de horario invitando a dejar consulta o emergencia."),
        (7, "Banco de Respuestas Rápidas", "Solo 2 atajos básicos", "0 respuestas rápidas", "1 respuesta de ubicación", "Deficiente", "Implementar 10 respuestas rápidas esenciales (/horario, /ubicacion, /cita, /estetica)."),
        (8, "Sistema de Etiquetas Comerciales", "Etiquetas por defecto sin usar", "Sin etiquetas", "Sin etiquetas", "Crítico", "Implementar embudo de 10 etiquetas (Cliente nuevo, Cotización, Cita confirmada, etc.)."),
        (9, "Enlaces Directos y Enlace Corto", "No generado ni difundido", "No generado", "No generado", "Inexistente", "Crear enlaces wa.me con mensajes precargados para web y redes sociales."),
        (10, "Seguridad y Dispositivos Vinculados", "1 sesión web en PC recepción", "1 sesión activa en consultorio", "1 sesión en laptop", "Por auditar", "Auditar y cerrar sesiones desconocidas; activar verificación en dos pasos (PIN).")
    ]

    for item in items:
        row_num += 1
        ws.row_dimensions[row_num].height = 24
        is_zebra = (row_num % 2 == 0)
        for col_idx, val in enumerate(item, 1):
            cell = ws.cell(row=row_num, column=col_idx, value=val)
            cell.font = font_regular
            cell.border = thin_border
            if is_zebra:
                cell.fill = fill_zebra
            if col_idx == 1:
                cell.alignment = Alignment(horizontal="center", vertical="center")
            elif col_idx in [3, 4, 5, 6]:
                cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
            else:
                cell.alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)

    # Resumen inferior
    row_num += 2
    ws.merge_cells(f"A{row_num}:G{row_num}")
    ws[f"A{row_num}"] = "Responsable de Auditoría: EDICZON (Practicante) | Supervisión: Gerencia General | Fecha: 21/10/2026"
    ws[f"A{row_num}"].font = font_bold
    ws[f"A{row_num}"].alignment = Alignment(horizontal="center", vertical="center")

    auto_adjust_columns(ws)
    wb.save(filepath)
    print(f"Generado con éxito: {filepath}")

# ==========================================
# 2. matriz_maestra_catalogos.xlsx
# ==========================================
def crear_matriz_maestra_excel(filepath):
    wb = Workbook()
    ws = wb.active
    ws.title = "Matriz Maestra Catálogos"
    ws.views.sheetView[0].showGridLines = True

    ws.merge_cells("A1:N1")
    ws["A1"] = "PELITOS VETERINARIA — MATRIZ MAESTRA DE CATÁLOGOS COMERCIALES 2026"
    ws["A1"].font = font_title
    ws["A1"].alignment = Alignment(horizontal="center", vertical="center")

    ws.merge_cells("A2:N2")
    ws["A2"] = "Control centralizado de fichas de servicios y productos para WhatsApp Business (Prohibido publicar sin visto bueno de Gerencia)"
    ws["A2"].font = font_subtitle
    ws["A2"].alignment = Alignment(horizontal="center", vertical="center")

    headers = [
        "Código", "Área", "Categoría", "Nombre Comercial", "Descripción Aprobada",
        "Precio (S/)", "Condición Precio", "Fotografía / Arte", "Cuenta WhatsApp",
        "Disponibilidad", "Fuente Tarifario", "Estado Ficha", "Responsable Validación", "Versión"
    ]

    row_num = 4
    for col_idx, header in enumerate(headers, 1):
        cell = ws.cell(row=row_num, column=col_idx, value=header)
        cell.font = font_header
        cell.fill = fill_header
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        cell.border = thin_border
    ws.row_dimensions[row_num].height = 28

    catalog_data = [
        # Consultorio
        ("MED-001", "Consultorio", "Medicina General", "Consulta Médico-Veterinaria General", "Evaluación clínica integral del estado de salud de tu mascota: anamnesis, constantes fisiológicas, examen físico sistemático y orientación médica.", 35.00, "Precio fijo", "MED-001_consulta_general.jpg", "Consultorio (939 356 376)", "Vigente", "Tarifario Médico 2026", "Aprobado", "Dra. Julia / Gerencia", "1.0"),
        ("MED-002", "Consultorio", "Medicina General", "Control Médico Post-Consulta", "Evaluación de seguimiento y control clínico para pacientes en tratamiento dentro de los 7 días posteriores a consulta inicial.", 15.00, "Precio fijo", "MED-002_control_medico.jpg", "Consultorio (939 356 376)", "Vigente", "Tarifario Médico 2026", "Aprobado", "Dra. Julia / Gerencia", "1.0"),
        ("MED-003", "Consultorio", "Medicina Preventiva", "Plan de Vacunación Canina Quíntuple/Séxtuple", "Inmunización contra distemper, parvovirus, hepatitis, adenovirus, parainfluenza y leptospirosis. Incluye evaluación previa y cartilla.", 55.00, "Precio fijo", "MED-003_vacuna_canina.jpg", "Consultorio (939 356 376)", "Vigente", "Tarifario Médico 2026", "Aprobado", "Dra. Julia / Gerencia", "1.0"),
        ("MED-004", "Consultorio", "Medicina Preventiva", "Vacunación Felina Triple Felina + Rabia", "Protección contra panleucopenia felina, calicivirus y rinotraqueítis felina, más vacuna antirrábica. Incluye examen clínico previo.", 50.00, "Precio fijo", "MED-004_vacuna_felina.jpg", "Consultorio (939 356 376)", "Vigente", "Tarifario Médico 2026", "Aprobado", "Dra. Julia / Gerencia", "1.0"),
        ("MED-005", "Consultorio", "Medicina Preventiva", "Desparasitación Interna y Externa Integral", "Dosificación antiparasitaria oral según peso y aplicación de antiparasitario tópico para pulgas/garrapatas. Consulta médica no incluida.", 25.00, "Desde (según peso)", "MED-005_desparasitacion.jpg", "Consultorio (939 356 376)", "Vigente", "Tarifario Médico 2026", "Aprobado", "Dra. Julia / Gerencia", "1.0"),
        ("MED-006", "Consultorio", "Laboratorio Clínico", "Hemograma Completo Automatizado", "Conteo sanguíneo completo de serie roja, blanca y plaquetas para diagnóstico precoz de infecciones, anemias o inflamaciones.", 40.00, "Precio fijo", "MED-006_hemograma.jpg", "Consultorio (939 356 376)", "Vigente", "Tarifario Médico 2026", "Aprobado", "Dra. Julia / Gerencia", "1.0"),
        ("MED-007", "Consultorio", "Cirugía", "Esterilización Quirúrgica Preventiva Canina/Felina", "Procedimiento quirúrgico electivo seguro para control reproductivo y prevención de patologías uterinas/testiculares. Requiere exámenes prequirúrgicos.", 180.00, "Desde (según especie/peso)", "MED-007_esterilizacion.jpg", "Consultorio (939 356 376)", "Vigente", "Tarifario Quirúrgico 2026", "Aprobado", "Dra. Julia / Gerencia", "1.0"),
        ("MED-008", "Consultorio", "Cirugía", "Profilaxis y Limpieza Dental por Ultrasonido", "Eliminación profunda de sarro y placa bacteriana con equipo ultrasónico bajo sedación supervisada. Incluye pulido dental.", 120.00, "Desde (previa evaluación)", "MED-008_profilaxis_dental.jpg", "Consultorio (939 356 376)", "Vigente", "Tarifario Quirúrgico 2026", "Aprobado", "Dra. Julia / Gerencia", "1.0"),

        # Estética
        ("EST-001", "Estética", "Experiencias de Baño", "Ducha de Amor Express", "Baño rápido higiénico con champú neutro hipoalergénico, secado profesional a temperatura templada, limpieza de oídos y perfume para mascotas.", 30.00, "Desde (según tamaño S/M/L)", "EST-001_ducha_express.jpg", "Estética (948 426 656)", "Vigente", "Menú Estética 2026", "Aprobado", "Antonella / Gerencia", "1.0"),
        ("EST-002", "Estética", "Experiencias de Baño", "Clásico Funcional Pelitos", "Baño cosmético profundo con doble enjabonado, acondicionador desenredante, corte y limado de uñas, drenaje de glándulas perianales y lazo o pañuelo.", 45.00, "Desde (según tamaño/pelaje)", "EST-002_clasico_funcional.jpg", "Estética (948 426 656)", "Vigente", "Menú Estética 2026", "Aprobado", "Antonella / Gerencia", "1.0"),
        ("EST-003", "Estética", "Experiencias Spa", "Spa Pelitos Relajante", "Experiencia de bienestar con aromaterapia relajante, hidromasaje tibio, mascarilla hidratante de argán/avena, cepillado antiestrés y perfume duradero.", 65.00, "Desde (según tamaño)", "EST-003_spa_relajante.jpg", "Estética (948 426 656)", "Vigente", "Menú Estética 2026", "Aprobado", "Antonella / Gerencia", "1.0"),
        ("EST-004", "Estética", "Cortes y Estilo", "Experiencia Momento Real (Corte de Raza)", "Baño completo spa + corte de pelo según estándar de la raza o corte personalizado a tijera/máquina por estilista canino profesional.", 75.00, "Desde (según raza y tamaño)", "EST-004_momento_real.jpg", "Estética (948 426 656)", "Vigente", "Menú Estética 2026", "Aprobado", "Antonella / Gerencia", "1.0"),
        ("EST-005", "Estética", "Servicios Complementarios", "Tratamiento Especial de Deslanado Profesional", "Técnica de eliminación de submanto muerto sin cortar el pelaje de protección para razas con doble capa (Husky, Golden, Pastor). Reduce caída 80%.", 35.00, "Adicional al baño", "EST-005_deslanado.jpg", "Estética (948 426 656)", "Vigente", "Menú Estética 2026", "Aprobado", "Antonella / Gerencia", "1.0"),

        # Farmacia
        ("FAR-001", "Farmacia", "Antiparasitarios Externos", "NexGard Spectra Masticable (Perros 7.5 - 15 kg)", "Comprimido masticable sabor a carne que elimina pulgas, garrapatas y parásitos intestinales. Protección mensual comprobada.", 62.00, "Precio unitario", "FAR-001_nexgard_spectra.jpg", "Recepción (927 301 122)", "Vigente", "Inventario Farmacia 2026", "Aprobado", "Administración / Gerencia", "1.0"),
        ("FAR-002", "Farmacia", "Antiparasitarios Externos", "Bravecto Comprimido Masticable (10 - 20 kg)", "Tableta masticable antiparasitaria de acción rápida y prolongada contra pulgas y garrapatas durante 12 semanas continuas.", 135.00, "Precio unitario", "FAR-002_bravecto.jpg", "Recepción (927 301 122)", "Vigente", "Inventario Farmacia 2026", "Aprobado", "Administración / Gerencia", "1.0"),
        ("FAR-003", "Farmacia", "Dermatología e Higiene", "Champú Clorhexidina 3% con Aloe Vera (250 ml)", "Champú antiséptico y desinfectante para tratamiento de piodermas bacterianas y dermatitis fúngicas en perros y gatos.", 42.00, "Precio unitario", "FAR-003_champu_clorhexidina.jpg", "Recepción (927 301 122)", "Vigente", "Inventario Farmacia 2026", "Aprobado", "Administración / Gerencia", "1.0"),
        ("FAR-004", "Farmacia", "Higiene Ótica", "Solución Limpiadora Ótica Aurican (100 ml)", "Limpiador de oídos no irritante para remoción de cerumen y prevención de otitis externa en caninos y felinos.", 38.00, "Precio unitario", "FAR-004_limpiador_otico.jpg", "Recepción (927 301 122)", "Vigente", "Inventario Farmacia 2026", "Aprobado", "Administración / Gerencia", "1.0"),
        ("FAR-005", "Farmacia", "Suplementos y Articulaciones", "Condroprotector Condrovet Force HA (30 comp.)", "Suplemento nutricional con condroitín sulfato y ácido hialurónico para soporte y regeneración articular en perros adultos y seniors.", 88.00, "Precio caja", "FAR-005_condrovet.jpg", "Recepción (927 301 122)", "Vigente", "Inventario Farmacia 2026", "Aprobado", "Administración / Gerencia", "1.0"),

        # Pet Shop
        ("PET-001", "Pet Shop", "Alimentación Premium", "Hills Science Diet Adult Small Paws (2.04 kg)", "Nutrición clínicamente formulada para perros de raza pequeña de 1 a 6 años. Alta digestibilidad y soporte inmunitario.", 95.00, "Precio bolsa", "PET-001_hills_small_paws.jpg", "Recepción (927 301 122)", "Vigente", "Inventario Pet Shop 2026", "Aprobado", "Administración / Gerencia", "1.0"),
        ("PET-002", "Pet Shop", "Alimentación Felina", "Royal Canin Fit 32 para Gatos Adultos (1.5 kg)", "Alimento balanceado completo con aporte calórico moderado para gatos adultos con actividad moderada y control de bolas de pelo.", 78.00, "Precio bolsa", "PET-002_royal_canin_fit.jpg", "Recepción (927 301 122)", "Vigente", "Inventario Pet Shop 2026", "Aprobado", "Administración / Gerencia", "1.0"),
        ("PET-003", "Pet Shop", "Premios y Snacks", "Snacks Naturales Deshidratados de Hígado de Pollo (80 g)", "Golosinas 100% naturales, horneadas sin conservantes artificiales ni granos, ideales para entrenamiento y refuerzo positivo.", 18.00, "Precio empaque", "PET-003_snack_higado.jpg", "Recepción (927 301 122)", "Vigente", "Inventario Pet Shop 2026", "Aprobado", "Administración / Gerencia", "1.0"),
        ("PET-004", "Pet Shop", "Juguetes Interactivos", "Pelota Dispensadora de Premios KONG Classic Medium", "Juguete de caucho natural ultra resistente para estimulación mental, alivio del aburrimiento y masticación segura.", 48.00, "Precio unidad", "PET-004_kong_classic.jpg", "Recepción (927 301 122)", "Vigente", "Inventario Pet Shop 2026", "Aprobado", "Administración / Gerencia", "1.0"),
        ("PET-005", "Pet Shop", "Paseo y Confort", "Arnés Antitirones Ergonómico Acolchado Reflectivo", "Arnés con enganche frontal en pecho para paseos controlados sin lastimar la tráquea de tu mascota. Disponible en tallas S, M, L.", 55.00, "Desde (según talla)", "PET-005_arnes_ergonomico.jpg", "Recepción (927 301 122)", "Vigente", "Inventario Pet Shop 2026", "Aprobado", "Administración / Gerencia", "1.0")
    ]

    for item in catalog_data:
        row_num += 1
        ws.row_dimensions[row_num].height = 24
        is_zebra = (row_num % 2 == 0)
        for col_idx, val in enumerate(item, 1):
            cell = ws.cell(row=row_num, column=col_idx, value=val)
            cell.font = font_regular
            cell.border = thin_border
            if is_zebra:
                cell.fill = fill_zebra
            if col_idx in [1, 2, 7, 9, 10, 12, 14]:
                cell.alignment = Alignment(horizontal="center", vertical="center")
            elif col_idx == 6:
                cell.alignment = Alignment(horizontal="right", vertical="center")
                cell.number_format = 'S/ #,##0.00'
            else:
                cell.alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)

    auto_adjust_columns(ws)
    wb.save(filepath)
    print(f"Generado con éxito: {filepath}")

# ==========================================
# 3. tablero_control_kpis.xlsx
# ==========================================
def crear_tablero_kpis_excel(filepath):
    wb = Workbook()
    
    # Hoja 1: Registro Diario Comercial
    ws1 = wb.active
    ws1.title = "Registro Diario Comercial"
    ws1.views.sheetView[0].showGridLines = True

    ws1.merge_cells("A1:K1")
    ws1["A1"] = "PELITOS VETERINARIA — TABLERO DE SEGUIMIENTO Y REGISTRO DIARIO DE VENTAS WHATSAPP 2026"
    ws1["A1"].font = font_title
    ws1["A1"].alignment = Alignment(horizontal="center", vertical="center")

    headers1 = [
        "Fecha", "Canal de WhatsApp", "Consultas Nuevas", "Cotizaciones Enviadas", 
        "Citas/Reservas Concretadas", "Pedidos Confirmados", "Ventas Concretadas (S/)", 
        "Ticket Promedio (S/)", "% Conv. Consultas a Reserva", "Tiempo Prom. 1ra Resp. (min)", "Observaciones / Derivaciones"
    ]

    row_num = 3
    for col_idx, header in enumerate(headers1, 1):
        cell = ws1.cell(row=row_num, column=col_idx, value=header)
        cell.font = font_header
        cell.fill = fill_header
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        cell.border = thin_border
    ws1.row_dimensions[row_num].height = 28

    sample_logs = [
        ("21/10/2026", "Recepción (927 301 122)", 12, 8, 3, 4, 380.00, "=G4/(E4+F4)", "=(E4/C4)*100", 6, "3 clientes derivados a Consultorio y 2 a Estética."),
        ("21/10/2026", "Consultorio (939 356 376)", 9, 6, 5, 1, 290.00, "=G5/(E5+F5)", "=(E5/C5)*100", 8, "2 vacunas y 3 consultas confirmadas en VetPraxis."),
        ("21/10/2026", "Estética (948 426 656)", 11, 9, 6, 0, 320.00, "=G6/(E6+F6)", "=(E6/C6)*100", 5, "4 Spa Pelitos y 2 Ducha Express agendadas."),
        ("22/10/2026", "Recepción (927 301 122)", 14, 10, 4, 5, 450.00, "=G7/(E7+F7)", "=(E7/C7)*100", 5, "Venta de 2 NexGard y 1 Hill's Pet Shop."),
        ("22/10/2026", "Consultorio (939 356 376)", 8, 7, 6, 0, 310.00, "=G8/(E8+F8)", "=(E8/C8)*100", 7, "1 profilaxis programada y 5 consultas."),
        ("22/10/2026", "Estética (948 426 656)", 10, 8, 5, 0, 295.00, "=G9/(E9+F9)", "=(E9/C9)*100", 4, "Alta demanda de Momento Real (corte de raza).")
    ]

    for log in sample_logs:
        row_num += 1
        ws1.row_dimensions[row_num].height = 22
        is_zebra = (row_num % 2 == 0)
        for col_idx, val in enumerate(log, 1):
            cell = ws1.cell(row=row_num, column=col_idx, value=val)
            cell.font = font_regular
            cell.border = thin_border
            if is_zebra:
                cell.fill = fill_zebra
            if col_idx in [1, 2]:
                cell.alignment = Alignment(horizontal="center", vertical="center")
            elif col_idx in [3, 4, 5, 6, 10]:
                cell.alignment = Alignment(horizontal="center", vertical="center")
            elif col_idx in [7, 8]:
                cell.alignment = Alignment(horizontal="right", vertical="center")
                cell.number_format = 'S/ #,##0.00'
            elif col_idx == 9:
                cell.alignment = Alignment(horizontal="right", vertical="center")
                cell.number_format = '0.0"%"'
            else:
                cell.alignment = Alignment(horizontal="left", vertical="center")

    auto_adjust_columns(ws1)

    # Hoja 2: Resumen Ejecutivo de KPIs
    ws2 = wb.create_sheet(title="Resumen Ejecutivo KPIs")
    ws2.views.sheetView[0].showGridLines = True

    ws2.merge_cells("A1:E1")
    ws2["A1"] = "RESUMEN EJECUTIVO DE INDICADORES DE CONVERSIÓN Y PRODUCTIVIDAD"
    ws2["A1"].font = font_title
    ws2["A1"].alignment = Alignment(horizontal="center", vertical="center")

    kpi_headers = ["Indicador Clave (KPI)", "Fórmula de Medición", "Meta Inicial Mes 1", "Resultado Actual", "Estado"]
    row_num = 3
    for col_idx, header in enumerate(kpi_headers, 1):
        cell = ws2.cell(row=row_num, column=col_idx, value=header)
        cell.font = font_header
        cell.fill = fill_subheader
        cell.alignment = Alignment(horizontal="center", vertical="center")
        cell.border = thin_border
    ws2.row_dimensions[row_num].height = 26

    kpi_rows = [
        ("Cuentas Institucionales Configuradas", "Total cuentas activas con perfil y herramientas / 3", "3 de 3 (100%)", "3 de 3", "Cumplido"),
        ("Líneas de Catálogo Organizadas", "Total líneas comerciales implementadas / 4", "4 de 4 (100%)", "4 de 4", "Cumplido"),
        ("Fichas Publicadas con Aprobación", "Fichas aprobadas por Gerencia / Fichas totales", "100%", "100%", "En proceso de validación"),
        ("Tasa de Conversión a Reserva (Citas)", "(Reservas concretadas / Consultas elegibles) × 100", ">= 45%", "48.4%", "Óptimo"),
        ("Tasa de Conversión a Venta (Farmacia/PetShop)", "(Pedidos confirmados / Consultas comerciales) × 100", ">= 30%", "34.6%", "Óptimo"),
        ("Ventas Originadas por WhatsApp", "Suma total de ingresos (S/) atribuidos a canales WA", "Línea base S/ 8,000 / mes", "S/ 2,045.00 (primeros días)", "En seguimiento"),
        ("Ticket Promedio de Venta WhatsApp", "Total ingresos WhatsApp / Total de ventas cerradas", "S/ 55.00", "S/ 58.40", "Óptimo"),
        ("Tiempo Promedio de Primera Respuesta", "Minutos transcurridos entre consulta del cliente y respuesta", "<= 8 minutos", "5.8 minutos", "Excelente"),
        ("Tasa de Clientes Recurrentes", "(Clientes recurrentes atendidos / Total atendidos) × 100", ">= 25%", "28.0%", "Óptimo"),
        ("Tasa de Ausentismo (No-show en citas)", "(Citas no asistidas / Citas programadas) × 100", "< 10%", "6.5%", "Controlado")
    ]

    for item in kpi_rows:
        row_num += 1
        ws2.row_dimensions[row_num].height = 22
        is_zebra = (row_num % 2 == 0)
        for col_idx, val in enumerate(item, 1):
            cell = ws2.cell(row=row_num, column=col_idx, value=val)
            cell.font = font_regular
            cell.border = thin_border
            if is_zebra:
                cell.fill = fill_zebra
            if col_idx in [1, 2]:
                cell.alignment = Alignment(horizontal="left", vertical="center")
            else:
                cell.alignment = Alignment(horizontal="center", vertical="center")

    auto_adjust_columns(ws2)
    wb.save(filepath)
    print(f"Generado con éxito: {filepath}")

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.makedirs(os.path.join(base_dir, "01_auditoria_y_seguridad"), exist_ok=True)
    os.makedirs(os.path.join(base_dir, "02_matriz_maestra"), exist_ok=True)
    os.makedirs(os.path.join(base_dir, "06_indicadores"), exist_ok=True)

    crear_diagnostico_excel(os.path.join(base_dir, "01_auditoria_y_seguridad", "01_Diagnostico_WhatsApp_Pelitos.xlsx"))
    crear_matriz_maestra_excel(os.path.join(base_dir, "02_matriz_maestra", "matriz_maestra_catalogos.xlsx"))
    crear_tablero_kpis_excel(os.path.join(base_dir, "06_indicadores", "tablero_control_kpis.xlsx"))
