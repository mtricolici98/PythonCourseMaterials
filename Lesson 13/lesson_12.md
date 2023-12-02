# Functions continued

## Importing functions from other files

Python allows importing values, functions and other things from different files.

This is best explained with an example.

Let's create a file:

functions.py

````python
# functions.py
def smiley_function(text, smiley_face=':)'):
    print(f'{smiley_face} {text}')
````

In the file above we have a function, that we may want to use across different python files.

In python, there are two ways to import stuff (objects, variables, functions):

1. Importing the entire module using the **import** keyword
2. Importing the specific function/object/variable, using **from** _module_ **import** _function_name_

To continue let's create another file.

program.py (or whatever you like)

Example: Importing the entire module

```python
# program.py

import functions

functions.smiley_function('I am running a function from a different file')
```

The above code, will import the entire functions.py module into the current python script.

Example 2: Importing the function alone

```python
# program.py

from functions import smiley_function

smiley_function('I am running a function from a different file')
```

The example above only imports the **smiley_function** from the functions **module**

### Importing multiple functions from the same module.

If we want to add more functions in our **functions.py** file, we can easily do so.

```python
# functions.py
def smiley_print_function(text, smiley_face=':)'):
    print(f'{smiley_face} {text}')


def number_input_function():
    user_inpt = input('Please type a whole number: ')
    if user_inpt.isnumeric():
        return int(user_inpt)
    else:
        return smiley_print_function('I asked for a whole number')
```

And if we want to import more than one function using the **from ... import** syntax, we can do so by separating the
function names by comma (**,**).

```python
# program.py
from functions import smiley_print_function, number_input_function
```

### What is a module

Modules are simply **.py** files that can be imported into other **.py** files. We can look at them as libraries that
contains various functions we want to use in multiple places (programs/scripts)

You can have an entire folder that acts as a module. This is what is called a package.

As our project will grow more and more complex, we will start seeing submodules/packages more often.

## Declaring a package

As I said, a package is a folder that contains multiple **.py** files or other packages.

Let's say we have a structure like below

````
Project
|---project_utils
|   |---__init__.py
|   |---database_utils.py
|   |---datetime_utils.py
|---services
|   |---__init__.py
|   |---database_service.py
|   |---file_utils.py
|---main.py
````

Our program logic may be in **main.py**

Inside **main.py** we might want to access some of our utils and services

````python
# main.py

from project_utils.database_utils import process_query_result
from services.database_service import query_database


def main():
    query_result = query_database(...)
    result_list = process_query_resullt(query_result)
````

## The __ init __ file

The init file is an optional (as of python 3.6) file that declares that the folder is a python module.

The init files are mostly used to provide "shortcuts" to functions or sub-modules inside our module

For example:

```python
# Project.services.__init__.py
# Importing functions from database_service module into the root of the package for easier access
from database_service import query_database, create_databse, create_table, delete_table, delete_database

```

Now, because our __init__ file imports functions from the **database_service**, we can access them directly from the
**services** module.

```python
# Now we can do this, because the services package already imports the functions from the database_service
from services import query_database
# Instead of this
from services.database_service import query_database
```

The init file can also be used to initialize some common logic in the package.

For example, in our services' init file we might want to create check if a folder to store program files is available
and create it if it isn't, we might also establish a database connection

```python
# Project.services.__init__.py

from database_service import *
from file_utils import *

# Doing initialization logic for our package

# Checking if database exists
if not database_exists('DEFAULT_DATABASE'):
    # creating database
    create_database('DEFAULT_DATABASE')

# Checking if folder for files exists
if not folder_exists('program_files'):
    # Creating folder
    create_folder('program_files')
```

You must be careful with the initialization logic for a package, because it will run every time the package is imported.

### name == main

Remember ``if __name__ == __main__: `` ?

Well, here is where it comes in as very important.

If our functions.py file has any code that runs inside the script. It will also be evaluated during the import.

```python
# functions.py
def smiley_function(text, smiley_face=':)'):
    print(f'{smiley_face} {text}')


smiley_function('Testing my function')
```

If we now import the **functions** module, the smiley_function **call** inside the module will be executed.

