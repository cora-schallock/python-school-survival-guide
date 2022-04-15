# Class

## Key Terms:
* class - a type in python
* object - a instance of a specific class
* method - a function that belongs to a specific class
* class variable - a variable that belongs to a specific object 

## Section #1: What's a class
A class can be thought of as a type in python. When you write code to define a custom class, you are in essence creating a new type that contains specific data and a specific functionality. When you want to create a new variable of a class, that is called an object. The data storred in the object is stored using class variables while the functionality is specified using a method.

### Syntax:
If we want to create a new type `animal` we can use the syntax below:
```
class animal:
  def __init__(self):
    pass
    
an_animal = animal() #creating an object of type animal
```

## Section #2: Methods
Python uses methods to implement built-in operations like comparisons, print statements, etc.

### __eq__
The `__eq__` is used to implement `==`

If you have an `__eq__` method defined as:
```
def __eq__(self,object_to_check):
  return self.height == object_to_check.height
```

It will be called by the following line:
```
animal_1 == animal_2
```

One thing that can be confusing about Python's syntax is the difference of the line above and that of the `__eq__` method.
This is how Python converts the line:
```
#you write:
animal_1 == animal_2

#Python reads it as:
type(animal_1).__eq__(animal_1,animal_2)
```

## Section #3: Misc.

### Checking Type:
```
a = animal()
isinstance(a,animal) #check if the variable a is of type animal
```
## References:
* [Python's Class Documentation](https://docs.python.org/3/tutorial/classes.html)



#### TODO:
* reorganize this
