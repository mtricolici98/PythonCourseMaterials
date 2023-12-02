# Booleans and Boolean Logic

## What are booleans ? 

In Python, a boolean is a data type that represents one of two possible values: True or False. Booleans are commonly used in programming for making decisions, controlling the flow of a program, and determining conditions.

## Comparison Operators in Python

Booleans are essential for creating logical expressions, which are expressions that evaluate to either `True` or `False`. These expressions are built using comparison operators, such as `==` (equality), `!=` (inequality), `<` (less than), `>` (greater than), `<=` (less than or equal to), and `>=` (greater than or equal to). These operators compare values and return a boolean result.

For example, consider the following code snippet:

```python
x = 5
y = 10

print(x == y)  # False
print(x < y)   # True
print(x > y)   # False
```

In this example, we compare the values of `x` and `y` using the equality (`==`) and less than (`<`) operators. The results are then printed to the console. As you can see, the expressions evaluate to either `True` or `False` based on the comparison between the values.

## If and else block

In Python, the `if` and `else` blocks are control structures used to execute different code paths based on specific conditions. They allow you to make decisions and control the flow of your program based on a boolean value.

Let's take a closer look at how `if` and `else` blocks work in Python.

The `if` statement is used to execute a block of code only if a certain condition is true. It follows this general syntax:

```python
if condition:
    # Code to execute if the condition is true
```

Here's an example that demonstrates the usage of an `if` statement:

```python
x = 5

if x > 0:
    print("x is positive")
```

In this code, the condition `x > 0` is checked. If it evaluates to `True`, the code inside the `if` block (the `print` statement) is executed. Otherwise, if the condition is `False`, the code inside the `if` block is skipped.

You can also include an `else` block along with the `if` statement to specify an alternative code path when the condition is false. The syntax for using `else` is as follows:

```python
if condition:
    # Code to execute if the condition is true
else:
    # Code to execute if the condition is false
```

Consider the following example:

```python
x = 5

if x > 0:
    print("x is positive")
else:
    print("x is non-positive")
```

In this code, if `x` is greater than 0, the message "x is positive" is printed. Otherwise, if `x` is not greater than 0 (i.e., it is zero or negative), the message "x is non-positive" is printed.

You can also chain multiple conditions together using the `elif` (short for "else if") statement. This allows you to specify additional conditions to check when the initial condition is false. Here's an example:

```python
x = 5

if x > 0:
    print("x is positive")
elif x < 0:
    print("x is negative")
else:
    print("x is zero")
```

In this code, if `x` is greater than 0, the message "x is positive" is printed. If `x` is not greater than 0, it checks the next condition `x < 0`. If that condition is true, the message "x is negative" is printed. Finally, if both conditions are false, the message "x is zero" is printed.

The `if` and `else` blocks provide a powerful way to make decisions and control the flow of your program based on specific conditions. By using logical expressions and boolean values, you can create complex decision-making structures to execute different code paths.


## Logical Operators (and, or, not)

Booleans can also be combined using logical operators: `and`, `or`, and `not`. These operators allow you to create more complex conditions by combining multiple boolean values.

Here's an example that demonstrates the usage of logical operators:

```python
x = 5
y = 10

print(x < 10 and y > 5)  # True
print(x > 10 or y > 20)  # False
print(not x == y)        # True
```

In this code snippet, we use the `and`, `or`, and `not` operators to combine boolean expressions. The `and` operator returns `True` if both expressions are `True`, the `or` operator returns `True` if at least one expression is `True`, and the `not` operator negates the boolean value.

## Truthy

The concept of "truthy" refers to values that are considered to be logically true when evaluated in a boolean context. It means that even though a value may not be explicitly `True`, it can still be treated as true in certain situations.

In Python, the following values are considered "truthy":

- Any non-zero number: Any number that is not equal to zero is considered truthy. For example, `1`, `2.5`, `-3`, and so on.

- Non-empty sequences (some will be discussed later): Sequences such as strings, lists, tuples, and sets are considered truthy if they contain any elements. For example, `"hello"`, `[1, 2, 3]`, `('a', 'b')`, `{1, 2, 3}`.

- Non-empty mappings (will be discussed later): Mappings such as dictionaries are considered truthy if they contain any key-value pairs.

On the other hand, the following values are considered "falsy":

- Zero numeric values: The integer `0` and floating-point `0.0` are considered falsy.

- Empty sequences: Sequences like empty strings `""`, empty lists `[]`, empty tuples `()`, and empty sets `set()` are considered falsy.

- `None`: The special value `None` is considered falsy.

The concept of truthy values is often used in conditional statements, such as `if` and `while` loops, where non-boolean values are implicitly converted to booleans for evaluation. For example:

```python
x = 5

if x:
    print("x is truthy")
else:
    print("x is falsy")
```

In this code, the value of `x` is evaluated in the boolean context of the `if` statement. If `x` is truthy (i.e., it has a non-zero value), the message "x is truthy" will be printed. Otherwise, if `x` is falsy (i.e., it is zero or an empty sequence), the message "x is falsy" will be printed.

Understanding truthy and falsy values allows you to write more expressive and concise code by leveraging the behavior of implicit boolean conversion. It enables you to perform conditional checks on a wide range of values beyond just the literal `True` and `False`.

## Combining Conditions

Combining logical expressions and boolean operations in Python allows you to create more complex conditions and perform advanced decision-making in your code. Python provides several boolean operators that enable you to combine and manipulate boolean values. Let's explore these operators:

1. Logical AND (`and`): The `and` operator returns `True` if both of its operands are true, and `False` otherwise. It follows the short-circuit evaluation, meaning that if the first operand is `False`, the second operand is not evaluated. Here's an example:

```python
x = 5
y = 10

if x > 0 and y < 20:
    print("Both conditions are true")
```

In this example, the code inside the `if` block will only execute if both conditions (`x > 0` and `y < 20`) are true.

2. Logical OR (`or`): The `or` operator returns `True` if at least one of its operands is true, and `False` otherwise. Similar to `and`, it also follows short-circuit evaluation. Here's an example:

```python
x = 5
y = 25

if x > 10 or y < 20:
    print("At least one condition is true")
```

In this case, the code inside the `if` block will execute if either condition (`x > 10` or `y < 20`) is true.

3. Logical NOT (`not`): The `not` operator negates the boolean value of its operand. If the operand is `True`, `not` returns `False`, and if the operand is `False`, `not` returns `True`. Here's an example:

```python
x = 5

if not x > 10:
    print("x is not greater than 10")
```

In this example, the code inside the `if` block will execute if the condition `x > 10` is false (i.e., `not (x > 10)` is true).

You can also combine multiple logical expressions and use parentheses to control the order of evaluation. Here's an example that demonstrates complex condition combining:

```python
x = 5
y = 10
z = 15

if (x > 0 and y > 0) or z < 20:
    print("Condition is true")
```

In this code, the expression `x > 0 and y > 0` is evaluated first, and then the result is combined with `z < 20` using the `or` operator.

By combining logical expressions and boolean operations, you can create intricate conditions to make decisions based on multiple criteria in your code. It's a powerful way to control the flow and behavior of your program.
