# Lesson 4 - Sequences, Lists

## What are sequences?

Up until now, we have primarily worked with basic data types such as integers, floats, and strings. These data types excel at storing single values. However, there are situations where we need to store multiple values in a single variable. This is where sequences come into play. Sequences are data types that allow us to store more than one value.

## Lists

The list is perhaps the most commonly used sequence in Python. It is exactly what it sounds like—a list of items.

Items in a list can be of any type. For example, you can have a list that contains 3 numbers and 2 words. This flexibility is not always available in other programming languages.

Key features of lists are:

* **Ordered**: Lists maintain the order in which the items are added.
* **Changeable**: You can modify any item in the list, regardless of its position.
* **Non-Unique**: A list can contain multiple occurrences of the same value.

There are two ways to declare an empty list: using the list constructor or using square brackets ([]).

```python
my_list = list()
also_list = []
```

You can also create non-empty lists directly.

```python
non_empty = [1, 2, 3]
```

### A collection you already know

We have previously worked with strings, and I mentioned that a string is essentially a list of characters and behaves like one.

### Accessing values

Values in a list can be accessed using their index, which represents their position in the list. Similar to strings, the index starts at 0.

```python
my_list = ['first', 'second', 'third']
print(my_list[0])  # first
print(my_list[1])  # second
print(my_list[2])  # third
print(my_list[3])  # Error: index out of range
```

Negative indexes can also be used, and you can obtain sub-lists by slicing a list.

```python
my_list = ['one', 'two', 'three']
print(my_list[-2])  # two
print(my_list[-2:])  # ['two', 'three']
print(my_list[0:2])  # ['one', 'two']
```

### Lists are mutable

Lists are mutable, which means you can change their elements or add new elements without creating a new list instance.

To change an element in a list, assign a new value to the element at a specific index.

```python
my_list = [1, 2, 3]
my_list[1] = 4
print(my_list)  # [1, 4, 3]
my_list[1] = 'two'
print(my_list)  # [1, 'two', 3]
```

### Adding elements to a list

There are two main ways to add elements to a list:

1. Using the **.append()** function.
2. Combining with another list (list concatenation).

```python
my_list = []
# Using append
my_list.append('First item')

# Concatenating lists (similar to string concatenation) adds the two lists together.
my_list = my_list + ['Second Item']

# OR

my_list += ['Second Item']

print(my_list)  # ['First item', 'Second Item']
```

List concatenation is also possible using the dedicated function **.extend()**.

### Removing items from a list

#### Using **remove()**

You can remove an item from a list using the **.remove()** function. This method takes the value of the item you want to remove as an argument.

```python
my_list = [1, 2, 3]
my_list.remove(1)
print(my_list)  # [2, 3]
```

If the item appears multiple times in the list, only the first occurrence will be removed. If the item does not exist in the list, it will raise a ValueError.

```python
my_list = [1, 2, 2, 3]
my_list.remove(2)
print(my_list)  # [1, 2, 3]
```

#### Using **del**

The **del** keyword allows you to remove an item from a list using its index.

```python
my_list = [1, 2, 3]
del my_list[1]
print(my_list)  # [1, 3]
```

You can also remove a slice of a list using the **del** keyword.

```python
my_list = [1, 2, 3, 4, 5]
del my_list[1:3]
print(my_list)  # [1, 4, 5]
```

#### Using **pop()**

The **.pop()** function removes an item from a list at a specific index and returns the value of the removed item. If no index is specified, it removes the last item in the list.

```python
my_list = [1, 2, 3]
removed_item = my_list.pop(1)
print(my_list)        # [1, 3]
print(removed_item)   # 2

last_item = my_list.pop()
print(my_list)        # [1]
print(last_item)      # 3
```

### List methods and functions

Lists have several built-in methods and functions that allow you to manipulate and work with them:

- **len()**: Returns the number of items in a list.
- **count()**: Returns the number of occurrences of a specific item in a list.
- **index()**: Returns the index of the first occurrence of a specific item in a list.
- **sort()**: Sorts the items in a list in ascending order.
- **reverse()**: Reverses the order of items in a list.
- **clear()**: Removes all items from a list.
- **copy()**: Creates a shallow copy of a list.
- **extend()**: Appends all items from another list to the end of the current list.

These methods can be called using the dot notation on a list object.

```python
my_list = [1, 2, 2, 3, 4, 5]

print(len(my_list))            # 6
print(my_list.count(2))        # 2
print(my_list.index(3))        # 3

my_list.sort()
print(my_list)                 # [1, 2, 2, 3, 4, 5]

my_list.reverse()
print(my_list)                 # [5, 4, 3, 2, 2, 1]

my_list.clear()
print(my_list)                 # []

new_list = [1, 2, 3]
copied_list = new_list.copy()
print(copied_list)             # [1, 2, 3]

other_list = [4, 5, 6]
new_list.extend(other_list)
print(new_list)                # [1, 2, 3, 4, 5, 6]
```

