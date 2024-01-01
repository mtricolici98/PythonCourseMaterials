For this homework your solution should contain both the function, and the ways you use the function in the the same
solution.

Example:

```python
def my_solution(arg1, arg2):
    pass


# test1
i1, i2 = input(), input()
sol_result = my_solution(i1, i2)
print(f"Result for {i1}, {i2} is {sol_result}")
# test2
print(my_solution('a', 'c'))
```

Please note that your functions must do **one thing, and do it well**, this means:

* Your function should return the result, instead of displaying it using pring (Have separate tests for displaying the
  result)
* Should use all the necessary information from arguments: Instead of using `input` inside the function, use it outside,
  and pass the value as an argument.

### Correct:

```python
def adder(a, b):
    return a + b


nr1 = int(input('a:'))
nr2 = int(input('b:'))

print(f"Result is {adder(nr1, nr2)}")
```

### Incorrect:

```python
def adder():
    a = int(input('a:'))
    b = int(input('b:'))
    print(f"Result is {a + b}")


adder()
```


