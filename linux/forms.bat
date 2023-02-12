@echo off
set /P a=a:
set /P b=b:
set /P c=c:
set /A r=%a%*%b%+%c%/(%c%*%c%/2)-1
echo a*b+c/(c*c/2)-1= %a%*%b%+%c%/(%c%*%c%/2)-1 = %r%
pause