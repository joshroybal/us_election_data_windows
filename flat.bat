@echo off
for /f %%f in ('dir /b json') do json2flat.py json/%%f
