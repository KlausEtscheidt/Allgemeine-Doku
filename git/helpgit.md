# Git

```{contents} Inhalt
:depth: 3
:backlinks: top

```

## Neuanlage
1. .gitignore erzeugen

2. Lege lokales repos an
Über vscode/source control +

3. Verbindug zum remote-repo erzeugen mit  
git remote add GartenRaspi https://github.com/KlausEtscheidt/GartenRaspi  
(ersetze GartenRaspi)

4. Files vom remote laden
git pull GartenRaspi master

5. Alle files stagen und committen

6. Alles files hochladen
git push GartenRaspi master (oder pussh -u ???)  
git fetch GartenRaspi (aktuelle Info ueber remote holen, sonst letzter commit lokal unbekannt)

7. Check ob synchron
git status
git log

Wenn Inhalt auf client und server schon unterschiedlich vorhanden runterladen mit --allow-unrelated-histories  
git pull --allow-unrelated-histories GartenRaspi master

## Neuen branch downloaden
git fetch macht alle branches lokal bekannt  
dann git checkout to  
git branch name :erzeugt neuen lokalen branch  
git branch -vv: detail info ueber alle branches

## Entferne Files (untrack)
1. Alle anzeigen 
git ls-files
2. Entferne aus repo
git rm --cache filename
3. Kontrolle
git status zeigt file als staged und deleted; ls-files zeigt file nicht mehr
4. Commit und pull
3. Ignorierte anzeigen
git ls-files --others --ignored --exclude-standard

## Committs zeigen
git log --pretty=oneline
oder 
git log

## Tags
### anlegen
git tag vx.x (oder commit-id anhaengen => alter Stand wird getaged)    
### suchen
git tag -l v1.*
### auf Remote schieben
git push GartenGui --tags
### von remote loeschen
git push --delete GartenRaspi v3.3.01
### in neuen branch auschecken
git checkout -b neuerBranch v2.0.0

## Remotes
git remote -v (anzeigen)  
git remote show name (details anzeigen)  
git remote rename alter_name neuer_name (umbenennen)

## History löschen
https://tecadmin.net/delete-commit-history-in-github/

## Einzel-File downloaden
git show HEAD\~4:findsocket.sh > tmp_findsocket.sh  
mit HEAD~4 als treeish (commit id) 4 commits zurück  
und findsocket.sh Datei zum downloaden  
Achtung im Befehl oben steht im MD-Text HEAD\\\~4: da die Tilde sonst zum Format durchstreichen führt 

## Commits aus History entfernen
Commits, die behalten werden sollen, werden in neuen branch geschoben
1. Erzeuge neuen branch ('dummy') aus letztem Commit ('$last'), der behalten werden soll
git branch dummy $last
2. $destination ist Ziel branch $first der erste committ der behalten wird
  Die commits $first bis $last  sitzen jetzt auf $destination (werden angewandt)
  dummy hat Stand von $last
  Achte auf ^ hinter $first
git rebase -p --onto $destination $first^ dummy
3. Kontrolle 
gitk --all --date-order
4. Checkout $destination und bringe auf Stand von dummy (entspricht $last)
git checkout $destination
git reset --hard dummy
5. lösche dummy
git branch -d dummy
6. lösche commits aus Quellbranch $source
git rebase -p --onto $first^ $last $source
