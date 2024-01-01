## Built In-Modules

Python empowers developers with a rich selection of built-in modules and packages. Among
these, the `os`, `sys`, `collections`, and `re` modules play a pivotal role in simplifying tasks and expanding the
functionality of Python programs. This comprehensive guide will delve into the capabilities of these modules,
elucidating their usage with detailed explanations and practical code examples.

## The `os` Module

The `os` module serves as a robust interface for interacting with the operating system, offering functions for file and
directory manipulation, process management, and environment variables.

The OS module, mainly does not care if your system is Windows, MacOS or Linux, it should work the same, this is why a
lot of people now use Python instead of "OS Specific" programming languages for system automation.

There are a few things we can do using the `os` module.

### File and Directory Operations

The `os` module facilitates working with files and directories in a platform-independent manner. For
example, `os.getcwd()` retrieves the current working directory, providing a foundation for navigating the file system.

```python
import os

# Get the current working directory
current_directory = os.getcwd()
print("Current Directory:", current_directory)
```

The `cwd` is useful when working with files. And specifically **relative file paths**.

Similarly, `os.listdir(path)` fetches the contents of a directory, enabling developers to inspect and process files
programmatically.

```python
import os

# List files in a directory
directory_path = "/path/to/directory"
files_in_directory = os.listdir(directory_path)
print("Files in Directory:", files_in_directory)
```

File manipulation is streamlined with functions like `os.remove(file)` for deletion and `os.rename(old, new)` for
renaming.

```python
import os

# Remove a file
file_to_remove = "example.txt"
os.remove(file_to_remove)

# Rename a file
old_name = "old_name.txt"
new_name = "new_name.txt"
os.rename(old_name, new_name)
```

### Process Management

The `os` module facilitates process management through functions like `os.system(command)`, allowing the execution of
shell commands from within Python scripts.

```python
import os

# Execute a shell command
os.system("ls -l")  # May not work on windows
```

Additionally, process-related information, such as the current process ID, can be retrieved using `os.getpid()`.

```python
import os

# Get the process ID of the current process
current_pid = os.getpid()
print("Current Process ID:", current_pid)
```

Environmental variables, critical for configuration and parameterization, can be manipulated using `os.environ`.

```python
import os

# Set an environment variable
os.environ["MY_VARIABLE"] = "my_value"
```

#### What are env-vars

Environmental variables are the most common way we, as programmers make our program run on different configuration. One
very commonly used env-var is: `IS_DEVELOP` or `DEVELOPMENT` or whatever you want to call it. It is often used to let
the program know that it is running in **development mode**, meaning it may output some more info in the console than
running in **production mode**, which should be a little more secretive.

## The `sys` Module:

The `sys` module facilitates interaction with the Python interpreter and the system environment, aiding in runtime
environment manipulation, command-line argument handling, and inter-script communication.

### Command-Line Arguments

`sys.argv` allows access to command-line arguments, enabling the creation of more dynamic and adaptable scripts. This is
specifically useful when we try to make command line applications and tools.

```python
import sys

# Access command-line arguments
script_name = sys.argv[0]
arguments = sys.argv[1:]
print("Script Name:", script_name)
print("Command-Line Arguments:", arguments)
```

### Runtime Environment

The `sys` module provides tools to manipulate the Python runtime environment. For instance, modifying the module search
path with `sys.path.append("/path/to/custom/module")` allows dynamic module loading.

This allows us to dynamically make our python detect more modules and more python `code` while the program is running.

```python
import sys

# Manipulate the module search path
sys.path.append("/path/to/custom/module")
```

#### Understanding PythonPath

The term `pythonpath` refers to a list of directories that Python traverses when searching for modules. The Python
interpreter searches through the entries of this list to find the location of modules that are needed for your code to
run.

Python tries to find the modules that are needed by your code in a specific order. It first looks in the current
directory, and then traverses the system's PATH environment variable. If a module is not found in either of these
locations, the interpreter will look for it in the PYTHONPATH environment variable.

You can set the PYTHONPATH environment variable to include the directories where you keep your custom modules. This
allows you to easily import those modules into your code without having to specify the full path to the modules.

Here are some commands that can be used to configure the PYTHONPATH environment variable:

1. **Windows**: export PYTHONPATH=C:\\path\\to\\my\\modules

2. **macOS/Linux**: export PYTHONPATH=$PYTHONPATH:/path/to/my/modules

3. **Adding to the beginning of the Python path**: export PYTHONSTARTUP=~/.pythonrc

4. **Using a virtual environment**: create a virtual environment and activate it before running your Python scripts.
   This will create a separate PYTHONPATH for your project and prevent conflicts with other projects on your system.

By setting the PYTHONPATH environment variable, you can easily manage the location of the modules that your code needs.
This makes it easier to maintain and share your code with others.

### Interpreter info

Information about the Python interpreter's version (`sys.version`) and the underlying operating system (`sys.platform`)
can be obtained for enhanced program adaptability.

```python
import sys

# Get Python version information
python_version = sys.version
print("Python Version:", python_version)

# Identify the operating system
platform = sys.platform
print("Operating System:", platform)
```

## The `collections` Package

The `collections` package introduces specialized data structures, augmenting the capabilities of built-in types.
Namedtuples, counters, deques, and OrderedDicts address various programming challenges efficiently.

### Namedtuples

`collections.namedtuple()` facilitates the creation of lightweight, immutable data structures with named fields,
enhancing code readability and maintainability.

