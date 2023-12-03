## Core concepts of control flow

Conditional statements are fundamental building blocks in programming that allow you to make decisions based on certain
conditions. They enable your program to execute different blocks of code depending on whether a given condition is true
or false. Conditional statements in Python include `if`, `elif`, and `else`.

## If and Else:

The `if` statement is used to execute a block of code only if a certain condition is true. The code block following
the `if` statement is executed if the condition is evaluated as **true**. Here's an example:

```python
age = 20

if age >= 18:
    print("You are eligible to vote.")
```

Output:

```
You are eligible to vote.
```

The `else` statement can be added to specify a block of code that should be executed if the condition in the `if`
statement is false. Here's an example:

```python
age = 15

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not old enough to vote.")
```

Output:

```
You are not old enough to vote.
```

### Important note on conditional blocks

Once your code has entered the conditional block it can not exit the block or enter the block if the condition changes.

Example:

```python
condition = True

if condition:
    print("We have entered the IF block")
    condition = False
    print("We are still running in the IF block")
    print("We can only exit this if-block if we exit the program")
else:
    print('I will never print')
```

But you may wonder, _what if my program wants to change its mind during a `if` condition_.

In such cases, we handle this by adding additional blocks.

```python
should_exit = input('Do you want to exit ? (y/n) ') == 'y'
if should_exit:
    print("preparing to close")
    should_exit = input('Are you sure you want to exit ? (y/n) ') == 'y'
    if should_exit:
        print('Still exiting')
        exit()
    else:
        print("Exit cancelled")
```

## Elif (else if):

The `elif` statement allows you to check for multiple conditions. It is useful when you have more than two
possibilities. The code block following the `elif` statement is executed if the corresponding condition is true. Here's
an example:

```python
age = 15

if age >= 18:
    print("You are eligible to vote.")
elif age == 17:
    print("You will be eligible to vote next year.")
else:
    print("You are not old enough to vote.")
```

Output:

```
You are not old enough to vote.
```

In this example, if the `age` variable is greater than or equal to 18, the first message will be printed. If it's 17,
the second message will be printed. Otherwise, the third message will be printed.

You can have multiple `elif` statements to check for different conditions.

## Using logical operators versus nested if statements:

Here's an example that demonstrates the use of nested `if` statements:

```python
age = 25
income = 50000

if age >= 18:
    if income > 30000:
        print("You are eligible for a loan.")
    else:
        print("You do not meet the income requirements.")
else:
    print("You are not old enough to apply for a loan.")
```

Output:

```
You are eligible for a loan.
```

In this example, the outer `if` statement checks if the `age` is greater than or equal to 18. If that condition is true,
it enters the nested `if` statement, which checks if the `income` is greater than 30000. If both conditions are true,
the message "You are eligible for a loan" is printed.

If the outer `if` condition is false (i.e., if the age is less than 18), the code proceeds to the `else` block, which
prints the message "You are not old enough to apply for a loan."

Nested `if` statements can be useful in scenarios where you need to evaluate multiple conditions in a hierarchical
manner, with different levels of checks and actions based on the outcome of each condition. However, as the level of
nesting increases, the code can become more complex and harder to read and maintain. In such cases, using logical
operators like `and`, `or`, and `not` can often lead to cleaner and more readable code.

Logical operators such as `and`, `or`, and `not` can be used to combine multiple conditions in a single statement. They
provide a way to express complex conditions without using nested `if` statements.

Example using `and`:

```python
age = 25
income = 50000

if age >= 18 and income > 30000:
    print("You are eligible for a loan.")
else:
    print("You are not eligible for a loan.")
```

Output:

```
You are eligible for a loan.
```

In this example, both conditions `age >= 18` and `income > 30000` must be true for the loan eligibility message to be
printed.

Logical operators can also be combined with `if`, `elif`, and `else` statements to create more complex decision-making
structures.

Using logical operators is generally preferred over using nested `if` statements, as it makes the code more readable and
easier to understand.

## Order of elif-blocks

The order of your elif blocks matters. The if/elif blocks are checked in sequence, on after the other, and python will
move to check the next block **only** if the condition on the previous block is **false**. This may lead to some
unexpected situations.

Think about the following example:

> Note: Code below is broken intentionally

```python
points = 70
if points >= 50:
    print('Grade is 5')
elif points >= 60:
    print('Grade is 6')
elif points >= 70:
    print('Grade is 7')
...
```

