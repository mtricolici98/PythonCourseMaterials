# Password Strength Checker

Write a Python function called `check_password_strength` that checks the strength of a given password. The function
should take one argument: `password` (string) representing the password to be checked. The function should return a
boolean value indicating whether the password meets the specified strength criteria.

The password strength criteria are as follows:

- At least 8 characters long
- Contains at least one uppercase letter
- Contains at least one lowercase letter
- Contains at least one digit
- Contains at least one special character (e.g., !@#$%^&*)

Write a program that uses the `check_password_strength` function to do the following:

1. Prompt the user to enter a password.
2. Call the `check_password_strength` function with the provided input.
3. Print whether the password meets the strength criteria or not.

Example Output:

```
Enter a password: MyPass123
Password strength: True (meets the criteria)

Enter a password: abcdefg
Password strength: False (does not meet the criteria)
```

> Note: You can enhance the password strength checker by adding additional criteria or customizing the requirements
> according to your preference.
