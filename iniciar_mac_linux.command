#!/bin/bash
# Script de inicio rápido para Mac / Linux
cd "$(dirname "$0")"
echo "=================================================="
echo "⚡ Iniciando Plataforma GCC OpenClaw eBook"
echo "=================================================="
echo "Abriendo servidor local en http://localhost:8080..."
python3 -m http.server 8080 &
SERVER_PID=$!
sleep 1
open "http://localhost:8080" || xdg-open "http://localhost:8080"
echo "Presiona Ctrl+C para detener el servidor cuando termines."
wait $SERVER_PID
