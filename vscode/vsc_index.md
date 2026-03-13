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

## Erweiterungen


### neue Erweiterung beginnen

[siehe auch: https://code.visualstudio.com/api/get-started/your-first-extension](https://code.visualstudio.com/api/get-started/your-first-extension)

Tools installieren  
`npm install --global yo generator-code`

Projekt anlegen  
`yo code`

### Installation

[siehe auch: https://code.visualstudio.com/api/working-with-extensions/publishing-extension](https://code.visualstudio.com/api/working-with-extensions/publishing-extension)

vsce Tool installieren  
`npm install -g @vscode/vsce`

erzeugt vsix-Paket:  
`vsce package`

Installiert das Paket:  
`code --install-extension my-extension-0.0.1.vsix`
