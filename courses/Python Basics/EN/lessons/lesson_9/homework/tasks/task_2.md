## Count the words

> **Note**: this exercise requires a lot of problem-solving, and is extremely challenging.
>
> Do not use any data type we have not learned before this lesson.

Create a program that will analyze the text in the link: https://www.gutenberg.org/cache/epub/1513/pg1513.txt

The program would have to tell the user the following:

* Total number of words in the text
* Top 50 most used words
* Top 50 least used words

To store information about the number of times used, you can use two lists (like below).

Example:

```python
list_words = ['word1', 'word2', 'word3', ...]
list_times = [10, 20, 30, ...]

# We found word1 another time
list_times[list_words.index('word1')] += 1

print(list_times[list_words.index('word1')])  # 11
```

> Hint: You can sort a copy of the list of occurrences, and find based on index inside the non-sorted list, what word is
> part of the top most/least used words. (Note, you will need to also use "start" parameter for index.)

You can open the link and retrieve the data using the code below.

```python
from urllib.request import urlopen

link = 'https://www.gutenberg.org/cache/epub/1513/pg1513.txt'
response = urlopen(link)
all_text = response.read()
```
