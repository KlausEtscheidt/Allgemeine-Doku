# Upload nach Github

- Mit Sphinx Single-Html erzeugen.

- Verzeichnis build/singlehtml aus .gitignore entfernen

- Projekt pushen

- In Github Projekt Public machen

- Unter settings pages (links) wählen
    ```{image} github.png
    :alt: fishy
    :class: bg-primary
    :width: 500px
    :align: center
    ```

- rechts unter source auf github-actions stellen

- Static html wählen

- Im Fenster 'workflows/static.yml' ganz unten
    ```YAML
         uses: actions/upload-pages-artifact@v3
         with:
           # Upload entire repository
           path: '.'
    ```
    path auf `./doku/build/singlehtml`