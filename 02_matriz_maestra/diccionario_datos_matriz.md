# DICCIONARIO DE DATOS Y ESPECIFICACIÓN DE LA MATRIZ MAESTRA DE CATÁLOGOS

**Proyecto N.° 03:** Pelitos Conecta Comercial 2026  
**Entregable:** 02 – Matriz Maestra  
**Responsable:** EDICZON (Practicante)  
**Supervisión:** Gerencia General  

---

## 1. Propósito de la Matriz Maestra

La **Matriz Maestra de Catálogos Pelitos 2026** es la única fuente de verdad (*Single Source of Truth*) para la gestión de productos y servicios que se publican en las tres cuentas institucionales de WhatsApp Business de Pelitos Veterinaria.

Ninguna ficha puede ser redactada o publicada directamente en WhatsApp sin estar previamente inventariada, validada y aprobada en esta matriz.

---

## 2. Estructura de Campos Obligatorios

| Campo | Tipo de Dato | Longitud / Formato | Obligatorio | Descripción y Reglas de Negocio |
|---|---|---|---|---|
| **Código** | Alfanumérico | 7 caracteres (`AAA-000`) | Sí | Identificador único del servicio o producto. Prefijos: `MED-` (Consultorio), `EST-` (Estética), `FAR-` (Farmacia), `PET-` (Pet Shop). |
| **Área** | Texto | Selección cerrada | Sí | Valores permitidos: `Consultorio`, `Estética`, `Farmacia`, `Pet Shop`. |
| **Categoría** | Texto | Hasta 40 caracteres | Sí | Subclasificación comercial (ej.: *Medicina Preventiva*, *Experiencias Spa*, *Antiparasitarios Externos*, *Alimentación Premium*). |
| **Nombre Comercial** | Texto | Hasta 60 caracteres | Sí | Nombre oficial y atractivo con el que se exhibe en WhatsApp Business. No debe superar los 60 caracteres para evitar truncamientos en la vista móvil. |
| **Descripción** | Texto largo | Hasta 300 caracteres | Sí | Redacción persuasiva y clara para el propietario. Debe explicar el beneficio real, los componentes incluidos y la indicación médica/estética. Prohibido garantizar curaciones médicas. |
| **Precio (S/)** | Numérico | Decimal `S/ 00.00` | Sí | Valor monetario en Soles peruanos según tarifario vigente aprobado por Gerencia. |
| **Condición Precio** | Texto | Selección cerrada | Sí | `Precio fijo`, `Desde (según peso)`, `Desde (según raza)`, `Precio caja/empaque`, `Previa evaluación`. |
| **Fotografía / Arte** | Texto | `codigo_nombre.jpg` | Sí | Nombre del archivo fotográfico institucional aprobado (proporción 1:1, resolución recomendada 1080x1080 px). |
| **Cuenta WhatsApp** | Texto | Selección cerrada | Sí | Cuenta en la que se publica: `Consultorio (939 356 376)`, `Estética (948 426 656)`, `Recepción (927 301 122)`. |
| **Disponibilidad** | Texto | Selección | Sí | `Vigente`, `Agotado temporalmente`, `Suspendido`, `Bajo pedido`. |
| **Fuente Tarifario** | Texto | Texto descriptivo | Sí | Documento interno de referencia (ej. *Tarifario Quirúrgico 2026*, *Inventario Farmacia Octubre 2026*). |
| **Estado Ficha** | Texto | Flujo de aprobación | Sí | `Borrador`, `Pendiente de revisión`, `Aprobado por Gerencia`, `Publicado en WhatsApp`. |
| **Responsable Validación** | Texto | Nombre y cargo | Sí | Persona que da fe de la exactitud técnica: Dra. Julia (Médico), Antonella (Estética), Administración o Gerencia General. |
| **Versión** | Numérico | Formato `X.Y` | Sí | Versión del contenido (ej.: `1.0`, `1.1` al actualizar precio). |

---

## 3. Flujo de Control y Aprobación de Fichas

```
[EDICZON: Redacta Borrador] 
         │
         ▼
[Validación Técnica del Área]
(Dra. Julia / Antonella / Admin)
         │
         ▼
[Aprobación Formal de Gerencia General]
         │
         ├────► NO APROBADO: Retorna a corrección (con observaciones)
         │
         ▼ APROBADO
[Carga y Publicación en WhatsApp Business]
         │
         ▼
[Verificación Visual en Dispositivo Móvil Test]
         │
         ▼
[Estado: PUBLICADO Y CONFORME]
```

---

## 4. Archivos Generados
- Libro Excel principal: `02_matriz_maestra/matriz_maestra_catalogos.xlsx`
- Tabla CSV de exportación: `02_matriz_maestra/matriz_maestra_catalogos.csv`
- Objeto JSON estructurado: `data/catalogo_maestro.json`
