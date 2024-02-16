# Pakete erzeugen

## Aus sourcen zum Testen
pip install -e .
im Verzeichnis das ./src enthält

## Aus lokaler wheel
pip install --force-reinstall dist\checkweb-1.2.0-py3-none-any.whl

## wheel erzeugen
python -m build
im Verzeichnis das ./src enthält
copy dist/checkweb-1.2.0-py3-none-any.whl e:\

## Anleitung unter
https://packaging.python.org/tutorials/packaging-projects/

