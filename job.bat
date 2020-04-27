@echo on
"C:\Program Files\7-Zip\7z.exe" x txt.zip
mkdir json & call json.bat
mkdir csv & call convert.bat csv
mkdir tab & call convert.bat tab
mkdir flat & call convert.bat flat
call convert.bat html
