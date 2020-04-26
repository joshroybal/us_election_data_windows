@echo on
"C:\Program Files\7-Zip\7z.exe" x txt.zip
mkdir json & call json.bat
rmdir txt /s /q
mkdir csv & call csv.bat
"C:\Program Files\7-Zip\7z.exe" a csv.zip csv
rmdir csv /s /q
mkdir tab & call tab.bat
"C:\Program Files\7-Zip\7z.exe" a tab.zip tab
rmdir tab /s /q
mkdir flat & call flat.bat
"C:\Program Files\7-Zip\7z.exe" a flat.zip flat
rmdir flat /s /q
mkdir direct & call direct.bat
"C:\Program Files\7-Zip\7z.exe" a direct.zip direct
rmdir direct /s /q
call html.bat
"C:\Program Files\7-Zip\7z.exe" a html.zip html
rmdir html /s /q
"C:\Program Files\7-Zip\7z.exe" a json.zip json
rmdir json /s /q
