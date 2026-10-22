# METODOLOGÍA DE INDICADORES DE GESTIÓN Y TABLERO COMERCIAL

**Proyecto N.° 03:** Pelitos Conecta Comercial 2026  
**Empresa:** Pelitos Veterinaria (Huánuco, Perú)  
**Entregable:** 06 – Indicadores  
**Responsable:** EDICZON (Practicante)  
**Supervisión:** Gerencia General  

---

## 1. Justificación de Medición

WhatsApp Business no debe operar como una caja negra de mensajes informales. Para evaluar la efectividad comercial del proyecto Pelitos Conecta Comercial 2026, se definen dos categorías de métricas:
1. **Indicadores de Implementación Técnica:** Evalúan el despliegue del sistema (cronograma y configuración).
2. **Indicadores de Desempeño Comercial (KPIs):** Evalúan el impacto real en citas, ventas y facturación.

---

## 2. Definición Técnica de KPIs Comerciales

### 1. Tasa de Conversión a Reserva de Cita (%)
- **Definición:** Porcentaje de conversaciones en las que un cliente que solicitó información médica o estética terminó agendando una cita formal.
- **Fórmula:**
  $$\text{Tasa de Reserva} = \left(\frac{\text{Citas Agendadas y Confirmadas}}{\text{Total Consultas Elegibles recibidas}}\right) \times 100$$
- **Meta Mes 1:** $\ge 45\%$

### 2. Tasa de Conversión a Venta en Farmacia / Pet Shop (%)
- **Definición:** Porcentaje de consultas por productos que culminaron en un pedido pagado o retirado.
- **Fórmula:**
  $$\text{Tasa de Venta} = \left(\frac{\text{Pedidos Concretados}}{\text{Total Consultas de Productos}}\right) \times 100$$
- **Meta Mes 1:** $\ge 30\%$

### 3. Ingresos Totales Originados por WhatsApp (S/)
- **Definición:** Suma monetaria en Soles de las ventas y servicios cobrados cuyo primer contacto o confirmación se dio a través de cualquiera de los 3 números de WhatsApp.
- **Regla de Conciliación:** Debe cotejarse diariamente contra el módulo de facturación de **VetPraxis** o el cuaderno de caja diario de Recepción, evitando duplicidad contable.
- **Meta Mes 1:** Línea base inicial proyectada en S/ 8,000.00 / mes atribuido al ecosistema WhatsApp.

### 4. Ticket Promedio por WhatsApp (S/)
- **Definición:** Valor promedio de consumo por cada operación cerrada por WhatsApp.
- **Fórmula:**
  $$\text{Ticket Promedio} = \frac{\text{Ingresos Totales por WhatsApp (S/)}}{\text{Total Operaciones Concretadas}}$$
- **Meta Mes 1:** $\ge \text{S/ } 55.00$

### 5. Tiempo Promedio de Primera Respuesta (FRT)
- **Definición:** Tiempo transcurrido (en minutos) desde que el cliente envía un mensaje nuevo hasta que un personal humano le responde.
- **Meta Mes 1:** $\le 8\text{ minutos}$ en horario de atención.

### 6. Tasa de Inasistencia a Citas (No-Show Rate) (%)
- **Definición:** Porcentaje de clientes que reservaron pero no acudieron ni reprogramaron.
- **Fórmula:**
  $$\text{No-Show} = \left(\frac{\text{Citas No Asistidas}}{\text{Total Citas Programadas}}\right) \times 100$$
- **Meta Mes 1:** $< 10\%$ (Se mitiga activando el mensaje recordatorio `/confirmar_cita`).

---

## 3. Rutina de Control y Registro Diario
1. A las 7:30 p. m. (cierre de atención), Diego (Recepción), Dra. Julia (Consultorio) y Antonella (Estética) anotan en el cuaderno o planilla digital:
   - Número de chats nuevos del día.
   - Cantidad de citas agendadas.
   - Cantidad de pedidos de productos cerrados.
2. EDICZON consolida los datos en `06_indicadores/tablero_control_kpis.xlsx` y genera el gráfico semanal para Gerencia.
