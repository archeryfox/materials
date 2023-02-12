chcp 65001
:: 1. В любом каталоге создайте Book.bat
:: 2. В пакетном файле Book.bat необходимо прописать код таким образом, чтобы при его вызове запрашивалось ввести число от 4 до 9, которое будет соответствовать кол-ву файлов, создаваемых на рабочем столе с названием Page*.bat (где * - порядковый номер). В случае ввода пользователем числа, выходящего за допустимый диапазон – вывести предупреждающее сообщение и попросить ввести число еще раз.
:: 3. Запустив один из файлов должна открыться консоль, где некоторое время будет идти загрузка. Если файл выигрышный, то консоль выдаст результат «Молодец! Ты угадал» (с изменением цвета консоли 7 сек), если нет, то «Неправильно, попробуй еще раз».
:: 4. После того, как был открыт выигрышный файл, все Page*.bat файлы удаляются.
@echo off
color 5
cd "C:\Users\arche\OneDrive\Рабочий стол"
:start
set /p tickets=Введите волшебное число от 4 до 9:
cls
if %tickets% lss 4 (echo %tickets% neq 4-9 && goto start) 
else (if %tickets% gtr 9 (echo tickets neq 4-9 && goto start))
for /l %%b in (1, 1, %tickets%) do @(echo @echo off > Page%%b.bat 
&& echo timeout /T 3 /nobrake >> Page%%b.bat 
&& echo color 4 >> Page%%b.bat 
&& echo echo Мда мда... чот не фортануло те >> Page%%b.bat  && echo timeout /T 5 /nobrake >> Page%%b.bat)
set /A R=(%RANDOM%%%%tickets%)+1
echo @echo off > Page%R%.bat 
&& echo timeout /T 3 /nobrake >> Page%R%.bat 
&& echo color 4 >> Page%R%.bat 
&& echo echo павизло паавизлооо)) >> Page%R%.bat 
&& echo timeout /T 6 /nobrake >> Page%R%.bat 
&& echo cd "C:\Users\arche\OneDrive\Рабочий стол" >> Page%R%.bat 
&& echo del Page*.bat >> Page%R%.bat
@REM бай бай сисадменщек)))))) анимечнек