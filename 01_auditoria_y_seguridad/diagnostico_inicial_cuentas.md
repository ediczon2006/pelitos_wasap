# PELITOS VETERINARIA — INFORME DE DIAGNÓSTICO INICIAL Y AUDITORÍA DE CUENTAS

**Proyecto N.° 03:** Pelitos Conecta Comercial 2026  
**Responsable Técnico:** EDICZON – Practicante de Ingeniería de Software  
**Supervisión:** Gerencia General  
**Fecha de Ejecución:** Miércoles 21 de octubre de 2026 (Semana 1)  
**Lema Institucional:** *«Expertos en cuidar a quien más te ama»*

---

## 1. Resumen de la Auditoría

Conforme a lo dispuesto en el Módulo 1 del plan técnico-instructivo, se procedió a realizar la auditoría diagnóstica de las tres (3) líneas y cuentas institucionales de WhatsApp Business que posee **Pelitos Veterinaria** en la ciudad de Huánuco.

El objetivo fue identificar el estado técnico-comercial inicial, inventariar los dispositivos vinculados, evaluar las brechas de seguridad y planificar las acciones de configuración antes de intervenir las cuentas.

---

## 2. Matriz de Estado Inicial por Cuenta Institucional

| Criterio Técnico / Comercial | WhatsApp Recepción<br>**(927 301 122 - Diego)** | WhatsApp Consultorio<br>**(939 356 376 - Dra. Julia)** | WhatsApp Estética<br>**(948 426 656 - Antonella)** |
|---|---|---|---|
| **Nombre Comercial** | "Pelitos Veterinaria Recepción" | "Consultorio Pelitos" | "Estética Pelitos" |
| **Foto de Perfil** | Logotipo anterior con baja resolución | Logotipo recortado | Foto informal no corporativa |
| **Descripción de Empresa** | Texto muy breve, sin llamado a la acción | Solo indica "Atención médica" | Sin descripción formal de spa |
| **Dirección y Ubicación GPS** | No vinculada a Google Maps | Solo texto ("Huánuco") | No configurada |
| **Horarios de Atención** | Desactivado en la app | No especifica domingos | Desactualizado |
| **Catálogo de Productos/Servicios** | **0 artículos** | **0 artículos** | 2 fotos sueltas sin precio ni detalle |
| **Mensaje de Bienvenida** | Texto predeterminado genérico | Desactivado | Desactivado |
| **Mensaje de Ausencia** | Desactivado | Desactivado | Desactivado |
| **Respuestas Rápidas** | 2 atajos informales | 0 atajos | 1 atajo básico (/ubicacion) |
| **Etiquetas Comerciales** | Etiquetas por defecto (sin usar) | 0 etiquetas | 0 etiquetas |
| **Enlaces Directos (wa.me) y QR** | Inexistentes | Inexistentes | Inexistentes |
| **Dispositivos Vinculados** | 1 sesión activa en PC recepción | 1 sesión en celular personal Dra. | 1 sesión en laptop |
| **Verificación en 2 Pasos (PIN)** | **Inactiva (Riesgo alto)** | **Inactiva (Riesgo alto)** | **Inactiva (Riesgo alto)** |

---

## 3. Diagnóstico por Canal

### 3.1. Canal Recepción (927 301 122 — Responsable: Diego)
- **Estado Actual:** Opera como el número más saturado de la clínica, respondiendo preguntas repetitivas sobre precios, vacunas, servicios de spa y disponibilidad de productos.
- **Cuellos de Botella:** Al no existir catálogo ni respuestas rápidas, el tiempo de respuesta varía entre 15 y 45 minutos. Los clientes interesados en medicina o spa se quedan esperando derivaciones manuales.
- **Acción Inmediata:** Configurar el catálogo de Farmacia y Pet Shop en esta cuenta, activar respuestas rápidas esenciales (`/horario`, `/ubicacion`, `/farmacia`, `/petshop`) y capacitar a Diego en derivación con un solo clic.

### 3.2. Canal Consultorio (939 356 376 — Responsable: Dra. Julia)
- **Estado Actual:** Recibe mensajes mixtos entre consultas médicas urgentes, dueños pidiendo diagnósticos por chat y recordatorios de vacunas.
- **Riesgos Clínicos:** No existe advertencia sanitaria de que por WhatsApp no se prescriben antibióticos ni se realizan diagnósticos clínicos definitivos sin previa evaluación física.
- **Acción Inmediata:** Cargar el catálogo médico (8 fichas: consulta general, control, vacunas canina/felina, desparasitación, hemograma, esterilización y profilaxis dental). Añadir cláusula sanitaria institucional en la descripción.

### 3.3. Canal Estética Canina y Felina (948 426 656 — Responsable: Antonella)
- **Estado Actual:** Gran interés de clientes, pero las cotizaciones son lentas porque las tarifas varían por raza, peso y estado del pelaje (nudos/deslanado).
- **Cuellos de Botella:** El cliente pregunta "¿cuánto cuesta bañar a mi perro?" y el personal responde con preguntas dispersas.
- **Acción Inmediata:** Cargar las 4 experiencias aprobadas (*Ducha Express*, *Clásico Funcional*, *Spa Relajante*, *Momento Real*) y el servicio complementario de *Deslanado*. Implementar la respuesta rápida `/estetica_cotizar` para pedir datos estandarizados.

---

## 4. Brechas de Seguridad Identificadas y Medidas Correctivas

1. **Ausencia de Verificación en Dos Pasos (2FA):**
   - *Riesgo:* Posible secuestro de cuenta o clonación de SIM.
   - *Medida:* Coordinar con Gerencia para ingresar un PIN de 6 dígitos institucional custodiado por Gerencia General.
2. **Dispositivos Vinculados sin Bitácora:**
   - *Riesgo:* Acceso a conversaciones de clientes desde computadoras o laptops no autorizadas.
   - *Medida:* Cerrar de inmediato todas las sesiones de WhatsApp Web no identificadas y registrar en bitácora solo las computadoras de recepción y consultorio.
3. **Privacidad de Contactos:**
   - *Riesgo:* Mezcla de contactos personales con los de clientes de Pelitos.
   - *Medida:* Establecer como política que ningún contacto institucional se guarde en cuentas personales de Google o iCloud del personal.

---

## 5. Entregables Generados

- Archivo Excel oficial: `01_auditoria_y_seguridad/01_Diagnostico_WhatsApp_Pelitos.xlsx`
- Checklist de Dispositivos: `01_auditoria_y_seguridad/checklist_seguridad_dispositivos.md`
- Política de Datos: `01_auditoria_y_seguridad/politica_seguridad_datos_clientes.md`
