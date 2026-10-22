@echo off
title Servidor Local Pelitos Veterinaria - Enlaces WhatsApp
cd /d "%~dp0\.."
echo =====================================================================
echo    PELITOS VETERINARIA -- SERVIDOR ACTIVO PARA PRUEBAS POR CELULAR
echo =====================================================================
echo.
echo Tu servidor esta activo en la red Wi-Fi local.
echo Puedes abrir estos enlaces desde tu celular conectado a la misma red:
echo.
echo   * PORTAL GENERAL MULTICANAL:
echo     http://192.168.1.84:8000/proyecto_wasap/index.html
echo.
echo   * CATALOGO PET SHOP (DIEGO):
echo     http://192.168.1.84:8000/proyecto_wasap/catalogo_recepcion.html
echo.
echo   * CATALOGO MEDICO (DRA. JULIA):
echo     http://192.168.1.84:8000/proyecto_wasap/catalogo_consultorio.html
echo.
echo   * CATALOGO ESTETICA (ANTONELLA):
echo     http://192.168.1.84:8000/proyecto_wasap/catalogo_estetica.html
echo.
echo   * WEB OFICIAL PELITOS:
echo     http://192.168.1.84:8000/pelitos_veterinaria/index.html
echo.
echo (Para detener el servidor presiona Ctrl + C o cierra esta ventana)
echo =====================================================================
echo.
python -m http.server 8000 --bind 0.0.0.0
pause
