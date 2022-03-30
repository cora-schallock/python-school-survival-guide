# Exceptions:

# Key Terms:
* exception - an error that occurs while your code is running
* raise - create an exception
* try/ except block - a block of code that checks for exceptions, and if an exception occurs it is handeled 

## Section #1: try/ except
The try/ except block is the foundation of how exceptions are handeled in python. A try/ except block has two parts the try block and the except block. 

**In a nutshell, you place your code that might raise an exception inside the try block and you place your code that handles the exception in the except block.**

#### Example #1: Basic try/ except
In this scenario, you are taking input from a user that indicates a number. If the input can not be convereted to a number you should tell the user what they did wrong.

```
try:  
  user_input = input("please enter a number:")
  the_number = int(user_input)
except:
  print("Error: You must enter a number")
```

If the user inputs a string of letters, say "abc", an exception is raised in the third line as calling int("abc") raises an exception, and the program jumps from the try block down to the except block.

# Syntax Review:
* `assert` - checks if a condition is met, and if it is not met it raises an exception
* `exception` - an error that occurs while your code is running
* `except` - indicates a block of code that should run if an exception is raised in a `try` block
* `raise` - creates an exception
* `try` - indicates a block of code that contains code where an exception could occur

## References:
* [Python's Exception Documentation](https://docs.python.org/3/tutorial/errors.html)
* [More about custom exceptions](https://www.programiz.com/python-programming/user-defined-exception)
* [Another explanation of the try/except block](https://www.w3schools.com/python/python_try_except.asp)
