#!/bin/bash

# GhostTrack Installation for Termux

echo "╔═══════════════════════════════════════╗"
echo "║  GhostTrack Termux Installation       ║"
echo "╚═══════════════════════════════════════╝"
echo ""

echo "[*] Updating packages..."
pkg update -y
pkg upgrade -y

echo "[*] Installing Python..."
pkg install python -y

echo "[*] Installing dependencies..."
pip install -r requirements.txt

echo ""
echo "[✓] Installation complete!"
echo "[*] Run: python ghosttrack.py"
echo ""