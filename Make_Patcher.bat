@echo off
cd patcher
..\7za.exe a -tzip ../patcher.zip -x!*.zip
cd ..
copy /B /Y "metin2launch.bin"+"patcher.zip" "metin2launch.exe"
del patcher.zip
pause
