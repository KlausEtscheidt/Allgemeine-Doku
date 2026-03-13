# Pakete erzeugen

## Verzeichnis-Struktur

Zur Typerkennung mit mypy muss folgende Struktur entstehen:

```console
Paketname    (Projekt- oder Paketverzeichnis)
    |
    |_generateDok.py   (optional: Erzeugt Doku mit pydoctor)
    |_Readme.md        (optionale Beschreibung evtl für Github)
    |_pyproject.toml   !!! wichtig: definiert das Paket für pip install
    |_src              Verzeichnis mit Python-Code des Pakets
        |
        |_Paketname            Unter-Verzeichnis mit Python-Code des Pakets
            |_Init.py          Kann leer sein, sollte besser Dok-String für Paket enthalten
            |_modulname1.py    Python-Code für Modul modulname1 des Pakets
            |_modulname2.py    Python-Code für Modul modulname2 des Pakets
            |_py.typed         leere Datei. Zeigt mypy das die Module typisiert sind
    |_apidoc            (Ausgabe von generatDok.py)
```

Damit mypy die Typen in den Modulen erkennt bzw. prüft muss die Datei *py.typed* ins Paketverzeichnis
un im *pyproject.toml* eingetragen werden.

### vereinfachte Struktur

Es wird auf die Zwischeneben verzichtet.
Scheint z.T. Probleme mit Typ-Checkern/Lintern zu machen, die fehlende Import bemängeln
Import aber einfach mit `import modulename`{l=pathon}

```console
Projektname    (Projekt- oder Paketverzeichnis)
    |
    |_generateDok.py   (optional: Erzeugt Doku mit pydoctor)
    |_Readme.md        (optionale Beschreibung evtl für Github)
    |_pyproject.toml   !!! wichtig: definiert das Paket für pip install
    |_src              Verzeichnis mit Python-Code des Pakets
        |
        |_Init.py          Kann leer sein, sollte besser Dok-String für Paket enthalten
        |_modulname.py    Python-Code für Modul modulname1 des Pakets
    |_apidoc            (Ausgabe von generatDok.py)
```

## pyproject.toml

Beispiel für Paket *KeCmdRunner*

```toml
[build-system]
requires = [
    "setuptools>=42",
]
build-backend = "setuptools.build_meta"

[project]
name = "KeCmdRunner"
version = "1.0.1"
authors = [{name = "Klaus Etscheidt", email = "klaus.etscheidt@gmail.com"}]
description = "Klasse zum Ausführen von System-Befehlen mit subprocess"
license = "GPL-3.0-or-later"

[tool.setuptools.package-data]
"KeCmdRunner" = ["py.typed"]
```

Eintrag fuer mypy:

```toml
[tool.setuptools.package-data]
"KeCmdRunner" = ["py.typed"]
```

Bewirkt anscheinend ?!? das die Datei py.typed mit ins Paket kommt.

## Pakete zur Weiterentwicklung lokal installieren

im Vater-Verzeichnis von src (Projekt-Verzeichnis):

`pip install -e .`{l=console}

## Pakete in die Python-Lib (site-packages) installieren

1. wheel erzeugen
`python -m build`{l=console}
2. whell installieren
`pip install --force-reinstall dist\name_des_paket_wheels.whl`{l=console}

### komplette Anleitung unter

[https://packaging.python.org/tutorials/packaging-projects/](https://packaging.python.org/tutorials/packaging-projects/)

## Kontrolle mit Pip

**pip list**
: zeigt alle installierten Pakete

**pip show paket**
: zeigt abhängigkeiten

**pip show -f kefritz**
: zeigt files in Paket kefritz

## MyPy Typerkennung

Erfordert Eintrag
[tool.setuptools.package-data]
"FfmpegService" = ["py.typed"]

in pyprojekt.toml und ausserdem eine leere Datei py.typed im Paketverzeichnis

## Benutzung

**Achtung**
Wenn das Paket FfmpegService heißt, und die Datei darin FfmpegService.py
wird importiert mit:

`import FfmpegService.FfmpegService as ffmpeg`{l=python}

Mit dir(ffmpeg) kann geprüft werden, was im Modul bekannt ist.
