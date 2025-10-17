@echo off
set /p Desc=Enter message:
cd C:\Projects\Bootcamp\Python\PYDSConvertor
git add .
git commit -m "%Desc%"
git push
pause