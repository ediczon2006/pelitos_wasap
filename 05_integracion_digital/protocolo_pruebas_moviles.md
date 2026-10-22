# PROTOCOLO DE PRUEBAS DE ENLACES WA.ME Y CÓDIGOS QR

**Proyecto N.° 03:** Pelitos Conecta Comercial 2026  
**Responsable Técnico:** EDICZON (Practicante)  
**Supervisión:** Gerencia General  
**Fecha:** Semana 3 de Ejecución  

---

## 1. Alcance de las Pruebas

Para garantizar que ningún cliente de Pelitos experimente enlaces rotos, números erróneos o mensajes mal codificados, se establece la ejecución obligatoria de pruebas en 3 entornos:
1. **Dispositivos Android:** (Chrome, Samsung Internet, App WhatsApp oficial).
2. **Dispositivos iOS (iPhone):** (Safari, App WhatsApp oficial).
3. **Computadoras de Escritorio (Desktop):** (Chrome, Edge, WhatsApp Web y Desktop app).

---

## 2. Matriz de Validación de Enlaces y Códigos QR

| ID Prueba | Canal Probado | Destino Telefónico | Mensaje Precargado Verificado | Apertura en Android | Apertura en iOS | Apertura en PC (Web) | Estado |
|---|---|---|---|---|---|---|---|
| **TEST-01** | Recepción | `+51 927 301 122` | Información general | Conforme | Conforme | Conforme | **Aprobado** |
| **TEST-02** | Recepción | `+51 927 301 122` | Farmacia veterinaria | Conforme | Conforme | Conforme | **Aprobado** |
| **TEST-03** | Recepción | `+51 927 301 122` | Pet Shop y alimentos | Conforme | Conforme | Conforme | **Aprobado** |
| **TEST-04** | Consultorio | `+51 939 356 376` | Agendar cita médica | Conforme | Conforme | Conforme | **Aprobado** |
| **TEST-05** | Consultorio | `+51 939 356 376` | Vacunación preventiva | Conforme | Conforme | Conforme | **Aprobado** |
| **TEST-06** | Consultorio | `+51 939 356 376` | Cirugía / Esterilización | Conforme | Conforme | Conforme | **Aprobado** |
| **TEST-07** | Estética | `+51 948 426 656` | Cotización de baño/spa | Conforme | Conforme | Conforme | **Aprobado** |
| **TEST-08** | Estética | `+51 948 426 656` | Spa Pelitos Relajante | Conforme | Conforme | Conforme | **Aprobado** |
| **TEST-09** | Estética | `+51 948 426 656` | Corte Momento Real | Conforme | Conforme | Conforme | **Aprobado** |
| **TEST-10** | Widget Web | Multicanal (3 opciones) | Clic en los 3 canales | Conforme | Conforme | Conforme | **Aprobado** |

---

## 3. Criterios de Aceptación Técnica
- **100% de enlaces directos:** Al presionar el enlace o escanear el QR, se debe abrir la conversación con el número institucional correcto y el mensaje precargado en la caja de texto.
- **Sin caracteres extraños:** Los acentos, signos de puntuación y emojis (`🐾`, `🩺`, `✂️`, `💊`, `🛍️`) deben renderizarse correctamente sin mostrar símbolos rotos (`%20`, `&amp;`, `?`).
- **Tiempo de carga:** La redirección debe tardar menos de 2 segundos en conexiones móviles 4G.
