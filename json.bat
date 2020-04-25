@echo off
for /f %%f in ('dir /b txt') do txt2json.py txt/%%f
