/**
 * Widget Multicanal Pelitos Conecta 2026
 * Manejo de eventos de apertura, cierre y analítica de clics por canal
 */
document.addEventListener('DOMContentLoaded', () => {
  const launcher = document.getElementById('pelitosWaLauncher');
  const windowEl = document.getElementById('pelitosWaWindow');
  const closeBtn = document.getElementById('pelitosWaClose');
  const channelCards = document.querySelectorAll('.pelitos-channel-card');

  if (!launcher || !windowEl || !closeBtn) return;

  // Toggle ventana
  launcher.addEventListener('click', () => {
    const isActive = windowEl.classList.contains('active');
    if (isActive) {
      windowEl.classList.remove('active');
      windowEl.setAttribute('aria-hidden', 'true');
    } else {
      windowEl.classList.add('active');
      windowEl.setAttribute('aria-hidden', 'false');
    }
  });

  // Cerrar ventana
  closeBtn.addEventListener('click', (e) => {
    e.stopPropagation();
    windowEl.classList.remove('active');
    windowEl.setAttribute('aria-hidden', 'true');
  });

  // Registro de clics para analítica comercial (Google Analytics / Pixel)
  channelCards.forEach((card) => {
    card.addEventListener('click', function () {
      const channelTitle = this.querySelector('.channel-name')?.textContent || 'Canal Desconocido';
      console.log(`[Pelitos Analytics] Clic en WhatsApp: ${channelTitle}`);
      
      // Si existe Google Analytics en la web institucional:
      if (typeof gtag === 'function') {
        gtag('event', 'click_whatsapp_channel', {
          event_category: 'Conversión WhatsApp',
          event_label: channelTitle
        });
      }
    });
  });

  // Cerrar al hacer clic fuera del widget en pantallas grandes
  document.addEventListener('click', (e) => {
    const container = document.getElementById('pelitosWaContainer');
    if (container && !container.contains(e.target)) {
      windowEl.classList.remove('active');
      windowEl.setAttribute('aria-hidden', 'true');
    }
  });
});
