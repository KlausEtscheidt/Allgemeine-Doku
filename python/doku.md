# Python dokumentieren

- größere Projekte: sphinx
- sonst: pydoctor

## Pydoctor

Ist eine schneller einzurichtende Alternative zu sphinx.

Mit folgendem Beispiel-Script **generateDok.py** wird eine Html-Doku aus den Dokstrings erzeugt:

```{literalinclude} generateDok.py
:language: python
```
Das Script geht davon aus, das es direkt über dem src-Verzeichnis, also im Projekt-Verzeichnis steht.
Könnte geändert werden, macht aber so Sinn (siehe Pakete erzeugen/Verzeichnisstruktur).

Das Script durchsucht die beiden angegebenen **infiles**.  
Es können auch Verzeichnisse angegeben werden, wobei z.T. unerwünschtes mit durchsucht wird.  
Die Ausgabe erfolgt, wie angegeben ins Verzeichnis **apidoc**, das parallel zum Script liegt.

Weiter werden der **Projektname** und das Format der **DokStrings** festgelegt.

## Pydoc

`python -m pydoc -b` startet den Browser und einen Server und zeigt alle auffindbaren Pakete an.

Das eignet sich auch zur Kontrolle ob ein Paket installiert wurde und was drin ist.

Es wertet ebenfalls die Dokstrings aus. Das Ergebnis ist aber unübersichtlicher als bei pydoctor

## Paket KeInspect

(noch in Arbeit)

Tool analysiert Python-Datei und erstellt Listen von Klassen, Funktionen usw.

Das Ergebnis wird in die Zwischenablage kopiert und kann in den Modul-Dokstring kopiert werden !!!