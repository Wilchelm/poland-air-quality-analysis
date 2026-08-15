@echo off
setlocal EnableDelayedExpansion

rem -------------------------------------------------------------
rem 1. Definicje katalogow
rem -------------------------------------------------------------
set "BASE_DIR=%~dp0"
set "ZIP_INPUT_DIR=%BASE_DIR%Tutaj_umiesc_pliki_ZIP_z_danymi"
set "OUTPUT_DIR=%BASE_DIR%pomiary"

rem -------------------------------------------------------------
rem 2. Czy katalog z ZIP-ow istnieje?
rem -------------------------------------------------------------
if not exist "%ZIP_INPUT_DIR%" (
    echo.
    echo BLAD: Folder "%ZIP_INPUT_DIR%" nie istnieje!
    echo Utworz folder i umieść w nim pliki .zip
    pause
    exit /b 1
)

rem -------------------------------------------------------------
rem 3. Przygotuj (czyś) katalog wyjsciowy
rem -------------------------------------------------------------
if exist "%OUTPUT_DIR%" rd /s /q "%OUTPUT_DIR%"
md "%OUTPUT_DIR%"

rem -------------------------------------------------------------
rem 4. Sprawdz plik metadanych i uruchom skrypt Python, jesli potrzeba
rem -------------------------------------------------------------
set "METADATA_XLSX=%BASE_DIR%Metadane oraz kody stacji i stanowisk pomiarowych.xlsx"
set "METADATA_CSV=%BASE_DIR%Metadane oraz kody stacji i stanowisk pomiarowych.csv"

if exist "%METADATA_XLSX%" (
    if not exist "%METADATA_CSV%" (
        echo.
        echo Wykryto plik metadanych: Metadane oraz kody stacji i stanowisk pomiarowych.xlsx
        echo Uruchamianie skryptu poprawa_adresu_dlugosci_i_szerokosci_geograficznej.py …
        python poprawa_adresu_dlugosci_i_szerokosci_geograficznej.py
    ) else (
        echo.
        echo Plik metadanych istnieje zarówno w formacie .xlsx, jak i .csv – nic nie robie.
    )
) else (
    echo.
    echo Nie znaleziono pliku Metadane oraz kody stacji i stanowisk pomiarowych.xlsx
)

rem -------------------------------------------------------------
rem 5. Wypakuj wszystkie ZIP-ow do folderu pomiary
rem -------------------------------------------------------------
echo.
echo Wypakowuje archiwa ZIP…
for %%Z in ("%ZIP_INPUT_DIR%\*.zip") do (
    echo - %%~nxZ
    tar -xf "%%Z" -m -C "%OUTPUT_DIR%"
)

rem -------------------------------------------------------------
rem 6. Usuwanie wszystkich .xlsx, ktore **nie** zawieraja "_24g"
rem -------------------------------------------------------------
echo.
echo Czyszczenie folderu: zachowuje tylko pliki z "_24g.xlsx"…

for /R "%OUTPUT_DIR%" %%X in (*.xlsx) do (
    echo %%~nX | findstr /i "_24g" >nul
    if !errorlevel! EQU 0 (
        rem Ten plik zostaje – nic nie robimy
    ) else (
        del "%%X"
        echo Usunieto: %%~nxX
    )
)

rem -------------------------------------------------------------
rem 7. Uruchom skrypt Pythona tylko jesli brak jest pomiary.csv
rem -------------------------------------------------------------
set "CSV_OUTPUT=%OUTPUT_DIR%\pomiary.csv"

if not exist "%CSV_OUTPUT%" (
    echo.
    echo Brak pliku pomiary.csv – uruchamianie skryptu Python…
    python procesuj_pomiary.py
) else (
    echo.
    echo Plik %CSV_OUTPUT% juz istnieje – skrypt Python nie zostanie uruchomiony.
)

rem -------------------------------------------------------------
rem 8. Usun folder "pomiary" z zawartoscia (po zakonczeniu wszystkich operacji)
rem -------------------------------------------------------------
echo.
echo Usuwam katalog "%OUTPUT_DIR%" wraz ze wszystkimi plikami…
rd /s /q "%OUTPUT_DIR%"

rem -------------------------------------------------------------
rem 9. Końcowa informacja o brakujących elementach
rem -------------------------------------------------------------
set "METADATA_CSV=%BASE_DIR%Metadane oraz kody stacji i stanowisk pomiarowych.csv"
set "METADATA_XLSX=%BASE_DIR%Metadane oraz kody stacji i stanowisk pomiarowych.xlsx"
set "CSV_OUTPUT=%OUTPUT_DIR%\pomiary.csv"

if not exist "%CSV_OUTPUT%" (
    echo.
    echo Uwaga: Brak pliku %CSV_OUTPUT%. Nie ma danych pomiarowych (brak ZIP‑ów z danymi pomiarowymi).
) else if not exist "%METADATA_CSV%" (
    echo.
    echo Uwaga: Brak pliku %METADATA_CSV%. Nie ma danych odnośnie stacji pomiarowych (brak pobranego pliku Excel z danymi stacji).
) else (
    echo.
    echo Wszystko OK – dane pomiarowe i metadane (zarówno CSV, jak i XLSX) istnieją.
)

pause   rem <-- czeka na Enter, by uzytkownik mógł przeczytać komunikat
