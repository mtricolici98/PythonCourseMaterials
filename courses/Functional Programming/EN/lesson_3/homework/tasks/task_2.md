# Bulk Renamer

Using functions you have created for the exercise above (ex1.) create a program that will take as input a path to a
folder.

**WARNING**: Use a test path, with files specifically created for the test purpose. Be careful as to not change
something is system folders.

The program should rename all files in the folder to numbers (from 1 to n) sorted by the creation date of the
file: `os.path.getctime(file_path)` - will return the date created of the file.

The program should not overwrite the extension of the file: `file.extension` - For example `some_Doc.docx` should be
renamed to `1.docx`.

Also add an option to add a prefix, for example: Prefix `doc` will rename all files
to `doc1.docx`, `doc2.png`, `doc3.pdf`, `doc4.docx`....
