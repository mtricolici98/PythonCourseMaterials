## The datetime module

Python's `datetime` module is a powerful library for handling dates and times. It provides classes and functions to
manipulate, format, and perform operations on dates and times. In this article, we will explore various aspects of
the `datetime` module, covering topics such as `DateTime` objects, `TimeDelta` objects, operations between them,
formatting options, parsing formatted datetime, and handling time zone information.

## The DateTime Object

The `datetime` module introduces the `datetime` class, which represents a date and time. It allows you to work with both
the date and time components. Let's create a `DateTime` object:

```python
from datetime import datetime

# Current date and time
current_datetime = datetime.now()
print("Current DateTime:", current_datetime)

# Creating a specific DateTime
specific_datetime = datetime(2022, 1, 1, 12, 30, 0)
print("Specific DateTime:", specific_datetime)
```

In the above example, we use `datetime.now()` to get the current date and time and create a specific `DateTime` object
using the `datetime` class.

> Note: Be careful when importing datetime

There is a `datetime` module in the `datetime` package.

`import datetime` will import just the package, and not the `datetime` object we need to work with DateTime.

## The TimeDelta Object

The `TimeDelta` class represents the difference between two dates or times. It allows us to perform arithmetic
operations on `DateTime` objects. Here's an example:

```python
from datetime import datetime, timedelta

# Create two DateTime objects
start_time = datetime(2022, 1, 1, 10, 0, 0)
end_time = datetime(2022, 1, 1, 12, 30, 0)

# Calculate the time difference
time_difference = end_time - start_time
print("Time Difference:", time_difference)
```

In this example, we create two `DateTime` objects and subtract them to obtain a `TimeDelta` object representing the time
difference between them.

## Operations between DateTime Objects

The `datetime` module supports various operations between `DateTime` objects, such as subtraction and comparison
operations.

Let's explore these operations:

```python
from datetime import datetime

# Create two DateTime objects
start_time = datetime(2024, 1, 10, 10, 0, 0)
other_time = datetime(2024, 1, 12, 10, 0, 0)

# Subtract one from the other
new_time = other_time - start_time
print("Difference between start and other_time is:", new_time)

print(start_time > other_time)  # False
print(start_time < other_time)  # True
print(start_time == other_time)  # False
```

## Operations between DateTime and TimeDelta Objects

We can also perform operations directly between `DateTime` and `TimeDelta` objects without explicitly creating a
new `DateTime` object.

We can create `timedelta` objects directly, using the `timedelta` constructor, to manipulate our dates.

Here's an example:

```python
from datetime import datetime, timedelta

# Create a DateTime object
start_time = datetime(2022, 1, 1, 10, 0, 0)

# Create a TimeDelta object
delta = timedelta(hours=2, minutes=30)

# Add TimeDelta to DateTime
new_time = start_time + delta
print("New DateTime after addition:", new_time)

# Subtract TimeDelta from DateTime
new_time_back = start_time - delta
print("New DateTime after subtraction:", new_time_back)
```

This example demonstrates that the result of adding or subtracting a `TimeDelta` from a `DateTime` object is a
new `DateTime` object.

## DateTime Formatting and Formatting Options

When working with dates in our program, we often want to show our datetime information in a nice, human-readable format.

The `strftime` method is used for this purpose. Let's see how to format a `DateTime` object:

```python
from datetime import datetime

# Create a DateTime object
current_datetime = datetime.now()

# Format DateTime to a string
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted DateTime:", formatted_datetime)
```

In this example, `%Y`, `%m`, `%d`, `%H`, `%M`, and `%S` are format codes representing the year, month, day, hour,
minute, and second, respectively.

We can use other formats to represent dates and times, for example, we can show our dates in a even nicer fashion using
other formatting parameters:

```python
from datetime import datetime

print(datetime(2024, 1, 1, 22, 00).strftime('%A, %d %B, %Y, %I:%M %p'))
```