```python
import functions  # Will print ':) Testing my function'
```

In order to fix this, we use ``__name__ == '__main__'``

This will check, that the code is evaluated not as part of an import but as part of the script execution.

````python
# functions.py
def smiley_function(text, smiley_face=':)'):
    print(f'{smiley_face} {text}')


if __name__ == '__main__':
    smiley_function('Testing my function')
````

Now if we import the functions' module, the **smiley_function** inside **functions** module will not be executed.

But if we run the functions.py program, it will still display **':) Testing my function'**

### Importing multiple functions/values with same name

Say you have 2 functions in different packages that have the same name

functions.py

```python
def factorial(nr):
    pass  # Implement factorial here
```

main.py

```python
from functions import factorial
from math import factorial
```

Above we have imported 2 functions with the name factorial. This means that only the lower function will be used.

If you want to use both functions separately you can give the function a nickname. Using the keyword **as**

```python
from functions import factorial as my_factorial
from math import factorial as math_factorial
```

### Don't worry about imports yet

Imports are very important in working with small to large programs, but you don't have to worry, because most of the
time, your IDE will help you with them.

# Errors

## What we've learned

We've learned about data types, collections and ways to work with them, functions and ways to build them.

Now is the time we learn on how to make our program, interface with our computer.

We will also discuss, how to handle unexpected errors, and how to make and handle expected errors.

## Exceptions (errors)

Exceptions are a part of a program that tell the user, the system and the program that something has gone wrong.

Exceptions are an essential part of a developers' toolkit, as it allows him to easily communicate that something
unexpected happened.

Exceptions are a way to communicate to other parts of the program that "Something happened that wasn't supposed to
happen"

But sometimes, we don't want Exceptions. Sometimes, we want to ignore them, or to ask the user to try again.

We could check everything everywhere with **if** statements to avoid having Exceptions, but that would be very
counter-productive. Instead, we can let Exceptions happen, and deal with them.

### Error handling

In python errors are handled using a **try: except:** block.

Try-Except blocks are similar to **if: else:** blocks

The code inside **try** will complete if there are no errors and the code inside **except** will execute only if there
is an error inside the **try** block

Example

```python
try:
    print('Some random String' + 120)
except:
    print('Error happened but I am still running')
```

### Excepting the expected

We can declare what kind of error we expect to happen, in order to handle that exact error

Example below.

```python
try:
    print(int(input('Input a number')))
except ValueError:
    print(f"User didnt input a valid number")
```

It's also possible to except any error. This is done by excepting **Exception**

````python
try:
    print(int(input('Input a number')))
except Exception:
    print(f"Something didnt go to plan")
````

### Finding out what the error was

You can use the **as** keyword to keep the instance of the error (exception) inside a variable.

To use **as** you **must** declare the type of the exception.

Most exception in python are derived from the **Exception** class. This means that if you try to except **Exception**,
you will most probably catch all of them.

```python
try:
    print('Some random String' + 120)
except Exception as error:
    print(f"Failed with error: {str(error)}")
```

### When is this useful ?

For example, you may need to use an external service, the quality or reliability of which you can never trust.

In that case, you may want to retry a couple of times, or use a fallback, or perhaps notify someone that something went
wrong.

Simple example: Assuring user inputs a float value

```python
def convert_to_float(string):
    try:
        return float(string)
    except ValueError:
        return None  # User input was not a float string


def main():
    maybe_number = None
    while maybe_number is None:
        maybe_number = convert_to_float(input('Input a numeric value'))
        if maybe_number is not None:
            print(f'Thanks for {maybe_number}')
        else:
            print(f'Try to input a number this time')


```

A more complex example: Trying to connect to an external service multiple times

```python
# This code is an example and is not functional
def get_connection_to_aws(max_retries):
    retries = 0
    connection = None
    while retries < max_retries:
        try:
            connection = connect_to_amazon_service(CONN_URL, CONN_KEY)  # Example Fucntion
            return connection
        except Exception as ex:
            print(f'Connection failed, reason: {str(ex)}')
            retries += 1
    if connection is None:
        send_mails_to_admin(str(ex))
```

