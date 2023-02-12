
chcp 65001
::1. Создать на диске С:\ папку Course;
REM 2. Создать в папке Course папку «Номер вашей группы»;
REM 3. В папке «Номер вашей группы» создать текстовый файл 
REM с именем «Ваша фамилия».txt;
REM 4. Скопировать данный файл в папку Course;
REM 5. Переименовать в папке Course файл «Ваша фамилия».txt 
REM на «Фамилия соседа по парте».txt;
REM 6. Удалить из папки «Номер вашей группы» файл «фамилия».txt;
REM 7. Вывести на экран сообщение: «Командный
REM файл создал студент «ваша фамилия»».
@echo off 

set group=П50-4-21
set mymame=Жабовский
set friend=Игошев
md C:\Course
cd C:\Course
md %group%
cd > C:\Course\%group%\%mymame%.txt
copy C:\Course\%group%\%mymame%.txt C:\Course
ren C:\Course\%group%\%mymame%.txt %friend%.txt
del C:\Course\%group%\%mymame%.txt
@echo on
echo Файл создан мной, а точнее студентом %mymame% из группы %group%
pause