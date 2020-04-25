@echo off
for /f %%f in ('dir /b json') do json2tab.py json/%%f
