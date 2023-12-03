Use the input function to read a list of names from console. The names should be separated by a comma.

Ex: `Marius, Ion, Vasile`

Using the string `.split()` method, you generate a `list` form the string, call the list `list_of_names`.

For each **name** in the list_of_names, ask the user to input a `grade`, and store it in the `list_of_marks`.

> Note: You will notice that both lists should have the same length, and the indices for marks and names correspond.

Afterward do the following:

* Display the full list of names, and their grades in the following format: "Marius got grade: 10"
* Calculate the sum of all grades
* Calculate the average grade.

Complete the `___` with the necessary code.

```python
names = ___
list_of_names = names.split(__)

list_of_marks = []

for name in list_of_names:
    mark = ___
    ___

# Codul pentru a afisa notele

marks_sum = 0
for mark in list_of_marks:
    marks_sum += ___

print(f"Suma notelor: {marks_sum}")
print(f"Media notelor: {marks_sum / ___}")
```