The code above will show `Grade is 5`, even though points is 70 which should be a `7`. This is because even though all
of conditions will resolve as True, only the first one will execute. **Other conditions only execute if the condition
above it is False.**

**Be careful, when ordering your conditions make sure that your conditions below have a chance to run at all.**

## Try-except

![f8d743ce-91eb-11ee-9837-7f0451042689.png](media%2Ff8d743ce-91eb-11ee-9837-7f0451042689.png)

Another interesting way to control the flow of the program is the `try: except:` block.

The `try-except` block allows the programmer to handle errors. By **handling**, I mean decide what happens when an error
occurs.

Errors are very common in programming, especially when humans are involved, this means that we should be ready for then
they happen and make the program do something smart with it instead of "crashing".
In Python, **errors** are called `exceptions`, the process of expecting an error to happen and executing alternative
code in
case it happens, is called **exception handling**.

```python

try:
    # This is the block where we are not sure if the code will run successfully.
    print("Asking user for a number")
    number = int(input("Enter a number: "))
    print(f"User has provided number {number}")
except Exception:
    # This is the code that we execute if there was an error in the code above.
    print("The value you entered is not a number, goodbye!")
    exit()
```

If we run the program above, we can enter a number as input, in that case we will see the following.

```
Asking user for a number
Enter a number: 10
User has provided number 10
```

However, if we enter a non-valid number string, the flow of execution will change:

```
Asking user for a number
Enter a number: ten
The value you entered is not a number, goodbye!
```

**Note** that as soon as the error happens, the code execution will switch from the `try` block to the `except` block.

It is also important to note, that there is no way to return back to the try block once the program entered a `except`
block, unless we use another try: except block in a different way.

```python
try:
    # This is the block where we are not sure if the code will run successfully.
    print("Asking user for a number")
    try:
        number = int(input("Enter a number: "))
        print(f"User has provided number {number}")
    except:  # This code will run only if there is an error in the above 2 lines.
        print(f"User did not provide a number")
    print(10 / number)
except Exception:
    # This is the code that we execute if there was an error in the code above.
    print("Some other error happened in the code")
    exit()
```

### What to write after except.

When we declare the `except` block, we have the option to provide "What kind of exception" we are expecting.

If we want to handle all kinds of exceptions, we should write `except Exception:` as this means,
**handle any exception**.

There are specific error types in Python, that sometimes help us do something different based on what has gone wrong.

For example:

* `int('Hello')` - this will raise a ValueError - Value is unexpected
* `10 / 0` - this will raise a ZeroDivisionError - Division by 0 is not possible
* `list(1,2,3)` - this will raise a TypeError - Type of arguments is not as expected

This way, we can control what happens in our program based on what the exception was.

```python
try:
    a = int(input())
    b = int(input())
    print(a / b)
except ValueError:
    print('Value entered is not a number')
except ZeroDivisionError:
    print('Division By 0 can not be done')
```

> Note that the main benefit of handling exceptions, is **NOT CRASHING THE PROGRAM**.

### Raising Exceptions

The process of telling the program that there was an error is called `raising an exception`.
This can be done using the `raise` keyword, followed by the exception type and message.

```python
age = 10
try:
    if age < 18:
        # raise ErrorType("Error message")
        raise ValueError("The user is too young!")
    print("Doing something awesome")
except ValueError as ex:
    print(ex)
```

In the example above we display two new concepts:

* Creating an error using `raise`
* Using the value of the exception using `as`

This means that when we encounter an error, we have access to it's message through the `ex` variable. Please note
that `ex` is a temporary variable name, and can be replaced with any other variable name.

### The except block

When the program is inside the `try` block, if the exception is raised, this would make the program skip to the
next `except` block.

The `except` block is however **not safe** from exceptions either. This may result in code like this:

```python
try:
    """something"""
except Exception as ex:
    try:
        """Something else"""
    except Exception as ex:
        print("Could not handle")
        exit()
```

Such examples of code, although completely correct, should be avoided, as it may lead to some VERY UGLY code.

> Note: Avoided doesn't mean NEVER DO IT, but instead it means that, if applicable, look for better ways to structure.

Instead, the programmer should try to solve the problem in a different way:

```python
first_attempt_success = True
try:
    """something"""
except Exception as ex:
    first_attempt_success = False
    print(f'First attempt failed because of: {ex}')

if first_attempt_success:
    print('done')
    exit()  # Early exit from program, as doing the second attempt is pointless

try:
    """Something else"""
except Exception as ex:
    print("Could not handle")
    exit()
```
