## What are booleans ?

![9562a48a-9067-11ee-b8cf-4fdbacccbea2.png](media%2F9562a48a-9067-11ee-b8cf-4fdbacccbea2.png)

In programming a boolean is a data type that represents one of two possible values: True or False.
Booleans are commonly used in programming for decision-making, thus controlling the flow of a program,
and determining conditions.

As we know, also in real life, not everything is black and white, so we need a way to make our decision-making
operations a bit more complex, this is where boolean algebra is helpful.

Another interesting concept, is reaching a value of truth. On its own, a True variable, if it always stays True
is not useful to anyone. Thus, operations and operators are used to _reach_ a certain value that says True or False.

## Comparison Operators in Python

Booleans are essential for creating logical expressions, which are expressions that evaluate to either `True`
or `False`. These expressions are often built using comparison operators, such as `==` (equality), `!=` (
inequality), `<` (less than), `>` (greater than), `<=` (less than or equal to), and `>=` (greater than or equal to).
These operators compare values and return a boolean result.

For example, consider the following code snippet:

```python
x = 5
y = 10

print(x == y)  # False
print(x < y)  # True
print(x > y)  # False
```

In this example, we compare the values of `x` and `y` using the equality (`==`) and less than (`<`) operators. The
results are then printed to the console. As you can see, the expressions evaluate to either `True` or `False` based on
the comparison between the values.

It is important to discern and remember that `=` and `==` can not be used interchangebly.

```python
a = 10  # I am telling python that I want a to be 10
a == 10  # I am asking the computer if a is 10
```

Compound comparison operatios **"a is greater or equals than b"** `>=` are always expressed as:

* `>=` - Greater or equals or
* `<=` - Smaller or equals

* `=>` - equals or greater or `=<` - equals or smaller will not work.

It is also possible to express `**b** is between **a** and **c**` using:

* `a < b < c`
* Equivalent to `a < b and b < c`

### The belonging operator

The operator of belonging `in` is used to check if an element belongs in a sequence or collection, and is expressed
as `element in collection`.

It can be used in the setting of strings, and it would tell if a `string` contains another `string` (also
called `sub-string`).

```python
print('ello' in 'Hello')  # True
print('c' in 'Python')  # False
print('A' in 'asparagus')  # False - Note that `in` is case sensitive.
```

`in` works on any `collection` - but for now, we are going to use it with strings alone.

## Basic decision making

The first and most important function our booleans server in a program is **decision-making**. This introduces us to the
conditional `if` block.

![47a389e4-9067-11ee-9855-9b2ecdf75d65.png](media%2F47a389e4-9067-11ee-9855-9b2ecdf75d65.png)

> The IF block allows us to protect code from being run under certain conditions.

## If and else block

In Python, the `if` and `else` blocks are control structures used to execute different code paths based on specific
conditions. They allow you to make decisions and control the flow of your program based on a boolean value.

Let's take a closer look at how `if` and `else` blocks work in Python.

The `if` statement is used to execute a block of code only if a certain condition is true. It follows this general
syntax:

```python
condition = True
if condition:
    print("I only execute if condition is True")
```

> Please note that by **BLOCKS** we refer to code written after `:` with 1 TAB indentation to the left. Example below.

```python
condition = True
if condition:
    print("I am inside the if block")
    print("I am also code inside the if block")
    print("I am also code inside the if block")
print("I am NOT code inside the if block - I will get executed even if codition is False")
```

Here's an example that demonstrates the usage of an `if` statement:

```python
x = 5

if x > 0:
    print("x is positive")
```

In this code, the condition `x > 0` is checked. If it evaluates to `True`, the code inside the `if` block (the `print`
statement) is executed. Otherwise, if the condition is `False`, the code inside the `if` block is skipped.

You can also include an `else` block along with the `if` statement to specify an alternative code path when the
condition is false. The syntax for using `else` is as follows:

![dee0b5de-9067-11ee-a84b-d7411d9c5cad.png](media%2Fdee0b5de-9067-11ee-a84b-d7411d9c5cad.png)

```python

condition = False
if condition:
    print("I only execute if condition is True")
else:
    print("I only execute if condition is False")

```

Consider the following example:

```python
x = 5

if x > 0:
    print("x is positive")
else:
    print("x is non-positive")
```

In this code, if `x` is greater than 0, the message "x is positive" is printed. Otherwise, if `x` is not greater than
0 (i.e., it is zero or negative), the message "x is non-positive" is printed.

You can also chain multiple conditions together using the `elif` (short for "else if") statement. This allows you to
specify additional conditions to check when the initial condition is false. Here's an example:

```python
x = 5

if x > 0:
    print("x is positive")
elif x < 0:
    print("x is negative")
else:
    print("x is zero")
```

In this code, if `x` is greater than 0, the message "x is positive" is printed. If `x` is not greater than 0, it checks
the next condition `x < 0`. If that condition is true, the message "x is negative" is printed. Finally, if both
conditions are false, the message "x is zero" is printed.

The `if` and `else` blocks provide a powerful way to make decisions and control the flow of your program based on
specific conditions. By using logical expressions and boolean values, you can create complex decision-making structures
to execute different code paths.

## Logical Operators (and, or, not)

