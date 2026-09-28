@echo off

cd /d "%~dp0"

python -m uvicorn src.main:app --reload

pause
```
