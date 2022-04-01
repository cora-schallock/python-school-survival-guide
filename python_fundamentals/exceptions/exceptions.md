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
Let's say that we want to write a program that asks the user for a number (x) and calculates the [factorial](https://en.wikipedia.org/wiki/Factorial) of that number (x!).

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

## Section #2: raise
Now what would happen in Example #1 if the user enetered "-1"?

It *won't* print an error message. It will get stuck in the factorial function and not return an answer (this is because x! is only defined for x >= 0).

### Key Idea: Not all bugs will cause an exception to be raised.

To fix this issue, we can use a raise statement. A raise statement is used to create an exception. Let's take a look at how we can use raise:

------------------------------------------------------------------------------------
#### Example #2: raise

After converting the user_input to a integer, we can check if it is non-negative and if not raise an exception

```
try:
    user_input = input("please enter a number:")
    the_number = int(user_input)
    if the_number >= 0:
        print(factorial(the_number))
    else:
        raise TypeError
except:
    print("Error: You must enter a number")
```

Now when we enter "-1", the boolean check `the_number >= 0` will evaluate to False thus causing us to go the else statment, and raising an exception (causing the code to jump from the try to the except).

------------------------------------------------------------------------------------

## Section #3: Creating Custom Exceptions
Creating custom exceptions is a good way to expand your code to better explain specific errors that occur in your program, and can be used to display error messages to the user that is easier to understand.

The syntax for creating a custom exception is as follows:
```
#define custom exception:
class CustomException(Exception):
    pass
    
#raise custom exception:
raise CustomException
```

An Exception is just a class. If you want to create a custom exception, you can create a new class (in the example above, a class called `CustomException`) and inherit the properties from the base class of Exception.

Let's take a look at how we can use this to display custom error messages:

------------------------------------------------------------------------------------
#### Example #3: Creating Custom Exceptions
```
try:
    user_input = input("please enter a number:")
    the_number = int(user_input)
    if the_number >= 0:
        print(factorial(the_number))
    else:
        raise NegativeIntegerException
except NegativeIntegerException:
    print("Error: You must enter a non-negative integer")
except:
    print("Error: You must enter a number")
```

Now when the user enters "-1" it will display "Error: You must enter a non-negative integer"

------------------------------------------------------------------------------------

## Section #4: Miscellaneous
There are a few miscellaneous items that relate to Exceptions, so I will breifly mention then:

* Assert:
An assert statment is used to check if a condition is met, and if not it raises an exception.

Now techinally we could rewrite the if/else statement in example #3 to use an assert:
```
assert the_number >= 0, NegativeIntegerException #if the_number is not >= 0, raise an NegativeIntegerException
```

However, it is recommended in most style guides that assets should only be used internally to check correctness (so if we are taking input from the user, we shold use a raise).From [Google's Python Style Guide Section 2.4.4](https://google.github.io/styleguide/pyguide.html):
`assert` is used to ensure internal correctness, not to enforce correct usage nor to indicate that some unexpected event occurred. If an exception is desired in the latter cases, use a raise statement. 

* finally:
This is use in addition to a try-except when you want to do an operation regardless of an exception occurred or not:
```
try:
    user_input = input("please enter a number:")
    the_number = int(user_input)
    print(factorial(the_number))
except:
    print("Error: You must enter a number")
finally:
    print("The program has finished running")

```

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
* [Google's Python Style Guide](https://google.github.io/styleguide/pyguide.html)


#### TODO:
* expand on section 3
* expand on section 4
* add section 4 to notebook
* double check spelling