### Avoid broad exceptions

The **except** statement allows the developer to specify what kind of exceptions the except block should handle.

This is usually more than just a suggestion. If the except statement is too broad, you may handle exception that were
never meant to be handled.

Not specifying an exception, will let the code run even if the exception is a system event. For example a keyboard
interrupt. Which should close any application.

```python
try:
    number = int(input('Enter A number'))
    result = 10 / number
except:  # VERY BAD Because we don't know what exactly failed
    pass  # Code
```

```python
try:
    number = int(input('Enter A number'))
    result = 10 / number
except ArithmeticError as err:  # Much better
    pass  # Code
```

Thankfully the IDE will warn you about the broad exceptions, but still, be on the lookout.

### Exceptions are only handled when encountered

This means that any code inside the **try** block will run until it encounters the error.

```python
try:
    print('Printing something')
    print('Printing something else')
    print(10 / 0)
    print('Printinng at the end')
except ZeroDivisionError:
    print('Exception handled')
# Printing something
# Printing something else
# Exception handled
```

The code in the try block will only run until it encounters the error

### Finally

Fundamentally, **try:except** blocks work similar to this.

```
# Run code 
if errror:
    # Run execept block
```

But they also provide a **finally** block. What is it for ?

````python
def convert_to_float():
    value = None
    try:
        value = float(input('Input a float'))
    except ValueError as ex:
        print(f"User invalid input: {str(ex)}")
    finally:
        return value
````

In the **finally** block, programmers usually do "clean-up". So they remove all that's left after either a successful or
a failed try:except execution.

Example:

```python
try:
    make_database_query(database, query)  # Trying to make a query against this database
except Exception as ex:
    print(f"Database had a problem: {str(ex)}")  # Database Failed to make query
finally:
    close_database_connection(database)  # Close connection to database, even if the query failed
```

### Raising Exceptions

Raising (or creating) an exception can be done using the **raise** keyword, and allows us to create errors anywhere in
our code.

All exceptions have a standard body that can contain the message.

```python
def find_index(list_to_lookup, item_to_find):
    for index in range(len(list_to_lookup)):
        if list_to_lookup[index] == item_to_find:
            return index
    raise Exception('Item not found')


try:
    find_index([1, 2, 3], 4)
except Exception as ex:
    print(str(ex))  # Ooops, Something went wrong...
```

### Types of exceptions.

All exceptions extend **BaseException**. So if you try to except BaseExecution, you will _catch them all_.

This is never a good thing, but nonetheless. You are also capable of extending and making your own exceptions.

But it is recommended to extend **Exception**.

```python
class MyCustomException(Exception):
    pass  # We don't need a body
```

### Raising Custom exceptions

```python
class ItemNotFoundError(Exception):
    pass  # We don't need a body


def find_index(list_to_lookup, item_to_find):
    for index in range(len(list_to_lookup)):
        if list_to_lookup[index] == item_to_find:
            return index
    raise ItemNotFoundError('Item not found')


try:
    find_index([1, 2, 3], 4)
except ItemNotFoundError as ex:
    print(f'Item was not found')
```

### Catching multiple exceptions

You can catch multiple exceptions, not just one, and it can be done in two ways, grouping them in one **except** block,
or having one separate **except** block for each.

```python
try:
    a = int(input('a'))
    b = int(input('b'))
    print(a / b)
except ZeroDivisionError as ex:
    print('Didn\'t you go to school')
except ArithmeticError as ex:
    print('Thoose numbers don\'t make sense')
except ValueError as ex:
    print("One of the values provided is not a number")
except Exception as ex:
    print("I don't know what happened, but I know it's bad...")
```

The **above** example will execute a specific except block, based on the type of the exception that was raised.

```python
try:
    a = int(input('a'))
    b = int(input('b'))
    print(a / b)
except (ZeroDivisionError, ArithmeticError) as ex:
    print('Thoose numbers don\'t make sense')
except Exception as ex:
    print("I don't know what happened, but I know it's bad...")
```

You can also provide a tuple of Exception classes, that one except block will catch.

#### Note: The order of exception matters, same as with elif blocks.
