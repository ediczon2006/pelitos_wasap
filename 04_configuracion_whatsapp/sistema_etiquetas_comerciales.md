# SISTEMA DE ETIQUETAS COMERCIALES (EMBUDO DE CONVERSIÓN)

**Proyecto N.° 03:** Pelitos Conecta Comercial 2026  
**Empresa:** Pelitos Veterinaria (Huánuco, Perú)  
**Objetivo:** Organizar visualmente el flujo de clientes desde el primer mensaje hasta el cierre y seguimiento, evitando conversaciones abandonadas o pedidos extraviados.

---

## 1. Arquitectura de las 10 Etiquetas Comerciales Oficiales

WhatsApp Business permite asignar colores y nombres a etiquetas para agrupar chats. En Pelitos se establece un estándar único para los 3 canales:

| N.° | Nombre de la Etiqueta | Color Sugerido | Significado / Fase del Embudo | Acción Operativa Obligatoria |
|---|---|---|---|---|
| **01** | `1. Cliente nuevo` | 🟡 Amarillo | Primer contacto de una persona que nunca se ha atendido en Pelitos. | Enviar bienvenida, solicitar nombre del dueño y mascota. |
| **02** | `2. Solicita información` | 🔵 Azul claro | El cliente consulta por un servicio, vacuna o producto en catálogo. | Compartir ficha técnica del catálogo y explicar beneficios. |
| **03** | `3. Cotización pendiente` | 🟠 Naranja | Requiere enviar un presupuesto (ej. baño según peso, cirugía o examen). | Enviar precio antes de 15 minutos e invitar a agendar. |
| **04** | `4. Cita por confirmar` | 🟣 Morado | Se ofreció un horario o fecha y se espera el "sí" del cliente. | Si no responde en 3 horas, enviar recordatorio amable. |
| **05** | `5. Cita confirmada` | 🟢 Verde claro | Turno pactado y agendado formalmente. | Registrar en VetPraxis / enviar mensaje `/confirmar_cita`. |
| **06** | `6. Pedido pendiente` | 🟤 Marrón | Cliente solicitó producto de Farmacia o Pet Shop (recojo o envío). | Verificar stock en almacén y enviar datos de pago. |
| **07** | `7. Venta concretada` | 🟢 Verde oscuro | Pago realizado, cita atendida o producto entregado. | Registrar monto en hoja comercial / solicitar comprobante. |
| **08** | `8. Seguimiento` | 🔴 Rosa / Magenta | Paciente atendido ayer que requiere control o evaluación posterior. | Enviar mensaje `/seguimiento` a las 24 o 48 horas. |
| **09** | `9. Cliente recurrente` | 🌟 Dorado / Amarillo intenso | Cliente fiel con más de 3 visitas registradas. | Brindar trato preferente y beneficios del Club Pelitos. |
| **10** | `10. Atención cerrada` | ⚪ Gris | Conversación finalizada que no requiere acción adicional por ahora. | Retirar etiquetas activas y archivar si corresponde. |

---

## 2. Flujo Operativo de Conversión

```
[1. Cliente nuevo] ──► [2. Solicita información] ──► [3. Cotización pendiente]
                                                             │
                                                             ▼
                                                   [4. Cita por confirmar]
                                                             │
                                                             ▼
                                                   [5. Cita confirmada]
                                                             │
                                                             ▼ (Atención realizada)
                                                   [7. Venta concretada]
                                                             │
                                                             ▼ (24 hrs después)
                                                   [8. Seguimiento]
                                                             │
                                                             ▼
                                              [9. Cliente recurrente / 10. Cerrada]
```

---

## 3. Reglas de Disciplina Operativa
1. **Regla de Etiqueta Única Principal:** Un chat no debe tener más de una etiqueta de estado de avance activo para evitar confusión en el embudo (por ejemplo, al pasar de *Cotización pendiente* a *Cita confirmada*, se retira la anterior).
2. **Revisión Diaria al Cierre de Turno:**
   - Diego (Recepción), Dra. Julia (Consultorio) y Antonella (Estética) deben filtrar los chats por la etiqueta `3. Cotización pendiente` y `4. Cita por confirmar` antes de retirarse, asegurando que no quede ningún cliente sin respuesta.
