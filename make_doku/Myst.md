# Myst-Knoff-Hoff

https://myst-parser.readthedocs.io/en/latest/intro.html

## Setup/Installation

```shell
pip install myst-parser
```

in conf.py eintragen:
extensions = ["myst_parser"]

### sphinx-autodoc2
funzt nicht
```shell
pip install sphinx-autodoc2
```
Eintrag in conf.py extensions = ["autodoc2",]

### Wandle rst in myst

```shell
pip install "rst-to-myst[sphinx]"
rst2myst convert docs/**/*.rst
```
s. https://rst-to-myst.readthedocs.io/en/stable/index.html

## direktiven

rst-Format:

```
.. note::

Achtung
```

Myth-Stil:
````md
```{note}
Achtung
```
````

oder klassisch:

````md
:::{note}
Achtung
:::
````

:::{note}
Achtung
:::


ergibt:

```{note}
Achtung
```

### Software-Modul

## roles
Sphinx :rolle: wird zu {rolle}

### GUI-Buttons etc
:::{code}
{guilabel}`meinbutton`
:::
{guilabel}`meinbutton`

## Code-Blocks


````md
```python
def myfunc():
    x = 5
```

oder

:::{code-block} python
def myfunc():
    x = 5
:::

````
 wird zu

```python
def myfunc():
    x = 5
```

Inline Python code 
```md
`a = "b"`{l=python}
```
wird zu `a = "b"`{l=python}

Sprachcodes (s. https://pygments.org/docs/lexers/#pygments.lexers.shell.BatchLexer):

    - python
    - ps1
    - doscon
    - md
    - vbnet

## Include
````md
```{literalinclude} err_test.py
:language: pyton
```
````

## Bilder
````md
```{image} github.png
:alt: fishy
:class: bg-primary
:width: 500px
:align: center
```
````

## Links + Targets

https://myst-parser.readthedocs.io/en/latest/syntax/cross-referencing.html

### links
#### Externe (lokale) Files

:::{Attention}
Absolute Pfade in Myst sind absolut zum Projektverzeichnis und nicht zum Filesystem !!

Links gehen nur mit Hmtl:

```md
<a href = "file:///V:/Tools/Excel%20Makros/doku/Benutzer_Anleitung%20Ersatz_Auftragsverfolgung.pdf"> link </a>
```
:::

#### Links zu anderen md-files
```md
 [](./Komponenten.md#software-komponenten)
```
linkt zum Anker *software-komponenten* der Datei *Komponenten.md*.

#### Links zu Software-Doku

```md
[](#Auftragsposition.Init)
```

linkt zur Beschreibung der *Init*-Methode der Klasse *Auftragsposition*.\
Evtl muss auch noch ein Modulname vorangestellt werden.

### Targets
#### Targets automatisch erzeugen
myst_heading_anchors = 2 in conf.py einfügen

s. https://myst-parser.readthedocs.io/en/v0.13.7/using/howto.html

Referenzen gehen anscheinend nur mit der Syntax [meinText](#targets-automatisch-erzeugen), wenn `targets-automatisch-erzeugen` die target-id ist:
```md
 [meinText](#targets-automatisch-erzeugen)
```

#### Suche link-Targets:
```console
myst-anchors -l 2 meine.md
```

## Markdown generell

### VS-Code

s. https://code.visualstudio.com/docs/languages/markdown

To switch between views, press **Ctrl+Shift+V** in the editor. 

You can view the preview side-by-side **(Ctrl+K V)** with the file you are editing and see changes reflected in real-time as you edit.