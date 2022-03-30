# Exceptions:

# Key Terms:
* exception - an error that occurs while your code is running
* raise - create an exception
* try-except block - a block of code that checks for exceptions, and if an exception occurs, it is handled appropriately 

## Section #1: try-except block
The try-except block is the foundation of how exceptions are handeled in python. A try-except block has two parts the try block and the except block. 

**In a nutshell, you place your code that might raise an exception inside the try block and you place your code that handles the exception in the except block.**

------------------------------------------------------------------------------------
#### Example #1: Basic try-except
Let's say that we want to write a program that asks the user for a number and calculates the [factorial](https://en.wikipedia.org/wiki/Factorial) of that number.

We begin by defing a function to calculate the factorial:
```
def factorial(x):
    if x == 0:
        return 1
    else:
        return x*factorial(x-1)
```

Next we write code to get the input number from the user, and calls the factorial function above:
```
user_input = input("please enter a number:")
the_number = int(user_input)
factorial(the_number)
```

Notice that there is a potential issue, what if instead of a number, the user types in "abc".
Try it for yourself!

What happens is an exception is raised when we try to convert "abc" to an integer.

We want to be able to handle this possible exception. So we add a try-except block. We will try to convert the user's input to a number and if we can't, we'll print out a message saying what happened.
```
try:
    user_input = input("please enter a number:")
    the_number = int(user_input)
    print(factorial(the_number))
except:
    print("Error: You must enter a number")
```

Now if the user inputs a string of letters, say "abc", an exception is raised in the third line as calling int("abc") raises an exception, and the program jumps from the try block down to the except block.

------------------------------------------------------------------------------------


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
