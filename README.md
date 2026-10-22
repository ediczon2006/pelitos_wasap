# 🐾 PELITOS VETERINARIA — PROYECTO N.° 03: PELITOS CONECTA COMERCIAL 2026

> **«Expertos en cuidar a quien más te ama»**  
> **Ubicación:** Huánuco, Perú  
> **Responsable Técnico:** EDICZON – Practicante de Ingeniería de Software  
> **Supervisión y Aprobación:** Gerencia General  
> **Áreas Beneficiarias:** Recepción, Consultorio Médico, Estética, Farmacia Veterinaria y Pet Shop  
> **Periodo de Ejecución:** 21 de octubre de 2026 al 17 de noviembre de 2026 (4 semanas)  
> **Presupuesto:** S/ 0 en nuevas suscripciones (WhatsApp Business gratuito, VetPraxis, Google Contacts y hojas de control)

---

## 📋 I. Resumen Ejecutivo del Proyecto

El proyecto **Pelitos Conecta Comercial 2026** transforma los tres números telefónicos institucionales de Pelitos Veterinaria en un ecosistema digital comercial organizado, profesional y medible. 

Mediante catálogos estructurados, un banco estandarizado de respuestas rápidas, un embudo de etiquetas comerciales y enlaces directos con códigos QR, los propietarios de mascotas en Huánuco pueden descubrir servicios médicos, experiencias de spa y productos de farmacia o pet shop directamente desde sus teléfonos móviles.

---

## 📱 II. Arquitectura de las Tres Cuentas Institucionales

