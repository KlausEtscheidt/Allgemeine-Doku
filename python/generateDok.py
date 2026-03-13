'''Erzeugt Html-Doku des Paketes (Quellen unter src) durch pydoctor im Vereichnis apidoc'''
from pydoctor.driver import main
from pathlib import Path
if __name__ == "__main__":
    # Das src-Dir liegt direkt unter diesem Script
    thisDir = Path(__file__).parent
    prjname = thisDir.name
    outDir = thisDir.joinpath('apidocs')
    # aktuelles Dir
    thisDir = Path(__file__).parent
    # Projektname
    prjname = thisDir.name
    # Format der Doc-Strings
    docformat= "google"
    # Ausgabe-Verz für Html
    outDir = thisDir.joinpath('apidocs')
    # Eingabedateien
    infile1 = thisDir.joinpath('src\\KeVideoTools')
    infile2 = thisDir.joinpath('test')

    params: list[str] = ["--mod-member-order source ",
                         "--cls-member-order source",
                        f"--docformat={docformat}",
                        f"--project-name {prjname}",
                        f"--html-output {outDir}",
                        f"{infile1}",
                        f"{infile2}"]

    paramStr = " ".join(params)

    try:
        main(paramStr)
    finally:
        input("weiter")
    pass  