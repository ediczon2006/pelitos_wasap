# SIMULACIÓN PRÁCTICA: 10 CASOS DE PRUEBA REALES

**Proyecto N.° 03:** Pelitos Conecta Comercial 2026  
**Empresa:** Pelitos Veterinaria (Huánuco, Perú)  
**Evaluador:** EDICZON (Practicante) / Gerencia General  
**Objetivo:** Poner a prueba la capacidad de respuesta, fluidez, uso de herramientas comerciales y empatía del personal ante situaciones cotidianas de atención al cliente.

---

## Banco de los 10 Casos de Prueba

### Caso 1: Solicitud de Vacunas para Cachorro (Canal Consultorio - Dra. Julia)
- **Simulación del Cliente:** *"Hola, acabo de adoptar un cachorrito mestizo de 2 meses y no sé qué vacunas le tocan ni cuánto cuesta."*
- **Criterio de Éxito:**
  1. Dra. Julia o asistente responde antes de 5 minutos con calidez.
  2. Utiliza la respuesta `/vacunas` o comparte la ficha `MED-003 Plan de Vacunación`.
  3. Menciona el beneficio de la evaluación física previa sin costo adicional.
  4. Ofrece opciones de días para agendar cita y aplica la etiqueta `4. Cita por confirmar`.

---

### Caso 2: Cotización de Baño para Husky con Muda de Pelo (Canal Estética - Antonella)
- **Simulación del Cliente:** *"Buenas tardes, tengo un Husky siberiano de 25 kg y está botando muchísimo pelo en mi casa. ¿Hacen deslanado y cuánto me saldría todo?"*
- **Criterio de Éxito:**
  1. Antonella saluda amablemente e identifica el servicio especializado.
  2. Comparte la ficha de `EST-002 Clásico Funcional` + `EST-005 Deslanado Profesional`.
  3. Explica con claridad la tarifa base y el adicional técnico por deslanado de doble capa.
  4. Plantea turnos disponibles para el fin de semana y asigna la etiqueta `3. Cotización pendiente`.

---

### Caso 3: Consulta de Pastilla Antiparasitaria (Canal Recepción - Diego)
- **Simulación del Cliente:** *"Hola, necesito la pastilla NexGard para mi perro que tiene pulgas, pero no sé de qué peso pedir."*
- **Criterio de Éxito:**
  1. Diego pregunta amablemente el peso aproximado de la mascota.
  2. Al indicar que pesa 12 kg, comparte la ficha `FAR-001 NexGard Spectra (7.5 - 15 kg)` con su precio de S/ 62.00.
  3. Pregunta si desea recoger en clínica o despacho por delivery.
  4. Aplica la etiqueta `6. Pedido pendiente`.

---

### Caso 4: Cliente con Mascota con Vómito Severo (Canal Recepción / Consultorio)
- **Simulación del Cliente:** *"Auxilio, mi perrito lleva 4 horas vomitando espuma blanca y está decaído. ¿Qué le puedo dar o qué pastilla le compro?"*
- **Criterio de Éxito:**
  1. El personal detecta riesgo clínico inmediato y **NO prescribe medicamentos por chat**.
  2. Emplea la respuesta rápida `/urgencia`.
  3. Indica acudir inmediatamente a la clínica en Jr. Dos de Mayo N.° 1234 y brinda el teléfono de alerta directa.

---

### Caso 5: Cotización de Corte Shih Tzu con Nudos (Canal Estética - Antonella)
- **Simulación del Cliente:** *"Hola, quiero que le corten el pelo a mi perrita Shih Tzu como de peluche, pero tiene unos nuditos atrás de las orejas."*
- **Criterio de Éxito:**
  1. Antonella solicita una foto de la mascota para evaluar el nivel de nudos.
  2. Comparte la ficha `EST-004 Experiencia Momento Real`.
  3. Explica amablemente que se intentará desenredar con mascarilla de argán sin maltratarla y advierte si se requiere corte higiénico.
  4. Agenda turno matutino y coloca `5. Cita confirmada`.

---

### Caso 6: Solicitud de Alimento Hill's con Delivery (Canal Recepción - Diego)
- **Simulación del Cliente:** *"Hola, ¿tienen comida Hill's para perro chiquito adulto y hacen delivery a Amarilis?"*
- **Criterio de Éxito:**
  1. Diego confirma stock y envía la ficha `PET-001 Hill's Small Paws 2.04 kg` (S/ 95.00).
  2. Informa el costo y tiempo de delivery local.
  3. Solicita dirección exacta, nombre de quien recibe y método de pago (Yape/Plin/Efectivo/POS).
  4. Marca como `6. Pedido pendiente` y posteriormente `7. Venta concretada`.

---

### Caso 7: Mensaje Fuera de Horario (Domingo por la noche)
- **Simulación del Cliente:** Mensaje enviado a las 10:30 p. m. solicitando información de profilaxis dental.
- **Criterio de Éxito:**
  1. Se activa automáticamente el mensaje de ausencia configurado.
  2. El lunes a las 8:30 a. m., el personal inicia el seguimiento saludando cordialmente y compartiendo la ficha `MED-008 Profilaxis Dental`.

---

### Caso 8: Cliente que Desea Reprogramar su Cita de Consulta
- **Simulación del Cliente:** *"Disculpe Dra., tenía cita para hoy a las 4:00 p. m. pero se me presentó un inconveniente de trabajo y no llegaré."*
- **Criterio de Éxito:**
  1. Responde empáticamente usando `/reprogramar`.
  2. Ofrece dos opciones de horario alternativo en las próximas 48 horas.
  3. Actualiza el agendamiento en VetPraxis y mantiene la etiqueta `5. Cita confirmada` con la nueva fecha.

---

### Caso 9: Derivación de Cirugía desde Recepción a Consultorio
- **Simulación del Cliente:** El cliente escribe a Recepción (`927 301 122`): *"Hola, quiero esterilizar a mi gatita de 7 meses, ¿cuánto cuesta?"*
- **Criterio de Éxito:**
  1. Diego orienta con amabilidad y deriva con el enlace directo de Consultorio `https://wa.me/51939356376`.
  2. La Dra. Julia recibe al cliente, comparte la ficha `MED-007 Esterilización` y explica los requisitos prequirúrgicos de ayuno y análisis.

---

### Caso 10: Seguimiento Pos-Atención de Spa (Canal Estética)
- **Simulación:** Mascota atendida el día anterior en sesión de Spa Relajante.
- **Criterio de Éxito:**
  1. Antonella activa el mensaje `/seguimiento` a las 11:00 a. m. del día posterior.
  2. Pregunta cómo se encuentra el paciente y si disfrutó de su experiencia.
  3. Al recibir respuesta positiva del cliente, asigna la etiqueta `9. Cliente recurrente`.
