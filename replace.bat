@echo on
for /f %%f in ('dir /b txt') do perl -i.bak -lp -e "s/TOTALS:/U. S. Total/g" txt/%%f
del txt\*.bak
for /f %%f in ('dir /b txt') do perl -i.bak -lp -e "s/Totals:/U. S. Total/g" txt/%%f
del txt\*.bak
for /f %%f in ('dir /b txt') do perl -i.bak -lp -e "s/Totals/U. S. Total/g" txt/%%f
del txt\*.bak
for /f %%f in ('dir /b txt') do perl -i.bak -lp -e "s/Total:/U. S. Total/g" txt/%%f
del txt\*.bak
for /f %%f in ('dir /b txt') do perl -i.bak -lp -e "s/U.S. Total:/U. S. Total/g" txt/%%f
del txt\*.bak
for /f %%f in ('dir /b txt') do perl -i.bak -lp -e "s/U.S. Total/U. S. Total/g" txt/%%f
del txt\*.bak
for /f %%f in ('dir /b txt') do perl -i.bak -lp -e "s/U.S. Totals:/U. S. Total/g" txt/%%f
del txt\*.bak
for /f %%f in ('dir /b txt') do perl -i.bak -lp -e "s/U.S. Totals:/U. S. Total/g" txt/%%f
del txt\*.bak
for /f %%f in ('dir /b txt') do perl -i.bak -lp -e "s/U. S. Total /U. S. Total/g" txt/%%f
del txt\*.bak
for /f %%f in ('dir /b txt') do perl -i.bak -lp -e "s/U.S Total/U. S. Total/g" txt/%%f
del txt\*.bak
