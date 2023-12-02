# Lesson 12: Python Functions

In this lesson, we will explore the concept of functions in Python and understand their importance in creating modular and reusable code. We will cover various aspects of functions, including function arguments, return values, side effects, default arguments, and argument type hints. Let's dive in!

### What are Functions?

Functions are blocks of code that perform a specific task. They allow us to encapsulate a set of instructions and execute them by calling the function name. Functions can take input arguments, process them, and optionally return a value.

Here's an example of a simple function that greets a person:

```python
def greet(name):
    print("Hello, " + name + "!")

# Calling the greet() function
greet("John")
```

Output:
```
Hello, John!
```

In this example, the `greet()` function takes a `name` argument and prints a greeting message with the provided name.

### Pass Keyword

The `pass` keyword is used as a placeholder when we want to create a function or a code block without any implementation. It ensures that the code is syntactically correct. Let's see an example:

```python
def placeholder_func():
    pass

# Calling the placeholder function
placeholder_func()
```

No output will be generated from this function since it does not have any implementation yet. However, it is a valid function that can be filled in later.

### Docstrings

Docstrings are string literals used to document Python modules, classes, methods, and functions. They serve as inline documentation, providing information about the purpose, usage, and parameters of the function.

Here's an example of a function with a docstring:

```python
def add_numbers(a, b):
    """
    Adds two numbers and returns the result.
    Parameters:
    a (int): First number
    b (int): Second number
    Returns:
    int: Sum of the two numbers
    """
    return a + b

# Accessing the docstring
print(add_numbers.__doc__)
```

Output:
```
Adds two numbers and returns the result.
Parameters:
a (int): First number
b (int): Second number
Returns:
int: Sum of the two numbers
```

The `__doc__` attribute allows us to access the docstring associated with the function.

### Function Arguments

Python supports three types of function arguments: positional arguments, keyword arguments, and default arguments.

**Positional Arguments**:
These arguments are passed based on their position in the function call. The values are assigned to the corresponding parameters in the function definition.

```python
def greet(name, age):
    print("Hello, " + name + "! You are " + str(age) + " years old.")

# Calling the greet() function with positional arguments
greet("Alice", 25)
```

Output:
```
Hello, Alice! You are 25 years old.
```

In this example, the `name` and `age` parameters are positional arguments, and the values are assigned based on their position in the function call.

**Keyword Arguments**:
Keyword arguments are passed with their corresponding parameter names during the function call. This allows for more flexibility and readability.

```python
def greet(name, age):
    print("Hello, " + name + "! You are " + str(age) + " years old.")

# Calling the greet() function with keyword arguments
greet(name="Bob", age=30)
```

Output:
```
Hello, Bob! You are 30 years old.
```

Here, the function call explicitly mentions the parameter names, making it easier to understand the values being passed.

**Default Arguments**:
Default arguments have predefined values and can be omitted

 during the function call. If no value is provided, the default value is used.

```python
def greet(name, message="Welcome"):
    print(message + ", " + name + "!")

# Calling the greet() function with and without the message argument
greet("Alice")
greet("Bob", "Greetings")
```

Output:
```
Welcome, Alice!
Greetings, Bob!
```

In this example, the `message` parameter has a default value of "Welcome". If the argument is not provided during the function call, the default value is used.

### Returning Values from Functions

Functions can return values using the `return` statement. The returned value can be of any data type. When a function encounters a `return` statement, it immediately exits, and the specified value is passed back to the caller.

```python
def square(num):
    return num * num

# Calling the square() function and storing the returned value
result = square(5)
print(result)
```

Output:
```
25
```

The `square()` function calculates the square of a number and returns the result. We can capture the returned value and use it in other parts of our code.

### Function Side Effects

Functions can have side effects, which occur when a function modifies something outside of its own scope. Side effects include changing the value of a global variable, modifying a data structure, or printing output to the console.

```python
count = 0

def increment_counter():
    global count
    count += 1

# Calling the increment_counter() function multiple times
increment_counter()
increment_counter()
increment_counter()

print(count)
```

Output:
```
3
```

In this example, the `increment_counter()` function modifies the value of the global variable `count` by incrementing it. The function has a side effect on the variable.

### Positional vs Keyword Arguments

Python allows the use of both positional and keyword arguments together in function calls. Positional arguments must be provided in the same order as the parameters in the function definition, while keyword arguments are passed with the parameter names.

```python
def greet(name, message):
    print(message + ", " + name + "!")

# Calling the greet() function with a mix of positional and keyword arguments
greet("Alice", message="Hello")
greet(message="Greetings", name="Bob")
```

Output:
```
Hello, Alice!
Greetings, Bob!
```

Mixing both types of arguments provides flexibility and improves the clarity of function invocations.

### Argument Type Hints

Python supports type hints, which allow us to specify the expected types of function arguments and return values. Although type hints are not enforced by the interpreter, they serve as documentation and can be checked using static type checkers like `mypy`.

```python
def add_numbers(a: int, b: int) -> int:
    return a + b

# Calling the add_numbers() function with incorrect argument types
result = add_numbers("2", 3)
print(result)
```

Output:
```
TypeError: can only concatenate str (not "int") to str
```

In this example, we have provided incorrect argument types, resulting in a `TypeError`. Type hints help catch potential errors and improve code clarity.

Congratulations! You have now learned about Python functions, their arguments, return values, side effects, default arguments, and argument type hints. Functions are powerful tools that enable code reuse and organization. Utilize them effectively to write clean, modular, and efficient code.