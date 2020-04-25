@echo off
for /f %%f in ('dir /b json') do json2direct.py json/%%f
