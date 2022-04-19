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
As mentioned before, methods are used to specify how classes behave.

There are two types of methods:
* custom methods
* built-in methods (sometimes also referred to as "Magic Methods" or "Dunder Methods")

Methods are specified with a method name, the class object you want to run the method with "self", and optionally additional arguments.

### Section #3.1 Custom Methods
Custom methods are used when you want to add a custom functionality to the class you have created. Custom classes can be used to set class variables (i.e. "Setter Methods" or "Mutator Methods"), get the values of class variables (i.e. "Getter Methods" or "Accessor Methods"), perform calculations, or basically anything a function can do.

------------------------------------------------------------------------------------
#### Example #2: Custom Classes

We are going to expand on the `animal` class from [the previous example](https://github.com/cora-schallock/python-school-survival-guide/blob/main/python_fundamentals/class/class.md#example-1-creating-a-class-object-with-__init__) by adding three additional methods, a method to update the height, a method to return the height, and a method to convert the height to incehs.
```
class animal:
  def __init__(self, name, species, height):
    self.name = name
    self.species = species
    self.height = height  
    
 def set_height(self, height):
     if isinstance(updated_height,int):
      self.height = updated_height
     else:
      raise ValueError('Height needs to be an integer.)
     
 def get_height(self):
     return "{} height is {} cm".format(self.name,self.height)
     
 def height_in_inches(self):
    #convert animals height in cm. to in.
    return self.height/2.54
```

And now to use these functions:
```
geoferry_the_giraffe = animal("geoferry","giraffe",520)

height = geoferry_the_giraffe.get_height()
print(height) #prints "geoferry height is 520 cm"

height_in_inches = geoferry_the_giraffe.height_in_inches()
print(height_in_inches) #prints "204.7244094488189"

geoferry_the_giraffe.set_height("a bad input") #raises a ValueError

geoferry_the_giraffe.set_height(521)
new_height = geoferry_the_giraffe.get_height()
print(new_height) #prints "geoferry height is 521 cm"
```

An advantage of using setter functions, as opposed to setting a class variable directly is that you can check the value your are setting is valid. In the example above, we want to know that the height is an integer so in `set_height` we add a statement to check that explicitly. 

An advantage of using getter functions, as opposed to getting a class variable directly is that you can standardize the output. In the example above, we want to know that the height is an integer so in `get_height` makes a set string that has the animals name and height as well as the units.


The `height_in_inches` is an example of another custom method, and it is being used for a calculation.

------------------------------------------------------------------------------------

### Section #3.2 Built-in methods

Built-in methods are methods that Python by default defines for you, but can be customized to specify how default python operations on a class should behave. Some examples are the `__str__` method that is used to customize the output of print statements, `__eq__` \ `__lt__` \ `__gt__` that are used for comparisons.

Here are a few examples

### __eq__
The `__eq__` method is used to implement `==`

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


### __lt__
The `__lt__` method is used to implement `<`

If you have an `__lt__` method defined as:
```
def __lt__(self,object_to_check):
  return self.height < object_to_check.height
```

It will be called by the following line:
```
animal_1 < animal_2
```

The `__lt__` method is also used to implement sorting and sorted.




## Section #3: Misc.

### Checking Type:
```
a = animal()
isinstance(a,animal) #check if the variable a is of type animal
```
## References:
* [Python's Class Documentation](https://docs.python.org/3/tutorial/classes.html)



#### TODO:
* expand on built-in methods
