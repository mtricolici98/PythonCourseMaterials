# Writing to a file

Make a small program that takes user input, and stores the information to a file. Call the file `write_test.txt`

The program must work in such a way, that if the file does not exist, it is created. However, if we launch the program
again, and the file already exists, instead of writing over the information, the information is added to the file
instead.

Example:

First Run we type in:

`Hello World`.

The file gets created and `Hello World` is stored in the file.

Second run we type: `Bye world`.

Now the file contains the following data:

```
Hello World
Bye world
```
