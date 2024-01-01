# Email Validator

Write a Python function called `is_valid_email` that validates the format of a given email address. The function should
take one argument: `email` (string) representing the email address to be validated. The function should return a boolean
value indicating whether the email address is valid.

The email address validation criteria are as follows:

- Contains a single "@" symbol.
- Contains at least one dot (.) after the "@" symbol.
- The domain name (after the last dot) has at least two characters.

Write a program that uses the `is_valid_email` function to do the following:

1. Prompt the user to enter an email address.
2. Call the `is_valid_email` function with the provided input.
3. Print whether the email address is valid or not.

Example Output:

```
Enter an email address: john@example.com
Valid email address: True

Enter an email address: johndoe@example
Valid email address: False
```
