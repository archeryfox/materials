chcp 65001
:: 1. В корневом каталоге создать папку FirstFolder используя переменную;
:: 2. Используя переменные создать в папке FirstFolder подпапку с названием SecondFolder;
:: 3. Создать 3 файла в директории SecondFolder, используя ввод с клавиатуры и записать в каждый из них некоторую информацию;
:: 4. Информацию из 3х выше созданных файлов необходимо записать в файл all.txt, который необходимо расположить в SecondFolder, а затем оттуда перенести его в FisrtFolder;
:: 5. С помощью команды Type вывести информацию из all.txt в консоль.
:: 6. Составьте формулу, которая должна состоять  из: «( )», «*», «/»,«%», «+» и «-». Значения для данной формулы должны задаваться через консоль пользователем. Вывести результат вычисления по формуле в консоль. Данную формулу необходимо записать в новый bat-файл, а запуск файла с формулой осуществить через основной пакетный файл (в котором вы прописывали все предыдущие пункты). 
@echo off
set fdr1=FirstFolder
set fdr2=SecondFolder
md C:\Course\%fdr1%
cd C:\Course\%fdr1%
md %fdr2%
:: @echo on
for /L %%i in (0,1,2) do (
set /P fn%%i=Введите название %%i го файла: 
cd > %fdr2%\%fn%%%i.txt
)
echo aaa > %fdr2%\%fn0%.txt	
echo bbb > %fdr2%\%fn1%.txt
echo ccc > %fdr2%\%fn2%.txt


type C:\Course\%fdr1%\%fdr2%\%fn0%.txt >> C:\Course\%fdr1%\%fdr2%\all.txt
type C:\Course\%fdr1%\%fdr2%\%fn1%.txt >> C:\Course\%fdr1%\%fdr2%\all.txt
type C:\Course\%fdr1%\%fdr2%\%fn2%.txt >> C:\Course\%fdr1%\%fdr2%\all.txt

type C:\Course\%fdr1%\%fdr2%\all.txt
call 
pause