@echo off
REM Se diriger au même niveau du fichier.
cd /d "%~dp0"
REM Récupère le nom d'utilisateur.
set PC_NAME=%computername%
REM Lancer l'éxécution du script principal.
py app/main.py %PC_NAME%