Booleans can also be combined using logical operators: `and`, `or`, and `not`. These operators allow you to create more
complex conditions by combining multiple boolean values.

Here's an example that demonstrates the usage of logical operators:

```python
x = 5
y = 10

print(x < 10 and y > 5)  # True
print(x > 10 or y > 20)  # False
print(not x == y)  # True
```

In this code snippet, we use the `and`, `or`, and `not` operators to combine boolean expressions. The `and` operator
returns `True` if both expressions are `True`, the `or` operator returns `True` if at least one expression is `True`,
and the `not` operator negates the boolean value.

This comes especially useful when you want to handle complex situations that are not exactly _black and white_.

For example:

```python
age = int(input())
parents_present = input("Are parents present ? Y/N").upper() == 'Y'

REQ_AGE = 14
if age >= REQ_AGE or parents_present:
    print('You are allowed to see the movie')
else:
    print('You should be at least 14 or be with your parents to see the movie')
```

Negation can be used to avoid situations like this:

```python
daytime = True
if daytime:
    print('Do nothing')
else:
    print('>>Turn on lights!')

## Instead we can do 

if not daytime:
    print('>>Turn on lights')
```

## Truthy

The concept of "**truthy**" refers to values that are considered to be logically **true** when evaluated in a boolean
context. It means that even though a value may not be explicitly `True`, it can still be treated as true in certain
situations.

In Python, the following values are considered "truthy":

- **Any non-zero number**: Any number that is not equal to zero is considered truthy. For example, `1`, `2.5`, `-3`, and
  so
  on.

- **Non-empty sequences** (some will be discussed later): Sequences such as **strings**, **lists**, **tuples**, and *
  *sets** are considered truthy if they contain any elements. For
  example, `"hello"`, `[1, 2, 3]`, `('a', 'b')`, `{1, 2, 3}`.

- **Non-empty mappings** (will be discussed later): Mappings such as dictionaries are considered truthy if they contain
  any
  key-value pairs.

On the other hand, the following values are considered "**falsy**":

- Zero numeric values: The integer `0` and floating-point `0.0` are considered **falsy**.

- Empty sequences: Sequences like empty strings `""`, empty lists `[]`, empty tuples `()`, and empty sets `set()` are
  considered falsy.

- `None`: The special value `None` is considered falsy.

The concept of truthy values is often used in conditional statements, such as `if` and `while` loops, where non-boolean
values are implicitly converted to booleans for evaluation. For example:

```python
x = 5

if x:
    print("x is truthy")
else:
    print("x is falsy")
```

> Run this once with x = 5 and another with x = 0
> Run this again with x = 'Hello' and x = ''

In the code above, the value of `x` is evaluated in the boolean context of the `if` statement. If `x` is truthy (i.e.,
it has
a non-zero value), the message "x is truthy" will be printed. Otherwise, if `x` is falsy (i.e., it is zero or an empty
sequence), the message "x is falsy" will be printed.

Understanding truthy and falsy values allows you to write more expressive and concise code by leveraging the behavior of
implicit boolean conversion. It enables you to perform conditional checks on a wide range of values beyond just the
literal `True` and `False`.

## Combining Conditions

Combining logical expressions and boolean operations in Python allows you to create more complex conditions and perform
advanced decision-making in your code. Python provides several boolean operators that enable you to combine and
manipulate boolean values. Let's explore these operators:

1. Logical AND (`and`): The `and` operator returns `True` if both of its operands are true, and `False` otherwise. It
   follows the short-circuit evaluation, meaning that if the first operand is `False`, the second operand is not
   evaluated. Here's an example:

```python
precipitations = True
temperature = 0

if temperature < 0 and precipitations:
    print('It is snowing')
if temperature > 0 and precipitations:
    print('It is raining')
if temperature < 0 and not precipitations:
    print('It is freezing')
if temperature > 0 and temperature < 10 and not precipitations:
    print('It is cold')
```

In this example, the code inside the `if` block will only execute if both conditions are true.

2. Logical OR (`or`): The `or` operator returns `True` if at least one of its operands is true, and `False` otherwise.
   Similar to `and`, it also follows short-circuit evaluation. Here's an example:

```python
is_allowed = False
IS_ADMIN = True

if is_allowed or IS_ADMIN:
    print('You got access')
```

In this case, the code inside the `if` block will execute if either condition (either `is_allowed` or `IS_ADMIN`) is
true.

3. Logical NOT (`not`): The `not` operator negates the boolean value of its operand. If the operand is `True`, `not`
   returns `False`, and if the operand is `False`, `not` returns `True`. Here's an example:

```python
x = 5

if not x > 10:
    print("x is not greater than 10")
```

In this example, the code inside the `if` block will execute if the condition `x > 10` is false (i.e., `not (x > 10)` is
true).

You can also combine multiple logical expressions and use parentheses to control the order of evaluation. Here's an
example that demonstrates complex condition combining:

```python
x = 5
y = 10
z = 15

if (x > 0 and y > 0) or z < 20:
    print("Condition is true")
```

In this code, the expression `x > 0 and y > 0` is evaluated first, and then the result is combined with `z < 20` using
the `or` operator.

By combining logical expressions and boolean operations, you can create intricate conditions to make decisions based on
multiple criteria in your code. It's a powerful way to control the flow and behavior of your program.

### Practice