## For loops, iteration

Another one of the main pillars of programming is iteration. **Iteration** is the process of doing the same thing multiple times with different values.

In Python, one way to achieve iteration is through the use of **for** loops. For loops are done using the **for ... in ...** blocks in Python. You can iterate through different collections such as lists and tuples.

Here's an example that demonstrates iterating over a list and printing each element:

```python
my_list = ['First', 'Second', 'Third']
for element in my_list:
    print(element)
# Output:
# First
# Second
# Third
```

You can iterate through tuples in the same way as any other collection:

```python
data = (52, 29, 39)
for el in data:
    print(el)
```

Let's consider a more practical example. Suppose we want to calculate the sum of a list of numbers:

```python
my_numbers = [10, 20, 14, 92, 20]
numbers_sum = 0  # Initialization of our collector variable
for number in my_numbers:
    numbers_sum += number  # Adding to our collector variable
print(numbers_sum)
```

In the above example, we iterate through the list of numbers and add each number to the `numbers_sum` variable.

## Range

Sometimes, you may want to iterate a certain number of times without having a specific list to iterate over. This is where the **range()** function comes in handy.

The **range()** function creates a sequence of numbers based on the parameters supplied to it. Here's an example that prints numbers from 0 to 4:

```python
for a in range(5):
    print(a)
# Output:
# 0
# 1
# 2
# 3
# 4
```

The **range()** function generates values one after another.

You can customize the **range()** function in several ways. For instance, you can specify the starting point and the end point of the range:

```python
for a in range(1, 6):
    print(a)
# Output:
# 1
# 2
# 3
# 4
# 5
```

In the above example, the range starts at 1 and ends at 6 (exclusive).

You can also provide a step value to control the increment between each iteration. The default step is 1, but you can customize it. For example:

```python
for a in range(0, 10, 2):
    print(a)
# Output:
# 0
# 2
# 4
# 6
# 8
```

In the above example, the range starts at 0, ends at 10 (excluding 10), and increments by 2.

### Negative ranges

It is possible to iterate downward into negative numbers by supplying a negative step value. Here's an example:

```python
for a in range(0, -5, -1):
    print(a)
# Output:
# 0
# -1
# -2
# -3
# -4
```

### Iterating a list using range

You can use the **range()** function to iterate over a list by using the length of the list as the range. Here's an example:

```python
my_list = [6, 9, 4, 2, 0]
for a in range(len(my_list)):  # len(my_list) == 5
    print(f'Item at index {a} is {

my_list[a]}')
# Output:
# Item at index 0 is 6
# Item at index 1 is 9
# Item at index 2 is 4
# Item at index 3 is 2
# Item at index 4 is 0
```

In the above example, we use the **range()** function with the length of the list. Each iteration of the range corresponds to the index position of the element in the list.

This approach can be further improved to work with two lists simultaneously, for example:

```python
list_1 = ['a', 'b', 'c']
list_2 = [97, 98, 99]
for index in range(len(list_1)):
    print(f'Letter {list_1[index]} has position {list_2[index]} in ASCII.')
```

The example above performs operations on both lists by using indexes instead of directly working with the collections.

### When is range helpful?

The **range()** function is helpful in the following scenarios:

1. When you want to perform a task a finite number of times.
2. When you want to access the index of an item during iteration.
3. When you want to know the count of iterations.

### What can we do inside an iteration (for loop)?

Inside an iteration, you can do anything you want. Here are a few examples:

1. Asking for user input:

```python
my_list = [2, 3, 4]
for a in my_list:
    print(f'Processing {a}')
    b = int(input('Enter a number: '))
    print(f'{a} * {b} = {a * b}')
```

2. Nested iteration:

```python
first_list = [10, 20, 30]
second_list = [90, 80, 70]
for a in first_list:
    for b in second_list:
        print(f'{a} * {b} = {a * b}')
```

3. Populating another list:

```python
number_list = [2, 3, 4, 5]
power_two_list = []
for number in number_list:
    power_two_list.append(number ** 2)  # a to the power of 2
print(power_two_list)  # Output: [4, 9, 16, 25]
```

4. Conditional processing:

```python
number_list = [23, 39, 48, 100]
numbers_under_50 = []
numbers_above_50 = []
for number in number_list:
    if number < 50:
        numbers_under_50.append(number)
    else:
        numbers_above_50.append(number)
```

In the above example, we iterate through a list of numbers and separate them into two lists based on a condition.

Additionally, you can make use of the `enumerate()` function to get both the index and the value of each item during iteration. Here's an example:

```python
my_list = ['apple', 'banana', 'orange']
for index, fruit in enumerate(my_list):
    print(f'Index: {index}, Fruit: {fruit}')
```

The `enumerate()` function returns an iterator that provides pairs of index and value for each item in the list. This can be useful when you need both the index and the value while iterating over a collection.
