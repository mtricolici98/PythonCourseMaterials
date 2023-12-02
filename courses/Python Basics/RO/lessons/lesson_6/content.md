## What are conditionals?

Conditional statements are fundamental building blocks in programming that allow you to make decisions based on certain conditions. They enable your program to execute different blocks of code depending on whether a given condition is true or false. Conditional statements in Python include `if`, `elif`, and `else`.

## If and Else:

The `if` statement is used to execute a block of code only if a certain condition is true. The code block following the `if` statement is executed if the condition is evaluated as true. Here's an example:

```python
age = 20

if age >= 18:
    print("You are eligible to vote.")
```

Output:
```
You are eligible to vote.
```

The `else` statement can be added to specify a block of code that should be executed if the condition in the `if` statement is false. Here's an example:

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

## Elif (else if):

The `elif` statement allows you to check for multiple conditions. It is useful when you have more than two possibilities. The code block following the `elif` statement is executed if the corresponding condition is true. Here's an example:

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

In this example, if the `age` variable is greater than or equal to 18, the first message will be printed. If it's 17, the second message will be printed. Otherwise, the third message will be printed.

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

In this example, the outer `if` statement checks if the `age` is greater than or equal to 18. If that condition is true, it enters the nested `if` statement, which checks if the `income` is greater than 30000. If both conditions are true, the message "You are eligible for a loan" is printed.

If the outer `if` condition is false (i.e., if the age is less than 18), the code proceeds to the `else` block, which prints the message "You are not old enough to apply for a loan."

Nested `if` statements can be useful in scenarios where you need to evaluate multiple conditions in a hierarchical manner, with different levels of checks and actions based on the outcome of each condition. However, as the level of nesting increases, the code can become more complex and harder to read and maintain. In such cases, using logical operators like `and`, `or`, and `not` can often lead to cleaner and more readable code.


Logical operators such as `and`, `or`, and `not` can be used to combine multiple conditions in a single statement. They provide a way to express complex conditions without using nested `if` statements.

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

In this example, both conditions `age >= 18` and `income > 30000` must be true for the loan eligibility message to be printed.

Logical operators can also be combined with `if`, `elif`, and `else` statements to create more complex decision-making structures.

Using logical operators is generally preferred over using nested `if` statements, as it makes the code more readable and easier to understand.
