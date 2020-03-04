# password-change-alert
Et verktøy i python for å varsle brukere om at passordet i ferd med å utløpe og la de endre det.

## Avhengigheter
Scriptet er skrevet for Python 2, så alle komponenter må være tilpasset det.

Last ned og installer følgende:

- [Python 3.8](https://www.python.org/ftp/python/3.8.2/python-3.8.2.exe)
- [Python for Windows Extensions](https://github.com/mhammond/pywin32/releases/download/b227/pywin32-227.win-amd64-py3.8.exe)

Gå til mappen med scriptet og kjør følgende kommando:

    pip install -r requirements.txt

Du skal nå kunne teste scriptet ved å gå til mappen med scriptet og skrive

    python PasswordChange.py

Får du en feilmelding som følger, gjør dette: https://stackoverflow.com/questions/27404312/python-active-directory-module-no-module-named-adsi

    Traceback (most recent call last):
      File "PasswordChange.py", line 16, in <module>
        from win32com import adsi
      File "C:\Program Files\Python38\lib\site-packages\win32comext\adsi\__init__.py", line 25, in <module>
        from adsi import *
    ModuleNotFoundError: No module named 'adsi'

## Oppsett
Endre navn på config_sample.py til config.py og tilpass innstillingene til deres miljø.

Legg ønsket logo i samme mappe som scriptet og kall den logo.png


## Kompilering med pyinstaller
For at brukerne skal unngå å måtte ha alt dette kan scriptet kompileres til en exe med PyInstaller.

Installer PyInstaller med pip:

	pip install pyinstaller

Kompiler scriptet med denne kommandoen:

    pyinstaller --add-data logo.png;. --onefile --distpath c:\PythonBuild --noconsole --win-private-assemblies PasswordChange.py

Scriptet skal nå finnes som C:\PythonBuild\PasswordChange.exe og kan distribueres til brukerne.