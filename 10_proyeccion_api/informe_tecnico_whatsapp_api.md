# INFORME TÉCNICO COMPARATIVO: MIGRACIÓN A WHATSAPP BUSINESS PLATFORM (API)

**Proyecto N.° 03:** Pelitos Conecta Comercial 2026  
**Empresa:** Pelitos Veterinaria (Huánuco, Perú)  
**Autor:** EDICZON – Practicante de Ingeniería de Software  
**Supervisión:** Gerencia General  
**Fecha:** Octubre 2026  
**Estado:** Proyección y Estudio de Factibilidad (Fase 2 Futura — Sin costo inicial)  

---

## 1. Resumen Ejecutivo

La fase actual del proyecto resuelve la organización comercial mediante **WhatsApp Business Gratuito (App)**, sin incurrir en costos mensuales de suscripción.

Sin embargo, a medida que el volumen de consultas de Pelitos Veterinaria supere las 50 a 100 conversaciones diarias por canal, surgirán limitaciones intrínsecas de la aplicación gratuita:
1. Limitación a un solo teléfono físico con un máximo de 4 dispositivos web vinculados.
2. Imposibilidad de tener una bandeja compartida (*Shared Inbox*) donde múltiples recepcionistas o médicos atiendan el mismo número simultáneamente con roles y métricas individuales.
3. Imposibilidad de conectar bots de auto-agendamiento sincronizados en tiempo real con la base de datos de **VetPraxis**.
4. Riesgo de bloqueo si se envían recordatorios masivos sin la certificación de Meta.

El presente informe analiza los requisitos técnicos, alternativas de proveedores BSP, costos estimados y beneficios de una eventual migración a **WhatsApp Business Platform (Cloud API)**.

---

## 2. Cuadro Comparativo: WhatsApp Business App vs. WhatsApp Business API

| Característica / Función | WhatsApp Business App (Fase Actual 2026) | WhatsApp Business Platform / API (Fase 2 Proyectada) |
|---|---|---|
| **Costo de Licencia** | **S/ 0.00 (Gratuito)** | Costo por conversación (Meta) + Plataforma multiagente ($25 - $70 USD/mes). |
| **Número de Agentes Simultáneos** | 1 smartphone físico + hasta 4 sesiones web. | **Ilimitado** (multiagente con bandeja unificada). |
| **Bandeja de Entrada Compartida** | No (los operadores se pisan los mensajes). | **Sí**, con asignación automática de chats a Diego, Julia o Antonella. |
| **Automatización / Chatbots** | Solo bienvenida, ausencia y atajos manuales. | **Chatbots con IA** (Gemini / Dialogflow) capaces de agendar citas en base de datos. |
| **Integración con VetPraxis** | Manual (el personal digita en el software). | **Automática vía Webhooks / API REST** (recordatorios automáticos de vacunas). |
| **Envío Masivo de Recordatorios** | Prohibido / Riesgo alto de baneo. | **Permitido y oficial** mediante plantillas aprobadas por Meta (*HSM Templates*). |
| **Métricas y Productividad** | Conteo manual en Excel. | **Dashboard en tiempo real**: tiempo de espera, calificación CSAT, volumen por hora. |

---

## 3. Modelo de Costos de Meta para WhatsApp Business API

Meta factura las conversaciones en bloques de 24 horas clasificadas en 4 categorías:
1. **Conversaciones de Servicio (Iniciadas por el usuario):** Las primeras 1,000 conversaciones al mes son **gratuitas**. A partir de la 1,001, tienen un costo de aprox. $0.015 USD (~S/ 0.06).
2. **Conversaciones de Utilidad (Recordatorios de cita, recetas):** Aprox. $0.020 USD (~S/ 0.08).
3. **Conversaciones de Autenticación (Envío de códigos OTP):** Aprox. $0.018 USD (~S/ 0.07).
4. **Conversaciones de Marketing (Promociones, campañas de spa):** Aprox. $0.045 USD (~S/ 0.17).

---

## 4. Proveedores de Solución Oficiales (BSPs Recomendados)

Para implementar la API sin necesidad de programar servidores desde cero, se evaluaron tres plataformas compatibles con el mercado peruano:

1. **WATI (WhatsApp Team Inbox):**
   - *Costo:* ~$49 USD / mes (incluye 5 agentes).
   - *Ventajas:* Interfaz muy amigable para clínicas, creador de chatbots sin código (*No-Code Flow Builder*), integración con Webhooks y Google Sheets.
2. **Kommo (ex-AmoCRM):**
   - *Costo:* ~$15 USD / usuario / mes.
   - *Ventajas:* Excelente CRM visual de ventas por WhatsApp, embudo de etapas automatizado, pipeline comercial.
3. **Meta Cloud API Directa (Desarrollo a Medida con Antigravity / Python / Node.js):**
   - *Costo:* $0 en software mensual (solo consumo de Meta).
   - *Ventajas:* Control total del código, base de datos propia, sin comisiones de terceros. Requiere servidor cloud (Google Cloud / AWS).

---

## 5. Recomendación para Gerencia General
- **Etapa Actual (Noviembre 2026):** Mantener y perfeccionar **WhatsApp Business Gratuito**. El proyecto Pelitos Conecta Comercial 2026 ya provee catálogos organizados, respuestas rápidas, etiquetas y enlaces sin gastar un solo sol.
- **Criterio de Disparo para Fase 2:** Evaluar la contratación de WhatsApp Business API únicamente cuando:
  - El volumen supere las 1,500 consultas mensuales.
  - La clínica incorpore un segundo o tercer recepcionista en paralelo.
  - VetPraxis habilite una API pública oficial para sincronización bidireccional de historias clínicas y citas.
