chcp 65001
@echo off
color 5
cd C:\Users\vboxuser\Desktop
:start
set /p tickets=Привет это лотерея! Выбери число от 4 до 9: 
cls 
if %tickets% lss 4 (echo tickets neq 4-9 && goto start) else (if %tickets% gtr 9 (echo tickets neq 4-9 && goto start))
for /l %%b in (1, 1, %tickets%) do @(echo @echo off > Page%%b.bat && echo chcp 65001 > Page%%b.bat && echo TIMEOUT /T 3 /NOBREAK >> Page%%b.bat && echo color 6 >> Page%%b.bat && echo echo не тот >> Page%%b.bat  && echo TIMEOUT /T 5 /NOBREAK >> Page%%b.bat)
set /A R=(%RANDOM%%%%tickets%)+1
echo @echo off > Page%R%.bat && echo chcp 65001 && echo TIMEOUT /T 3 /NOBREAK >> Page%R%.bat && echo color 8 >> Page%R%.bat && echo echo Good job! You found it! >> Page%R%.bat  && echo TIMEOUT /T 5 /NOBREAK >> Page%R%.bat && echo cd C:\какой-то путь до рабочего стола\Desktop >> Page%R%.bat && echo del Page*.bat >> Page%R%.bat