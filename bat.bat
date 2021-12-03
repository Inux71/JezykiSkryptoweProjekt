@echo off

:menu
echo ----------------------------
echo ------------MENU------------
echo ----------------------------
echo 1. Stworz raport
echo 2. Wyswietl ostatni raport
echo 3. Usun raporty
echo 4. Koniec
echo ----------------------------
set /p "wybor=Podaj opcje: "

if %wybor%==1 (
    cls

    call py1.py
    call py2.py
    echo Raport gotowy!

    goto :menu
)

if %wybor%==2 (
    cls
    if exist .\raporty\*.html (
        for /f %%F in ('dir .\raporty\ /b /o-d') do (
            call .\raporty\%%F
            goto :menu
        )
    ) else (
        echo Brak raportow!
    )

    goto :menu
)

if %wybor%==3 (
    cls
    if exist .\raporty\*.html (
        del .\raporty\*.html
        echo Raporty usuniete!
    ) else (
        echo Raporty usuniete!
    )

    goto :menu
)

if %wybor%==4 (
    goto :eof
)

pause