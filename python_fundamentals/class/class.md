# Class

## Key Terms:
* class - a type in python
* object - an instance of a class
* method - a function that specifies how your class behaves and is used to customize the functionality of your class
* attributes - a variable that belongs to a specific object of the class
* initalize - create a new class object

## Section #1: What's a class
A class can simply be thought of a type in python. Let's say you want to create your own custom type that has a unique functionality and stores data, this can be done by defining a custom class.

By defining a custom class, you are just specifying a new type. In in this new custom class, you can define both class methods and attributes you can customize the functionality of the type and data storred in the type, respectively.

## Section #2 Initalizg (a.k.a the `__init__` method)
When you create a new variable of a class, you create an object (sometimes refered to as a "class object"). 


The object is created using the initalization method  `__init__`, in general the syntax looks like this:
```
#define CustomClass
class CustomClass:
  def __init__(self,**kwargs):
    #insert code here to save the **kwargs as attributes
    pass
    
an_object = CustomClass() #creating an object of type CustomClass
```

Side note, if you read through Python's documentation and you see `**kwargs` or `**kw` this means keyword-arguments. This is shorthand to say that a class method (or a function) can have arguments but doesn't have to. In this syntax it just means that the CustomClass can be initalized with some keyword arguments, and can be customized to fit your use-case (take a look at the example below to get a better idea what this can look like).


------------------------------------------------------------------------------------
#### Example #1: Creating a Class Object with `__init__`
Let's say we want to create a custom class called `animal`. For now, this class is just going to be used to store information about Zoo Animals (using attributes) and it will store an animals name, species, and height. To define this class, we need an `__init__` method that initalizes a new animal object:
```
class animal:
  def __init__(self, name, species, height):
    self.name = name
    self.species = species
    self.height = height    
```

And then once we have defined this animal class, we create a class object by using the following syntax:
```
geoferry_the_giraffe = animal("geoferry","giraffe",520)
```
------------------------------------------------------------------------------------


## Section #3: Methods
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
