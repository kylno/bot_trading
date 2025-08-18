@echo off
title 🔍 Diagnostic IA uniquement

echo 🔎 Lancement du diagnostic auto_env_check.py...
cd /d "%~dp0automation"
python auto_env_check.py

echo ✅ Diagnostic terminé.
pause