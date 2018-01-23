# password-change-alert
Et verktøy i python for å varsle brukere om at passordet i ferd med å utløpe og la de endre det.

## Avhengigheter
Scriptet er skrevet for Python 2, så alle komponenter må være tilpasset det.

Last ned og installer følgende:

- [Python 2.7](https://www.python.org/ftp/python/2.7.13/python-2.7.13rc1.msi)
- [wxPython 3.0](https://sourceforge.net/projects/wxpython/files/wxPython/3.0.2.0/wxPython3.0-win32-3.0.2.0-py27.exe/download)
- [Python for Windows Extensions](https://github.com/mhammond/pywin32/releases/download/b222/pywin32-222.win32-py2.7.exe)

Kjør følgende kommando:

    pip install pyad

Du skal nå kunne teste scriptet ved å gå til mappen med scriptet og skrive

    python PasswordChange.py

## Oppsett
Endre navn på config_sample.py til config.py og tilpass innstillingene til deres miljø.

Legg ønsket logo i samme mappe som scriptet og kall den logo.png


## Kompilering med pyinstaller
For at brukerne skal unngå å måtte ha alt dette kan scriptet kompileres til en exe med PyInstaller.

Installer PyInstaller med pip:

	pip install pyinstaller

Kompiler scriptet med denne kommandoen:

    pyinstaller --add-data logo.png;logo.png --onefile --distpath c:\PythonBuild --noconsole --win-private-assemblies PasswordChange.py

Scriptet skal nå finnes som C:\PythonBuild\PasswordChange.exe og kan distribueres til brukerne.