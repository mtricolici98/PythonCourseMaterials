## dict

Dict - short for Dictionary is another type of collection. **The biggest difference from a list is that in a dict, the values are not accessed by the index but by a 'key'.** This means that instead of using a numeric index to retrieve a value, you use a specific key associated with that value.

You can think of a dictionary as a collection of key-value pairs. Each pair consists of a **key** and a **value**. The key serves as a unique identifier for the corresponding value.

Dictionary keys can be of any immutable type, such as strings, numbers, or tuples. On the other hand, dictionary values can be of any type, including dictionaries themselves. This flexibility allows dictionaries to represent complex and hierarchical data structures.

Dictionaries are particularly useful for storing and retrieving data because they guarantee that a given value is always going to be accessible at a given key. This makes dictionary lookup very efficient, especially when you know the key you're looking for.

### How to define a dict

Dicts can be defined in two ways.

1. By calling the constructor `dict()`. You can create an empty dictionary using the constructor, or you can pass key-value pairs to create a non-empty dictionary.

   ```python
   my_dict = dict()  # Empty dict using constructor
   my_not_empty_dict = dict(my_key='My value')  # Non-empty dict using constructor
   ```

2. By using the curly brackets `{}` (similar to sets) and separating the key and value with a colon `:`.

   ```python
   my_dict = {'my_key': 'My value'}
   ```

### Why use dicts

Dicts offer a convenient way to store dynamic data. For example, you can use a dictionary to store information about a person, such as their name, age, profession, and hobbies.

```python
me = {
    'name': "My name",
    'age': 20,
    'profession': 'Policeman',
    'hobbies': ['Music', 'Reading sport books', 'Finding purpose in life']
}
```

Using dictionaries allows you to organize and access multiple pieces of information easily, whether it's within your program or when storing data in a file or database. Dictionaries act as dynamic objects that can be modified and expanded at runtime, providing great flexibility.

### Working with dicts

Dictionaries behave like a combination of sets and lists.

Values in sets can be iterated over, have a length, and can be accessed using square brackets like a list. Similarly, dictionaries have a length that represents the number of key-value pairs it contains.

```python
my_dict = {1: 'A', 'two': 'TWO', 'a': 3}
len(my_dict)  # 3
```

#### What can be inside a dict?

Dict **values** can be of any type, including other dictionaries. This allows you to create complex data structures by nesting dictionaries within dictionaries.

Dict **keys** should be an immutable data type to ensure that they can be used as unique identifiers.

#### Accessing values

Accessing values in a dictionary is done by specifying the key associated with the desired value. If the key is not present in the dictionary, an error will be raised.

```python
my_dict = {'my_key': 'My value'}
print(my_dict['my_key'])  # My value
```

#### Adding/Changing values

To add or change values in a dictionary, you can assign a value to a new key to add a new key-value pair, or you can assign a value to an existing key to update its value. If a key does not exist during assignment, it will be created.

```python
my_dict = {'my_key':

 'My value'}
my_dict['my_other_key'] = 'My other value'
print(my_dict['my_other_key'])  # My other value
```

It's important to note that values in a dictionary can be passed directly or as references to objects.

## Object references

In Python, assigning the value of one **mutable** variable to another variable will create another reference to the same value. This means that changes made to one variable will affect the other variable as well.

```python
some_list = [1, 2, 3]
also_some_list = some_list
```

In the example above, both `some_list` and `also_some_list` now refer to the same list object. If you modify the list using either variable, the list itself will be updated.

```python
some_list = [1, 2, 3]
also_some_list = some_list
also_some_list.append(4)
print(some_list)  # [1, 2, 3, 4]
```

To avoid unintentional modifications, you need to handle object references with care, especially when working with mutable objects like lists and dictionaries.

### Cloning

Immutable data types are cloned by default when they are assigned to a new variable. This means that a copy of the value is created, and modifying one variable does not affect the other.

If you want to make a clone of a mutable data type (e.g., a list), you can use the list constructor `list()` or the `.copy()` method of the list.

```python
some_list = [1, 2, 3]
some_list_clone = list(some_list)
also_clone = some_list.copy()
some_list_clone.append(4)
print(some_list)  # [1, 2, 3]
print(some_list_clone)  # [1, 2, 3, 4]
print(also_clone)  # [1, 2, 3]
```

By creating a clone, you can work with a separate copy of the mutable object and modify it independently.

## Iteration

Iteration through a dictionary is possible, and it returns the keys of the dictionary. You can then use the keys to access the corresponding values.

```python
my_dict = {'first': 1, 'second': '2', 'third': [1, 2, 3]}
for key in my_dict:
    print(my_dict[key])
# 1
# 2
# [1, 2, 3]
```

#### Values or Keys only

It's possible to iterate only through the keys or the values of a dictionary using the `.keys()` and `.values()` methods, respectively.

```python
my_dict = {1: 'one', 2: 'two', 3: 'three'}
for key in my_dict.keys():
    print(key)
# 1
# 2
# 3
for value in my_dict.values():
    print(value)
# one
# two
# three
```

### Dicts can be nested

Yes, you can have a dictionary inside another dictionary, as many levels deep as you need. This is useful when you want to create flexible data structures that can accommodate changing requirements.

```python
flights = {
    'Air Moldova': {
        'Incoming': [dict(number='AA1110', source='Frankfurt, DE', destination='Chisinau, MD')],
        'Outgoing': [dict(number='OB1110', source='Chisinau, MD', destination='Milan, IT')],
    }
}
```

While manually creating nested dictionaries can be cumbersome, working with them programmatically provides greater convenience and flexibility. You can access

 and manipulate nested values using their corresponding keys.

For example, to print a list of all incoming flights from Air Moldova:

```python
for flight in flights['Air Moldova']['Incoming']:
    print(flight['number'], flight['source'], flight['destination'])
```

#### Items

You can also access both the keys and the values of a dictionary simultaneously using the `.items()` method, which returns a sequence of key-value pairs.

```python
my_dict = {1: 'one', 2: 'two', 3: 'three'}
for key, value in my_dict.items():
    print(f'Key: {key}, Value: {value}')
# Key: 1, Value: one
# Key: 2, Value: two
# Key: 3, Value: three
```

The `.items()` method is useful when you need to work with both the keys and the values within a loop.

## Unpacking

**Unpacking** in Python refers to the process of extracting individual values from a collection. It allows you to assign multiple variables in a single line of code.

Let's try unpacking on tuples first.

Tuples are ideal for unpacking because they have a fixed size, so you always know how many elements to expect. However, you can also use unpacking with lists, although the number of variables must match the size of the list.

```python
my_tuple = (10, 20)
# Unpack the tuple into variables a and b
a, b = my_tuple
print(a)  # 10
print(b)  # 20
```

Here's an example of unpacking more than two values:

```python
some_tuple = (10, 30, 'Yes')
width, height, condition = some_tuple
```

However, it's important to note that attempting to unpack a different number of values than the size of the tuple or list will raise an error.

```python
tup = (10, 12)
a, b, c = tup  # Raises an error
```

Unpacking can be performed on collections of any size, but be mindful of the readability and maintainability of your code when unpacking large collections.

## The `in` keyword: Checking for membership in a collection

For dictionaries, the `in` keyword checks for membership among the keys by default.

```python
my_dict = dict(a=1, b=2, c=3)
print('d' in my_dict)  # False
print('c' in my_dict)  # True
print(3 in my_dict)  # False
print(3 in my_dict.values())  # True
```

You can use the `in` keyword to check if a certain key exists in a dictionary. Additionally, you can also use the `in` keyword with the `values()` method to check for the presence of a value within the dictionary.