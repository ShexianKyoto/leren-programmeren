#A variable name can only contain (A-z, 0-9, and _ ) and cannot start with a number
variable = "hello" #string datatype
variable2 = 13     #integer datatype
variable3 = 1.132  #float datatype
variable4 = 1j     #complex datatype
variable5 = True   #boolean datatype
#multiple variables with multiple values
#x, y, z = "Orange", "Banana", "Cherry"

print(variable)
print(f'{variable} {variable2}') #f' string werkt met spaties

print(str(variable), int(variable2), float(variable3), complex(variable4))

aantal = int(5)
omschrijving = str("product")
stuksprijs = float(1.28)
regelprijs = aantal * stuksprijs
kassabon = aantal, omschrijving, stuksprijs, regelprijs
print(f'{kassabon}') # f string with {variable} parameter

#   BiF: Built-in Functions
#   int() | float() | str() | bool() | max/min() | range() | print() | input | list() | len() | iter() |
#   tuple(list which is ordered and unchangable) | 

#list1 = [variable, "string"]

#Tuples are used to store multiple items in a single variable.

#typecasting: datatype omzetten andere datatype

#looping through a string
#for x in "banana":
#print(x)

#boolean = true or false, example: 10 > 9 = true

### PYTHON OPERATORS ###

#   Python Arithmetic Operators
#Operator    Name	            Example
#   +        Addition	        x + y	
#   -        Subtraction	    x - y	
#   *        Multiplication	    x * y	
#   /        Division	        x / y	
#   %        Modulus	        x % y	
#   **       Exponentiation	    x ** y	
#   //       Floor division	    x // y

#   Python Assignment Operators
#Operator	 Example	    Same As
#   =	     x = 5          x = 5	
#   +=	     x += 3	        x = x + 3	
#   -=	     x -= 3	        x = x - 3	
#   *=	     x *= 3	        x = x * 3	
#   /=	     x /= 3	        x = x / 3	
#   %=	     x %= 3	        x = x % 3	
#   //=	     x //= 3	    x = x // 3	
#   **=	     x **= 3	    x = x ** 3	
#   &=	     x &= 3	        x = x & 3	
#   |= 	     x |= 3	        x = x | 3	
#   ^=	     x ^= 3	        x = x ^ 3	
#   >>=	     x >>= 3	    x = x >> 3	
#   <<=	     x <<= 3        x = x << 3

#   Python Comparison Operators
# Operator   Name                        Example
#   ==       Equal	                     x == y	
#   != 	     Not equal	                 x != y	
#   >	     Greater than	             x > y	
#   <	     Less than	                 x < y	
#   >=	     Greater than or equal to    x >= y	
#   <=	     Less than or equal to	     x <= y

#   Python Logical Operators
# Operator   Description                                                Example
#   and 	 Returns True if both statements are true	                x < 5 and  x < 10	
#   or	     Returns True if one of the statements is true	            x < 5 or x < 4	
#   not	     Reverse the result, returns False if the result is true	not(x < 5 and x < 10)

#   Python Identity Operators
# Operator   Description                                                Example
#   is 	     Returns True if both variables are the same object	        x is y	
#   is not	 Returns True if both variables are not the same object	    x is not y

#   Python Membership Operators
# Operator   Description                                                                            Example
#in 	     Returns True if a sequence with the specified value is present in the object	        x in y	
#not in	     Returns True if a sequence with the specified value is not present in the object	    x not in y

#   Python Bitwise Operators
# Operator  Name                    Description
#   & 	    END                     Sets each bit to 1 if both bits are 1
#   |	    OR	                    Sets each bit to 1 if one of two bits is 1
#   ^	    XOR	                    Sets each bit to 1 if only one of two bits is 1
#   ~ 	    NOT	                    Inverts all the bits
#   <<	    Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off
#   >>	    Signed right shift	    Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off

### PYTHON BIF ###

#Function	    Description
#abs()	        Returns the absolute value of a number
#all()	        Returns True if all items in an iterable object are true
#any()	        Returns True if any item in an iterable object is true
#ascii()	        Returns a readable version of an object. Replaces none-ascii characters with escape character
#bin()	        Returns the binary version of a number
#bool()	            Returns the boolean value of the specified object
#bytearray()	    Returns an array of bytes
#bytes()	        Returns a bytes object
#callable()	    Returns True if the specified object is callable, otherwise False
#chr()	        Returns a character from the specified Unicode code.
#classmethod()	Converts a method into a class method
#compile()	    Returns the specified source as an object, ready to be executed
#complex()	    Returns a complex number
#delattr()	    Deletes the specified attribute (property or method) from the specified object
#dict()	        Returns a dictionary (Array)
#dir()	        Returns a list of the specified object's properties and methods
#divmod()	    Returns the quotient and the remainder when argument1 is divided by argument2
#enumerate()	    Takes a collection (e.g. a tuple) and returns it as an enumerate object
#eval()	        Evaluates and executes an expression
#exec()	        Executes the specified code (or object)
#filter()	    Use a filter function to exclude items in an iterable object
#float()	        Returns a floating point number
#format()	    Formats a specified value
#frozenset()	    Returns a frozenset object
#getattr()	    Returns the value of the specified attribute (property or method)
#globals()	    Returns the current global symbol table as a dictionary
#hasattr()	    Returns True if the specified object has the specified attribute (property/method)
#hash()	        Returns the hash value of a specified object
#help()	        Executes the built-in help system
#hex()	        Converts a number into a hexadecimal value
#id()	        Returns the id of an object
#input()	        Allowing user input
#int()	        Returns an integer number
#isinstance()	Returns True if a specified object is an instance of a specified object
#issubclass()	Returns True if a specified class is a subclass of a specified object
#iter()	        Returns an iterator object
#len()	        Returns the length of an object
#list()	        Returns a list
#locals()	    Returns an updated dictionary of the current local symbol table
#map()	        Returns the specified iterator with the specified function applied to each item
#max()	        Returns the largest item in an iterable
#memoryview()	Returns a memory view object
#min()	        Returns the smallest item in an iterable
#next()	        Returns the next item in an iterable
#object()	    Returns a new object
#oct()	        Converts a number into an octal
#open()	        Opens a file and returns a file object
#ord()	        Convert an integer representing the Unicode of the specified character
#pow()	        Returns the value of x to the power of y
#print()	        Prints to the standard output device
#property()	    Gets, sets, deletes a property
#range()	        Returns a sequence of numbers, starting from 0 and increments by 1 (by default)
#repr()	        Returns a readable version of an object
#reversed()	    Returns a reversed iterator
#round()	        Rounds a numbers
#set()	        Returns a new set object
#setattr()	    Sets an attribute (property/method) of an object
#slice()	        Returns a slice object
#sorted()	    Returns a sorted list
#staticmethod()	Converts a method into a static method
#str()	        Returns a string object
#sum()	        Sums the items of an iterator
#super()	        Returns an object that represents the parent class
#tuple()	        Returns a tuple
#type()	        Returns the type of an object
#vars()	        Returns the __dict__ property of an object
#zip()	        Returns an iterator, from two or more iterators