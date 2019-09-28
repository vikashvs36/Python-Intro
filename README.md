# Python-Intro

> ## Data types

Python provides various standard data types that define the storage method on each of them. The data types defined in Python are given below.

* Numbers
* String
* List
* Set
* Tuple
* Dictionary

> ## Declaring Variable and Assigning Values

> #### Number
1. Assigning single value to multiple variables:
  
    x=y=z=50  

2. Assigning multiple values to multiple variables:
  
    a,b,c=5,10,15  
    The values will be assigned in the order in which variables appears. That means:
    a=5, b=10, c=15
     
> #### String:
* The operator * is known as repetition operator as the operation "Python " *2 returns "Python Python ".

      > str = "Vikash"
      > print str
      Vikash
      > print (str1*2) # printing the string twice  
      Vikash Vikash

**Syntax : { } .format(value)**
Example: 
 
    # Print a table from user input
    no = int(input("Please enter a number to print table : "))
    for i in range(1,11) :
    print("{} * {} = {}".format(no,i,no*i))

    
> #### List
Lists are similar to arrays in C. However; the list can contain data of different types. The items stored in the list are separated with a comma (,) and enclosed within square brackets [].
We can use slice [:] operators to access the data of the list. The concatenation operator (+) and repetition operator (*) works with the list in the same way as they were working with the strings.

Consider the following example.

    > l = [1, "hi", "python", 2]  
    > print (l[3:]);  
    [2]
    > print (l[0:2]);  
    [1, 'hi']
    > print (l);  
    [1, 'hi', 'python', 2]
    > print (l + l);  
    [1, 'hi', 'python', 2, 1, 'hi', 'python', 2]
    > print (l * 3);   
    [1, 'hi', 'python', 2, 1, 'hi', 'python', 2, 1, 'hi', 'python', 2]

> #### Tuples:
* Tuple is another form of collection where different type of data can be stored.
* It is similar to list where data is separated by commas. Only the difference is that list uses square bracket and tuple uses parenthesis.
* Tuples are enclosed in parenthesis and cannot be changed.

Eg:
 
    >> tuple=('rahul',100,60.4,'deepak')  
    >> tuple1=('sanjay',10)  
    >> tuple  
    ('rahul', 100, 60.4, 'deepak')  
    >> tuple[2:]  
    (60.4, 'deepak')  
    >> tuple1[0]  
    'sanjay'  
    >> tuple+tuple1  
    ('rahul', 100, 60.4, 'deepak', 'sanjay', 10)  
    
> #### Dictionary:
* Dictionary is a collection which works on a key-value pair.
* It works like an associated array where no two keys can be same.
* Dictionaries are enclosed by curly braces ({}) and values can be retrieved by square bracket([]).

Eg:

    >> dictionary={'name':'charlie','id':100,'dept':'it'}  
    >> dictionary  
    {'dept': 'it', 'name': 'charlie', 'id': 100}  
    >> dictionary.keys()  
    ['dept', 'name', 'id']  
    >> dictionary.values()  
    ['it', 'charlie', 100]   
    
> ## Special Python Operators

* ** (Exponent)	It is an exponent operator represented as it calculates the first operand power to second operand.
* // (Floor division)	It gives the floor value of the quotient produced by dividing the two operands.

> ## Python Comments

1) Single Line Comment:

       # This is single line comment.  
      
2) Multi Line Comment:

       ''''''This 
       Is 
       Multipline comment'''  

> ## If-else statements

    if condition:   
        # block of statements   
    elif condition:   
        # block of statements   
    elif condition:   
        # block of statements   
    else:
        # block of statements

