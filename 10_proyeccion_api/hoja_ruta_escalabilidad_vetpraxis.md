# HOJA DE RUTA TÉCNICA: INTEGRACIÓN FUTURA CON VETPRAXIS Y SISTEMAS CLÍNICOS

**Proyecto N.° 03:** Pelitos Conecta Comercial 2026  
**Empresa:** Pelitos Veterinaria (Huánuco, Perú)  
**Autor:** EDICZON – Practicante de Ingeniería de Software  
**Supervisión:** Gerencia General  

---

## 1. Contexto y Limitación Técnica Actual

En la **Fase 1 (actual)**:
- No existe integración técnica automática entre WhatsApp Business y VetPraxis.
- El personal de recepción o consultorio atiende al cliente en WhatsApp, consulta la disponibilidad en VetPraxis manualmente y registra la cita en la agenda de la clínica.
- Esta separación manual es segura, de costo cero y evita errores de sincronización durante la fase de prueba.

---

## 2. Arquitectura de Integración Proyectada (Fase 2)

```
[ Cliente en WhatsApp ]
          │
          ▼  (Mensaje entrante)
[ Meta Cloud API / Webhook ]
          │
          ▼  (Evento POST en JSON)
[ Backend Integrador Pelitos (Python FastAPI / Node.js) ]
          │
     ┌────┴──────────────────────────────┐
     │                                   │
     ▼                                   ▼
[ Agente IA / Gemini ]          [ Base de Datos Intermedia ]
(Procesa intención del dueño)   (Caché de citas y pacientes)
     │                                   │
     └─────────────┬─────────────────────┘
                   │
                   ▼  (API REST / DB Sync)
         [ VetPraxis Cloud ]
         • Agenda Médica en Tiempo Real
         • Historias Clínicas
         • Facturación Electrónica SUNAT
```

---

## 3. Casos de Uso Automatizables con la API
1. **Recordatorio Automático de Citas:**  
   El sistema consulta VetPraxis a las 8:00 a. m. y envía automáticamente un mensaje por WhatsApp a los propietarios con cita agendada para el día siguiente:  
   *«Hola Carlos, te recordamos que mañana a las 10:00 a. m. Firulais tiene su vacuna séxtuple con la Dra. Julia. ¿Confirmas tu asistencia? (Responde SI o NO)»*.
2. **Alerta Preventiva de Refuerzo de Vacunas:**  
   30 días antes de vencer la vacuna de una mascota, VetPraxis dispara un webhook para recordarle al dueño con un botón de agendamiento directo.
3. **Envío Automatizado de Resultados de Laboratorio:**  
   Cuando el analizador hematológico carga los resultados en VetPraxis, el sistema genera un PDF protegido y lo envía automáticamente al WhatsApp del propietario con un saludo de la Dra. Julia.

---

## 4. Fases de Implementación Sugeridas

| Fase | Periodo Estimado | Alcance Técnico | Inversión Estimada |
|---|---|---|---|
| **Fase 1 (Actual)** | Oct - Nov 2026 | WhatsApp Business App, Catálogos, Enlaces, Manuales, Excel. | **S/ 0.00** |
| **Fase 2 (Piloto API)** | Q2 2027 | Meta Cloud API + Servidor intermedio Python en Google Cloud. | ~$20 - $40 USD / mes |
| **Fase 3 (Integración Full)** | Q4 2027 | Webhooks bidireccionales con VetPraxis y recordatorios automáticos. | Según licenciamiento API |
