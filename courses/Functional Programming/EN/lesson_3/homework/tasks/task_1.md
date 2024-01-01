# File list

Create a python program that will take as an input a `path` in the computer: ex: `C:\Program Files\`.

The program should list all files (and only files, not other folders) inside the folder if the path provided is a
folder.

If the path is not a folder, the program should show a nice error: `Provided path is not a folder.`

If the path does not exist, the program should show a nice error: `Provided path does not exist.`

### Hints:

Use: os.path.isdir, os.path.join(), os.listdir
