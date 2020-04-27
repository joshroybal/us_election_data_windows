@echo off
for /f %%f in ('dir /b json') do convertjson.py json/%%f %1
