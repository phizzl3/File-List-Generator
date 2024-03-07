# File-List-Generator

 Gets a directory from the user and outputs a text file with a list of
 files located in that directory into the user's Downloads folder.

## Build info

Windows

```bash
pyinstaller -F -n "File List Generator" --icon=.\icon\list.ico .\file-list-generator\main.py 
```

MacOS

```bash
pyinstaller -F -n "File List Generator" ./file-list-generator/main.py 
```
