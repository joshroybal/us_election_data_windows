@echo off
for /f %%f in ('dir /b json') do json2csv.py json/%%f
