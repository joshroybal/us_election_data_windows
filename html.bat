@echo off
for /f %%f in ('dir /b json') do json2html.py json/%%f
