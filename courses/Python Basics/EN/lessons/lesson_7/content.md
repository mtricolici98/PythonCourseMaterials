## Iteration and Loops

This topic will cover the basics of loops, including the for loop, nested for loops, and while loops, along with their
appropriate use cases.

Loops are control structures that allow us to execute a block of code repeatedly based on a given condition.
They help automate repetitive tasks and process collections of data efficiently. Iteration refers to the repetition of a
certain set of instructions or code until a specific condition is met.

In Python, we can iterate over various types of objects, including **strings**, **lists**, **tuples**, **sets**,
and **dictionaries**.

## How the for loop works:

The **for** loop is used to iterate over a sequence of elements, such as a list or a string. It has the following
syntax:

```
for element in sequence:
    # code block to be executed
```

The loop iterates over each element in the sequence and executes the code block. The "element" variable takes the value
of each item in the sequence one by one. The loop continues until all elements in the sequence have been processed.

## Nested for loops:

Nested for loops are used when we need to iterate over multiple sequences simultaneously. This allows us to perform
operations on combinations of elements from different sequences. The inner loop is executed completely for each
iteration of the outer loop. Here's an example:

```
for i in range(3):
    for j in range(2):
        print(i, j)
```

This code will output the following:

```
0 0
0 1
1 0
1 1
2 0
2 1
```

### A practical example where nested loops are used:

Find all combinations of `a` and `b` where `a + b == c`. Having `c` as input from the console.

```python

c = int(input('C: '))

for a in range(1, c):
    for b in range(c - a + 1):
        if a + b == c:
            print(f'{a} + {b}')
```

Let's look at other examples, utilizing the **rows and columns**:

Where we calculate row out of the table below has the largest sum of elements.

```python

table = [
    [5, 4, 3, 2, 1, 2, 6, 7],
    [5, 4, 3, 2],
    [1, 5, 6, 1, 2, 6],
    [1, 6, 9, 1, 6, 2, 4, 6],
    [6, 3, 4, 9, 6, 4, 1],
]
largest_row = None
sum_largest_row = 0
for row in table:
    # Calculating the ROW information for current ROW
    sum_this_row = 0
    for element in row:
        sum_this_row += element

    # Comparing to previous results
    if sum_this_row > sum_largest_row:
        # This row is larger than any other previous row, meaning it becomes the new largest row
        largest_row = row
        sum_largest_row = sum_this_row

print(f"Largest Row Is {largest_row}")
```

In the example above, we check each row in the table, and on each iteration, we conditionally change the variables from
outside the loop.

## What are while loops:

For loops are great at iterating over a fixed length of items. Thus, for-loops only allow to iterate a fixed number of
times.

To overcome this limitations, programming also has **while loops**.

While loops repeatedly execute a block of code as long as a specified condition is true. It is useful when the number of
iterations is unknown or depends on user input. The syntax for a while loop is as follows:

```
while condition: # condition is boolean
    # code block to be executed
```

The loop will continue to execute the code block until the condition evaluates to False. It's important to ensure that
the condition eventually becomes False; otherwise, the loop will run indefinitely, causing a program to hang.

## Uses of while loops

While loops can be used the same way for loops can be used, and more, however with while-loops you must always be
mindful about the **exit-condition.**

The **exit-condition** of a while loop, is "what should happen for a loop to stop".

A simple example is the following:

```python
should_run = True
collected_string = ''
while should_run:
    print('Welcome to my string collector, type in any string and press enter to add it to the collection.')
    print("or type `stop` to stop the program")
    to_collect = input('?')
    if to_collect == 'stop':
        should_run = False
    else:
        collected_string += f"{to_collect}\n"  # Using a new-line to make it more beautiful.

print('The program managed to collect the following inputs:')
print(collected_string)
```

The program above will run **indefinitely** - This means that neither the user, nor the programmer can know how many
times the loop should be executed. But the programmer knows that at some point the program should stop, and he
implements the `exit-condition` of the loop.

Another use of the while loop, is to perpetually check something.

Let's make a loop that will check that a timer is ready.

```python
import time  # Python time module 

timer_seconds = int(input("How many seconds ? "))

time_end = time.time() + timer_seconds  # The timer should end x seconds after now
time_now = time.time()
while time_now < time_end:
    print(f'Timer will run another {int(time_end - time_now)} seconds.')
    time.sleep(1)
    # Most important step of all
    time_now = time.time()

print('Timer done!')
```

> Note the last step of the loop

At the last step of the loop, we must update the `time_now` variable, to provide an exit condition. If we never
update `time_now` to be the current time, the program will wait indefinitely

> Actually, you can try it out yourself, comment out the last line of the loop.

## When to use while vs. for loops:

Use a **for** loop when **you know the number of iterations** in advance or need to iterate over a **known sequence of
elements**.
For example, when processing each item in a list or iterating through a string character by character.

Use a **while** loop when the number of iterations **is uncertain** or depends on a condition that may change during
execution.
For instance, when repeatedly asking for user input until a certain condition is met or when performing a task until a
specific state is reached.

Loops and iteration are fundamental concepts in Python programming. The for loop is suitable for iterating over known
sequences, while nested for loops handle multiple sequences simultaneously. On the other hand, while loops are useful
when the number of iterations is uncertain or based on a condition. Understanding when to use each type of loop is
essential for writing efficient and effective code.

## Practice Exercises

Practice makes perfect, this is why I want you to solve exercises (by yourself) to get a good hang of the concepts.

Certainly! Here's a list of distinct exercises, some using `while` loops and others using `for` loops, each chosen based
on the suitability of the loop type:

### While Loop Exercises:

1. **Countdown:**
   Print numbers from 10 to 1 in reverse order using a `while` loop.

2. **User Input Sum:**
   Take input from the user until they enter 0, then print the sum of all entered numbers using a `while` loop.


3. **Password Checker:**
   Ask the user to enter a password, and keep prompting until they enter the correct password ('secret') using a `while`
   loop.

### For Loop Exercises:

4. **Print Characters:**
   Print each character of a given string using a `for` loop.


5. **Table of Squares:**
   Print the squares of numbers from 1 to 5 using a `for` loop.

6. **List Sum:**
   Calculate and print the sum of elements in a list using a `for` loop.


7. **Nested Loop:**
   Print a pattern using nested `for` loops.
   Output:
   ```
   1
   1 2
   1 2 3
   ```

8. **Factorial with Range:**
   Calculate the factorial of a number using a `for` loop and the `range` function.