| Canal Institucional | Número Telefónico | Responsable Operativo | Rol Comercial y Líneas Asignadas | Enlace de Prueba |
|---|---|---|---|---|
| **WhatsApp Recepción** | `+51 927 301 122` | **Diego** | Puerta de entrada, derivación, orientación, pedidos de **Farmacia Veterinaria** y **Pet Shop**. | [Abrir Chat](https://wa.me/51927301122?text=%C2%A1Hola%20Pelitos%20Veterinaria%21%20%F0%9F%90%BE%20Deseo%20informaci%C3%B3n%20general.) |
| **WhatsApp Consultorio** | `+51 939 356 376` | **Dra. Julia** | Servicios médicos, vacunación, laboratorio clínico, profilaxis, cirugías y citas recurrentes. | [Abrir Chat](https://wa.me/51939356376?text=%C2%A1Hola%20Consultorio%20Pelitos%21%20%F0%9F%A9%BA%20Deseo%20agendar%20una%20cita%20m%C3%A9dica.) |
| **WhatsApp Estética** | `+51 948 426 656` | **Antonella** | Catálogo de experiencias de spa, cotizaciones por tamaño/raza, deslanado y reservas por turnos. | [Abrir Chat](https://wa.me/51948426656?text=%C2%A1Hola%20Est%C3%A9tica%20Pelitos%21%20%E2%9C%82%EF%B8%8F%F0%9F%9B%81%20Deseo%20cotizar%20un%20servicio%20de%20ba%C3%B1o.) |

---

## 🗂️ III. Estructura de Entregables del Repositorio (10 Carpetas Obligatorias)

El proyecto está organizado conforme a lo establecido en la **Sección XV del Plan Técnico-Instructivo**:

```text
c:\Users\edicz\Documents\proyecto_pelitos\proyecto_wasap\
├── README.md                                       <-- Índice general y guía de navegación
├── index.html                                      <-- Portal Web Interactivo y Cockpit Comercial
│
├── tools/                                          <-- Scripts de automatización y generación
│   ├── generar_archivos_excel.py                   <-- Generador de libros XLSX con openpyxl
│   ├── exportar_catalogo_json.py                   <-- Exportador de catálogo a CSV y JSON
│   └── generar_enlaces_qr.py                       <-- Generador de enlaces wa.me y códigos QR
│
├── data/                                           <-- Fuentes de datos estructuradas
│   ├── catalogo_maestro.json                       <-- 23 artículos con precios, fotos y enlaces
│   ├── enlaces_whatsapp.json                       <-- Enlaces con texto URL-encoded
│   └── respuestas_rapidas.json                     <-- 11 atajos estandarizados
│
├── 01_auditoria_y_seguridad/                       <-- Módulo 1: Auditoría de Cuentas
│   ├── 01_Diagnostico_WhatsApp_Pelitos.xlsx        <-- Ficha oficial de diagnóstico en Excel
│   ├── diagnostico_inicial_cuentas.md              <-- Reporte técnico de brechas identificadas
│   ├── checklist_seguridad_dispositivos.md         <-- Control de sesiones y verificación en 2 pasos
│   └── politica_seguridad_datos_clientes.md        <-- Normativa interna de protección de datos
│
├── 02_matriz_maestra/                              <-- Módulo 2: Matriz Maestra y Fichas Modelo
│   ├── matriz_maestra_catalogos.xlsx               <-- Libro Excel oficial con 23 fichas
│   ├── matriz_maestra_catalogos.csv                <-- Tabla exportable CSV
│   ├── diccionario_datos_matriz.md                 <-- Especificación de campos y reglas de control
│   └── fichas_modelo_muestra_aprobacion.md         <-- 5 fichas modelo con identidad de marca
│
├── 03_catalogos_comerciales/                       <-- Fichas Técnicas por Línea Comercial
│   ├── consultorio_medico.md                       <-- 8 fichas médicas (Dra. Julia)
│   ├── estetica_canina_felina.md                   <-- 5 experiencias de grooming y spa (Antonella)
│   ├── farmacia_veterinaria.md                     <-- 5 productos de venta libre (Recepción)
│   └── pet_shop.md                                 <-- 5 alimentos y accesorios (Recepción)
│
├── 04_configuracion_whatsapp/                      <-- Módulo 3: Configuración de la Atención
│   ├── perfiles_institucionales.md                 <-- Textos de perfil, horarios y bienvenidas
│   ├── banco_respuestas_rapidas.md                 <-- 11 atajos (/horario, /cita, /estetica)
│   ├── sistema_etiquetas_comerciales.md            <-- Embudo de 10 etiquetas comerciales
│   └── guion_atencion_y_cierre_comercial.md        <-- Metodología de 5 pasos para cerrar citas
│
├── 05_integracion_digital/                         <-- Módulo 4: Enlaces Web y Códigos QR
│   ├── directorio_enlaces_wame.md                  <-- Directorio de enlaces wa.me
│   ├── widget_web_pelitos.html                     <-- Widget multicanal flotante para la web
│   ├── widget_web_pelitos.css                      <-- Estilos corporativos del widget
│   ├── widget_web_pelitos.js                       <-- Lógica interactiva y analítica de clics
│   └── protocolo_pruebas_moviles.md                <-- Matriz de validación en Android, iOS y PC
│
├── 06_indicadores/                                 <-- Módulo 5: Tablero y Métricas Comerciales
│   ├── tablero_control_kpis.xlsx                   <-- Libro Excel de control diario y KPIs
│   ├── metodologia_kpis_y_conversiones.md          <-- Fórmulas y metas de conversión comercial
│   └── plantilla_registro_diario.md                <-- Hoja de control diario para el counter
│
├── 07_manual_operativo/                            <-- Módulo 6: Manuales de Operación
│   ├── manual_administracion_whatsapp_business.md  <-- Manual paso a paso con capturas
│   └── guia_rapida_para_personal.md                <-- Guía de bolsillo plastificable
│
├── 08_capacitacion/                                <-- Módulo 7: Capacitación del Personal
│   ├── plan_capacitacion_personal.md               <-- Programa de 3 sesiones prácticas
│   ├── simulaciones_10_casos_prueba.md             <-- 10 situaciones reales de role-playing
│   └── rubrica_evaluacion_practica.md              <-- Rúbrica de evaluación sobre 20 puntos
│
├── 09_informes_y_seguimiento/                      <-- Módulo 8: Informes de Gestión
│   ├── acta_aprobacion_e_inicio.md                 <-- Acta formal firmada por Gerencia y EDICZON
│   ├── reporte_jornada_01_21oct2026.md             <-- Reporte oficial del Día 1
│   ├── plantilla_reporte_diario.md                 <-- Formato institucional de reporte diario
│   └── bitacora_cambios_e_incidencias.md           <-- Registro histórico de versiones y problemas
│
└── 10_proyeccion_api/                              <-- Módulo 9: Proyección Tecnológica Futura
    ├── informe_tecnico_whatsapp_api.md             <-- Comparativa Business App vs. Cloud API y costos
    └── hoja_ruta_escalabilidad_vetpraxis.md        <-- Arquitectura de integración con VetPraxis
```

---

## 🚀 IV. Cómo Ejecutar y Visualizar el Proyecto

### 1. Abrir el Portal Web Interactivo (Cockpit Comercial)
Para abrir el panel de control interactivo donde Gerencia y el equipo pueden explorar los catálogos, copiar respuestas y probar enlaces:
- Haz doble clic en el archivo [`index.html`](index.html) para abrirlo en cualquier navegador (Google Chrome, Microsoft Edge, Firefox).
- O ejecuta en PowerShell:
  ```powershell
  Start-Process index.html
  ```

### 2. Probar el Widget Web Flotante
Para verificar la experiencia que tendrán los usuarios en la web de Pelitos Veterinaria:
- Abre el archivo [`05_integracion_digital/widget_web_pelitos.html`](05_integracion_digital/widget_web_pelitos.html).

### 3. Regenerar los Libros de Excel Oficiales
Si se actualizan precios o datos en el futuro, los libros de Excel pueden reconstruirse automáticamente ejecutando:
```powershell
python tools/generar_archivos_excel.py
python tools/exportar_catalogo_json.py
python tools/generar_enlaces_qr.py
```

---

## 📊 V. Cronograma de Trabajo de 4 Semanas

| Periodo | Hito Principal | Entregables Clave | Estado |
|---|---|---|---|
| **Semana 1**<br>(21 – 27 oct) | **Auditoría, Planificación y Organización** | Diagnóstico de cuentas, Matriz Maestra y 5 fichas modelo | **Completado (Día 1)** |
| **Semana 2**<br>(28 oct – 3 nov) | **Construcción y Configuración de Catálogos** | 4 líneas comerciales cargadas en WhatsApp Business | *Programado* |
| **Semana 3**<br>(4 – 10 nov) | **Integración, Pruebas y Operación Comercial** | Enlaces wa.me, QR, widget web, etiquetas y piloto | *Programado* |
| **Semana 4**<br>(11 – 17 nov) | **Optimización, Capacitación y Cierre Final** | Manuales, capacitación del equipo, KPIs y entrega | *Programado* |

---

## 🤝 VI. Criterios de Aceptación de Gerencia General

Conforme a la Sección XVI del plan, el proyecto se considerará aprobado al cumplirse:
- [x] Las tres cuentas institucionales inventariadas y con propuesta de perfil formal.
- [x] Cuatro catálogos comerciales estructurados en 23 fichas con validación médica y de estética.
- [x] Banco de respuestas rápidas y sistema de 10 etiquetas comerciales listo para uso.
- [x] Directorio de enlaces directos, códigos QR y widget web probados.
- [x] Tablero de control de KPIs y registro diario de conversiones implementado en Excel.
- [x] Manual operativo, plan de capacitación y simulaciones de prueba documentadas.
- [x] Informe técnico de viabilidad y arquitectura para futura migración a WhatsApp Business API.
