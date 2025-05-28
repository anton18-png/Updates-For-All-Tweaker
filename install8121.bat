@echo off
REM Проверяем, существует ли файл 8121.7z
if not exist "8121.7z" (
    echo Файл архива 8121.7z не найден!
    pause
    goto :eof
)

REM Проверяем, есть ли 7za.exe
if not exist "7za.exe" (
    echo Не найден файл 7za.exe!
    pause
    goto :eof
)

REM Распаковка архива в текущую папку
7za.exe x "8121.7z" -o"%cd%" -y

echo Распаковка завершена.
rem pause
