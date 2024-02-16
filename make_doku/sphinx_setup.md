# Sphinx Projekt einrichten

## automatisches Anlegen

Halbautomatisches Anlegen der Projektstruktur für ein Python-Paket.

1. Verzeichnis anlegen

  ```console
      mkdir doku
      cd doku
      sphinx-quickstart
  ```

  Legt im Verzeichnis `doku` die nötigen Unterverzeichnisse und eine `conf.py` an.

2. Verzeichnis füllen

```console
  sphinx-apidoc -o doku  -f -e -a -A "Klaus Etscheidt" -H checkweb .\src
```
Legt wird eine komplette Struktur inkl conf.py an.\ 
Diese evtl nicht verwenden, da ungeeignet!

`.\src` zeigt auf das Unterverz src des Paketes, in dem die Python-Sourcen liegen. Es wird auch __init__.py gelesen und integriert.

```console
sphinx-apidoc -o doku -e .\src
```
Erzeugt nur rst-Dateien.

## manuelles Anlegen

Manuelles Anlegen der Projektstruktur für ein Python-Projekt oder eine beliebige andere Doku.

Verzeichnis anlegen, wie oben und conf.py von geeigneter Vorlage kopieren.

## Skripte für Ausgabe

Mit
```console
sphinx-build [options] <sourcedir> <outputdir>
```
werden aus den *.rst / *.md-Eingabedateien die Ausgaben erzeugt.\
\<sourcedir\> ist dabei der Top-Knoten der Eingabedateien in dem auch conf.py steht.\
Die Ausgaben landen in \<outputdir\>.

Zur einfacheren Bearbeitung gibt es zwei Powershell-Skripte zum Erzeugen
eines kompilierten Helpfiles (Htmlhelp *.chm) bzw. einer Html-Ausgabe.

### makeall_chm.ps

Erzeugt zunächst die Html-Ausgaben. 
Der Name der Dateien wird in conf.py über `htmlhelp_basename` definiert.
Es entsteht eine entsprechende *.hhp-Datei, die von dem Skript über hhc.exe
in die *.chm-Datei kompiliert wird.

Das Skript prüft ob die chm-Datei aktuell angezeigt wird und stoppt den zugehörigen Prozess.

Wenn dieser beendet ist, wird die chm-Datei ins source-Verzeichnis verschoben
und angezeigt.

Das Skript muss für neue Projekte zumindest an folgenden Punkten angepasst werden:

```Powershell
    # Projektname der in conf.py als htmlhelp_basename eingetragen wurde
    # Hieraus entsteht der Name der *.hhp-Datei
    $projekt = "knoffhoff"
    # Fenster-Titel der mit hhc.exe angezeigten Hilfe-Datei (zum killen)
    $window_title = "knoffhoff 1.0 Dokumentation"
    # Eingabeverzeichnis, das auch conf.py und die oberste index.md enthalten muss
    $sourcedir = '.'
    # Ausgabeverzeichnis (eigentlich immer build)
    $outputdir = 'build'
```

### makeall_singlehtml.ps1
Erzeugt ebenfalls die Html-Ausgaben und zeigt sie an. 
Anpassung wie [](#makeall_chmps) aber ohne `$windowtitle`{l=Powershell}

`a = "b"`{l=python}

## conf.py ergänzen

Damit die Python-Projketdateien gefunden werden, am Anfang sys.path erweitern.\
Dies ist nur für autodoc-Projekte nötig.\
Hier wird das Verzeichnis FotoAlbum in den Suchpfad eingefügt:
 
 ```{code-block} python
    # If extensions (or modules to document with autodoc) are in another directory,
    # add these directories to sys.path here. If the directory is relative to the
    # documentation root, use os.path.abspath to make it absolute, like shown here.
    #
    import os
    import sys
    # Hier liegt das Python-Basis-Verz FotoAlbum drei Ebenen über conf.py
    my_dir=os.path.abspath(os.path.join('.','..','..','..','FotoAlbum'))
    sys.path.append(my_dir)
```

Allgemeines:

 ```{code-block} python
    project = 'knoffhoff'
    copyright = '2024, Klaus Etscheidt'
    author = 'Klaus Etscheidt'
    release = '1.0'
    # root_doc = 'Readme'  macht Probleme root muss immer index heißen
    htmlhelp_basename = project
```

Sphinx Extensions:

 ```{code-block} python
    extensions = ['sphinx.ext.autodoc', 'sphinx.ext.coverage',
    'sphinx.ext.napoleon', 'sphinx.ext.todo', 'myst_parser']
```

Sonstiges:

 ```{code-block} python
    # Die Docstrings der Klasse und der init-Methode werden verwendet.
    autoclass_content = 'both'

    # Die Einträge werden wie im Source-Code angeordnet
    autodoc_member_order = 'bysource'
    # Keine Vererbung von Docstrings
    autodoc_inherit_docstrings = False

    # ???
    napoleon_use_param = True

    # Aut. Erzeugen von Ankern bei Überschriften bis level 7
    myst_heading_anchors = 7
    # Myst extension
    myst_enable_extensions = ["deflist"]
```

