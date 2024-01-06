## High order functions

A function, in programming is considered to be a `high order function` if it possesses the ability to receive another
function as input. In Python, all functions are `objects`, which means that they can be treated the same way all the
other variables are treated. This is known as **functions being first class citizens**.

### What do I mean ?

In many programming languages, there is not much you can do to a function.You can call it, maybe pass some arguments,
and that's about it. However, Python takes functions to a whole new level by treating them as first-class citizens. This
means that functions can be assigned to variables, passed as arguments to other functions, returned as values from other
functions, and even stored in data structures. This flexibility is the foundation for high-order functions in Python.

### Examples of High Order Functions

Let's delve into some practical examples to understand the concept of high-order functions better. One classic example
is the `map()` function. The `map()` function takes a function and an iterable (such as a list) as arguments and applies
the function to each item in the iterable, returning a new iterable containing the results.

```python
def square(x):
    return x ** 2


numbers = [1, 2, 3, 4, 5]
squared_numbers = map(square, numbers)
print(list(squared_numbers))  # Output: [1, 4, 9, 16, 25]
```

In this example, the `square()` function is passed as an argument to the `map()` function, making `map()` a high-order
function.

Another commonly used high-order function is `filter()`. The `filter()` function takes a function and an iterable,
applying the function to each item in the iterable and returning a new iterable containing only the items for which the
function returns `True`.

```python
def is_even(x):
    return x % 2 == 0


numbers = [1, 2, 3, 4, 5]
even_numbers = filter(is_even, numbers)
print(list(even_numbers))  # Output: [2, 4]
```

Here, the `is_even()` function is passed as an argument to the `filter()` function.

## Lambda Functions

To further enhance the concept of high-order functions, Python supports the creation of anonymous functions using lambda
expressions. Lambda functions are particularly useful when you need a simple function for a short period and don't want
to formally define it using the `def` keyword.

```python
numbers = [1, 2, 3, 4, 5]
squared_numbers = map(lambda x: x ** 2, numbers)
print(list(squared_numbers))  # Output: [1, 4, 9, 16, 25]
```

In this example, a lambda function is used directly within the `map()` function, demonstrating the conciseness and
flexibility that lambda functions bring to high-order functions.

Lambdas are often seen as `single use` functions, that is because they are commonly employed for short-term or specific
tasks where defining a full-fledged function using the `def` keyword would be too much work. The concise syntax of
lambda functions makes them ideal for quick, one-off operations. However, their apparent simplicity can sometimes lead
to misconceptions about their capabilities.

### Conciseness and Readability

One of the primary advantages of lambda functions is their conciseness. They allow you to define a function in a single
line of code, which can be particularly useful when the function is short-lived or when brevity is a priority. Consider
the following example using a lambda function to square a list of numbers:

```python
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
```

While lambda functions offer brevity, it's essential to strike a balance between conciseness and readability. In more
complex scenarios or when functions become intricate, using a named function with the `def` keyword might be more
appropriate for maintaining code clarity.

### Limitations of Lambdas

Lambda functions come with certain limitations. They are restricted to a single expression and cannot contain statements
or multiple expressions. This limitation arises from the need to maintain the simplicity and brevity of lambda syntax.
For more intricate logic, it is recommended to use a regular named function.

```python
# Lambda function (valid)
add = lambda x, y: x + y

# Lambda function (invalid)
# Uncommenting the line below will result in a syntax error
# complex_function = lambda x: if x > 0: x ** 2 else: x
```

Attempting to include an `if-else` statement in a lambda function, as shown in the commented code, would result in a
syntax error. In such cases, a named function is a better alternative.

### Use Cases for Lambdas

Lambdas shine in scenarios where a small, anonymous function is needed for a short duration. Common use cases include
sorting, filtering, and mapping operations. Consider the following example of sorting a list of tuples based on the
second element:

```python
pairs = [(1, 5), (3, 1), (8, 2)]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print(sorted_pairs)  # Output: [(3, 1), (8, 2), (1, 5)]
```

Here, the lambda function serves as a concise key function for sorting without the need for a separate named function.

## Functions inside other functions

