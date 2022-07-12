@echo off

pip freeze > requirements.txt
timeout /t 5
pip uninstall -r requirements.txt -y