```python
from collections import namedtuple

# Create a namedtuple
Person = namedtuple("Person", ["name", "age", "gender"])
person = Person(name="Alice", age=25, gender="Female")

# Access fields
print("Name:", person.name)
print("Age:", person.age)
print("Gender:", person.gender)
```

This is extremely useful when you have a data type that is not used enough to be a full new data structure, but at the
same time it is helpful to have it in a structured entity.

### Counters

`collections.Counter` simplifies counting occurrences of elements in iterable objects, a valuable tool for frequency
analysis or data distribution tracking.

```python
from collections import Counter

# Count occurrences of elements in an iterable
numbers = [1, 2, 3, 1, 2, 3, 4, 5]
number_counts = Counter(numbers)
print("Number Counts:", number_counts)
```

### Deques

The `collections.deque()` provides a double-ended queue implementation, suitable for high-performance queues and stacks.
Its constant-time operations make it ideal for specific use cases.

```python
from collections import deque

# Create a deque
my_deque = deque([1, 2, 3])

# Perform deque operations
my_deque.append(4)  # Append element at the right end
my_deque.appendleft(0)  # Append element at the left end
popped_element = my_deque.pop()  # Remove and return element from the right end
popped_left_element = my_deque.popleft()  # Remove and return element from the left end
```

### OrderedDicts

`collections.OrderedDict` maintains the order of elements based on their insertion sequence, crucial for scenarios where
preserving order is essential.

```python
from collections import OrderedDict

# Create an ordered dictionary
ordered_dict = OrderedDict()
ordered_dict["one"] = 1
ordered_dict["two"] = 2
ordered_dict["three"] = 3

# Maintain order based on insertion
print("Ordered Dictionary:", ordered_dict)
```

## The `re` Module

The `re` module in Python provides a robust implementation of regular expressions, offering powerful tools for string
manipulation and pattern matching.

### Pattern Matching:

`re.match()` and `re.search()` allow for pattern matching at the beginning and anywhere in a string, respectively. This
is invaluable for validating user inputs, extracting information, or filtering data based on specific criteria.

```python
import re

# Check if a string starts with 'Hello'
pattern = re.compile("^Hello")
result = pattern.match("Hello, World!")
print("Pattern Match:", bool(result))
```

### Search and Replace

`re.sub()` facilitates pattern-based substitution, enabling the modification of strings based on specified patterns.
This is especially useful for data cleaning and preprocessing tasks.

```python
import re

# Substitute 'apple' with 'orange

'
pattern = re.compile("apple")
text = "I have an apple and a banana."
modified_text = pattern.sub("orange", text)
print("Modified Text:", modified_text)
```

### Grouping and Capturing

Regular expressions support grouping and capturing, allowing developers to extract specific portions of matched
patterns. This feature is instrumental in extracting meaningful information from complex text data.

```python
import re

# Extract year, month, and day from a date string
pattern = re.compile(r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})")
date_string = "2022-01-01"
match = pattern.match(date_string)

# Access captured groups
year = match.group("year")
month = match.group("month")
day = match.group("day")

print("Year:", year)
print("Month:", month)
print("Day:", day)
```

### Other examples:

Regular expressions (regex) are a powerful tool for text manipulation in Python. They allow you to search, extract, and
modify text in a flexible and efficient way. Here are some useful examples of how to use regular expressions in Python:

**1. Extracting email addresses from text:**

```python
import re

text = "Please contact me at johndoe@example.com or jane.smith@gmail.com"

pattern = r"[\w+\.]+@[\w+\.]+\.[a-zA-Z]{2,}"

matches = re.findall(pattern, text)

print(matches)  # Output: ['johndoe@example.com', 'jane.smith@gmail.com']
```

**2. Validating phone numbers:**

```python
import re

phone_number = "+1 415 555-1212"

pattern = r"^\+\d{1,3} \d{3}-\d{3}-\d{4}$"

if re.match(pattern, phone_number):
    print("Phone number is valid")
else:
    print("Phone number is not valid")
```

**3. Extracting URLs from web pages:**

```python
import re

html_text = """
<html>
  <head>
    <title>My Website</title>
  </head>
  <body>
    <a href="https://www.python.org/">Visit Python Website</a>
    <p>This is some text with no links.</p>
    <a href="https://www.google.com/">Visit Google Search</a>
  </body>
</html>
"""

pattern = r"<a\s+href=\"([^\"]+)\"\s*>(.+?)</a>"

matches = re.findall(pattern, html_text)

for url, text in matches:
    print(f"URL: {url}")
    print(f"Text: {text}")
```

**4. Replacing text with regular expressions:**

```python
import re

text = "This is a string with some numbers: 12345"

pattern = r"\d+"

new_text = re.sub(pattern, "X", text)

print(new_text)  # Output: This is a string with some numbers: XXXX
```

These examples demonstrate the versatility of regular expressions in Python. They can be used for a wide variety of
tasks, from simple text manipulation to complex data extraction and validation. With practice, you can master these
powerful tools to enhance your Python programming skills.

## Conclusion

Python's built-in modules and packages, are not limited to just `os`, `sys`, `collections`, and `re`, but they empower
developers to create robust, efficient, and platform-independent solutions.

By understanding and leveraging the functionalities of these modules, programmers can streamline common tasks, enhance
code readability, and build more maintainable and scalable applications.

As developers, you should continue to explore and master these built-in modules, gaining the ability to tackle a wide
range of programming tasks with confidence, elevating their Python programming skills to new heights.