Because functions are so portable, in Python you can write a function that only exists inside another function. This is
often done to encapsulate functionality, create closures, or implement specialized behavior that is only relevant within
a specific context. Functions defined within other functions in Python are known as inner functions or nested functions.

### Encapsulation and Scope

When a function is defined within another function, it gains access to the variables and parameters of its containing
function. This is due to Python's scoping rules. The inner function has access to its own local variables, the variables
of the outer function, and global variables (though modifying global variables from within a function is typically
avoided for clarity).

```python
def outer_function(x):
    def inner_function(y):
        return x + y

    return inner_function


closure = outer_function(10)
result = closure(5)
print(result)  # Output: 15
```

In this example, `inner_function` has access to the `x` parameter of `outer_function`, forming a closure. The
returned `inner_function` can then be assigned to the variable `closure` and invoked with its own arguments.

### Closure

A closure is a function object that has access to variables in its lexical scope, even when the function is called
outside that scope. Closures are a powerful concept, enabling the creation of functions with behavior dependent on
external variables while maintaining encapsulation.

```python
def power_of(base):
    def exponent(power):
        return base ** power

    return exponent


square = power_of(2)
cube = power_of(3)

print(square(3))  # Output: 8
print(cube(2))  # Output: 9
```

Here, `exponent` is an inner function that captures the `base` variable from its containing function `power_of`. The
returned functions (`square` and `cube`) act as specialized power functions.

### Specialized Behavior

Functions inside other functions are particularly useful when you need to create variations of a function with specific
behavior tailored to different scenarios. This is often seen in scenarios like configuration or customization.

```python
def greet(prefix):
    def greeting(name):
        return f"{prefix}, {name}!"

    return greeting


hello_greet = greet("Hello")
hi_greet = greet("Hi")

print(hello_greet("Alice"))  # Output: Hello, Alice!
print(hi_greet("Bob"))  # Output: Hi, Bob!
```

In this example, `greet` is a function that returns a specialized greeting function based on the provided prefix. This
allows for modular and customizable behavior without duplicating code.

## Decorators

Decorators (commonly seen using the `@` notation above a function definition) is a powerful and versatile feature in
Python that enables developers to modify or extend the behavior of functions or methods. They serve as wrappers around
functions, allowing you to execute code before and after the function's execution. Decorators are instrumental in
achieving cleaner, more modular, and reusable code, promoting the Don't Repeat Yourself (DRY) principle.

### Basics of Decorators

In Python, a decorator is a function that takes another function as input, extends the behavior of the latter function,
and usually returns a new function. The `@` symbol is a syntactic sugar that simplifies the application of decorators to
functions. Here's a simple example:

```python
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")

    return wrapper


@my_decorator
def say_hello():
    print("Hello!")


say_hello()
```

In this example, `my_decorator` is a decorator function that wraps around `say_hello`. When `say_hello()` is called, it
is actually `wrapper()` that gets executed, providing a way to extend the functionality of `say_hello` without modifying
its code directly.

### Applying Multiple Decorators

Python allows the stacking of multiple decorators on a single function. Decorators are applied from the innermost to the
outermost, creating a chain of wrappers around the original function. Consider the following example:

```python
def uppercase_decorator(func):
    def wrapper():
        result = func()
        return result.upper()

    return wrapper


def exclamation_decorator(func):
    def wrapper():
        result = func()
        return f"{result}!"

    return wrapper


@exclamation_decorator
@uppercase_decorator
def say_hello():
    return "hello"


print(say_hello())  # Output: HELLO!
```

In this example, `say_hello` is decorated first with `uppercase_decorator` and then with `exclamation_decorator`. The
order of decoration affects the final behavior of the function.

### Decorators with Arguments

Decorators can also accept arguments, adding another layer of flexibility. This is achieved by introducing an additional
layer of functions. For instance:

```python
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)

        return wrapper

    return decorator


@repeat(3)
def say_hello():
    print("Hello!")


say_hello()
```

In this example, the `repeat` decorator takes an argument `n` and returns a decorator function. The returned decorator
then repeats the execution of the original function `n` times.

### Use Cases of Decorators

Decorators are extensively used in web frameworks like Flask and Django for tasks such as authentication, logging, and
caching. They enhance code readability by separating concerns and promoting modular design.

