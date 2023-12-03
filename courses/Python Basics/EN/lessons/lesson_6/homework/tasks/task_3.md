Improve the password generator

Improve the password generator below, such as it is able to generate passwords that also contain numbers and special
characters.

```python
import string
import random

all_letters = list(string.ascii_letters)
print(all_letters)
pass_length = int(input('Pass length'))

password = ''
for a in range(pass_length):
    letter_index = random.randrange(0, len(all_letters))
    password += all_letters[letter_index]
    print(password)
```

> Note: random.randrange(0, x) will generate a single random number from a to x
>
> Note: the string module may also have other useful characters information
