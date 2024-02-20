# VS-Code Knoff-Hoff

## Tasks

Terminal / Aufgabe ausführen / "Zahnrad" öffnet tasks.json:

```{literalinclude} tasks.json
:language: json
```

Hier wurde das Powershell-Skript lint_all.ps1 eingebaut,
welches pslint startet:

```{literalinclude} lint_all.ps1
:language: ps1
```

Der problemmatcher-Abschnitt in der task filtert die Ausgabe von pylint
und überträgt sie in die vs-code "PROBLEME"