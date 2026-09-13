@echo off
title GCC OpenClaw eBook
echo ==================================================
echo Iniciando Plataforma GCC OpenClaw eBook
echo ==================================================
echo Abriendo servidor local en http://localhost:8080...
start http://localhost:8080
python -m http.server 8080
pause