In the example above, `%A` is Full weekday name, `%B` is the full month name, `%I` is the hour in 12-hour format
and `%p` is AM/PM.

You can see more examples and formats [here](https://www.programiz.com/python-programming/datetime/strftime).

Please note that any other characters that do not start with `%` will be written (formatted) into the result literally.

### Why format ?

Formatting your date-time is crucial not only to display your date-time but also to serialize the datetime information.

If we try to save a date-time to a JSON file, we will quickly notice that it will not work.

```python
from datetime import datetime
import json

json.dumps(datetime.now())  # Raises TypeError: Object of type datetime is not JSON serializable
```

Formatting comes to help, as we can safely store strings into JSON files.

```python
from datetime import datetime
import json

json_string = json.dumps(
    dict(date=datetime(2024, 1, 1, 22, 10).strftime('%Y-%m-%d %H:%M:%S'))
)
print(json_string)  # {"date": "2024-01-01 22:10:00"}
```

## Parsing Formatted DateTime to an Object

Conversely, you may need to convert a formatted string into a `DateTime` object. The `strptime` method is used for this
purpose.

The `strptime` method does the exact opposite of what `strftime` does, converting a string datetime to a `datetime`
object.

To achieve this, we need the string we pass to match the format we are specifying.

Here, we provide the format of the string using the same format codes as in the `strftime` method.

```python
from datetime import datetime

# Parse a formatted string to DateTime
date_string = "2022-01-01 12:30:00"
parsed_datetime = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print("Parsed DateTime:", parsed_datetime)
# Passing incomplete formats or incomplete date string will raise ValueErrors...
parsed_datetime = datetime.strptime(date_string, "%Y-%m-%d %H:%M")  # Raises: ValueError: unconverted data remains: :00
print("Parsed DateTime:", parsed_datetime)
```

This, similarly to our `strftime` example, allows us to easily extract precise date information and store it as an
object to do data manipulation.

```python
from datetime import datetime

# Parse a formatted string to DateTime
birthday = "30/01/1998"
# Using 3rd party module for better timedelta
from dateutil.relativedelta import relativedelta

delta = relativedelta(datetime.now(), datetime.strptime(birthday, '%d/%m/%Y'))
print(delta.years)
```

In the example above we used another module called `relativedelta` from the package `dateutil`.

This provides additional handling, as timedelta is only limited **days**, **seconds**, **minutes**.

## 7. Handling Time Zone Information

Dealing with time zones is crucial when working with dates and times. The `pytz` library is commonly used for time zone
support in Python:

```python
from datetime import datetime
import pytz

# Create a DateTime object with time zone information
dt_with_tz = datetime(2022, 1, 1, 12, 0, 0, tzinfo=pytz.UTC)
print("DateTime with Time Zone:", dt_with_tz)

# Convert DateTime to a different time zone
new_tz = pytz.timezone("America/New_York")
dt_ny = dt_with_tz.astimezone(new_tz)
print("DateTime in New York Time Zone:", dt_ny)

chisinau_tz = pytz.timezone('Europe/Chisinau')
dt_chisinau = dt_with_tz.astimezone(chisinau_tz)
print(dt_chisinau)
```

In this example, we create a `DateTime` object with time zone information and then convert it to a different time zone
using the `astimezone` method.

Timezones are important for large scale apps that run in different countries or on different continents.

You don't want your Photo, posted at 12:00 in Chisinau to show up as posted in the **future** on in some
different country.

Usually applications stick to one **main** timezone, and adjust the datetime based on the timezone of the user (
similarly to how we do it above).

## Conclusion

Mastering the `datetime` module is essential for any Python developer working with dates and times. The module provides
powerful tools for creating, manipulating, and formatting date and time objects. By understanding the concepts covered
in this article, you'll be well-equipped to handle a wide range of scenarios involving dates and times in your Python
applications.
