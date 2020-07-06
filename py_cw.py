

# Arash's coursework template

# Krishna Mattapalli, ktm7   <--- so we know who you are
# F28PL Coursework 2, Python                         <--- sanity check


# You may assume variables, procedures, and functions defined in earlier questions
# in your answers to later questions, though you should add comments in code explaining
# this if any clarification might help read your code.


################################################################################
# Question 1   <--- Yes, so we know what question you think you're answering


"""
The complex numbers are explained here (and elsewhere):
 http://www.mathsisfun.com/algebra/complex-number-multiply.html
Represent a complex integer as a pair of integers, so (4,5) represents 4+5i (or 4+5j, depending on the complex numbers
notation you use).
1a. Using def, define functions cadd and cmult representing complex integer addition and
multiplication.
For instance,
 cadd((1,0),(0,1))
should compute
 (1,1).
1b. Python has its own native implementation of complex numbers. Write translation functions
tocomplex and fromcomplex that map the pair (x1,y1) to the complex number x1+(y1)j and vice 
versa. You may use the python methods real and imag without comment, but not complex 
(use j directly instead).
"""
#  <--- always have the question under your nose

#####################################
# Question 1a

# This cadd functions works on addition of complex integers.
def cadd(c1, c2):
     return (((c1[0] + c2[0]),(c1[1] + c2[1])))

# Examples for cadd Function.
print(cadd((1,0),(0,1)))    
print(cadd((5,1),(1,5))) 
    
# This cmult functions works on multiplication of complex integers.
def cmult(c1, c2):
     return (((c1[0] * c2[0]) - (c1[1] * c2[1])), ((c1[1] * c2[0]) + (c1[0] * c2[1])))

# Examples for cmult Function.
print(cmult((1,0),(0,1))) 
print(cmult((5,1),(1,5)))      


#####################################
# Question 1b

# This tocomplex Function works on translation of numbers to complex-numbers.
def tocomplex(x1, y1):
    c = x1 + y1 * 1j
    return c

# Examples for tocomplex Function.
print(tocomplex(4, 5))  
print(tocomplex(3, 2))



# This fromcomplex Function works on translation of complex-numbers to numbers, opposite to tocomplex Function.
def fromcomplex(c):
    c.real
    c.imag
    return (int(c.real), int(c.imag))

# Examples for fromcomplex Function.
print(fromcomplex(1+6j))
print(fromcomplex(4+5j))

# END ANSWER TO Question 1
################################################################################


################################################################################
# Question 2


"""
2a. Using def, write iterative functions seqaddi and seqmulti that implement pointwise
addition and multiplication of integer sequences.
For instance
 seqaddi([1,2,3],[~1,2,2])
should compute
 [0,4,5]
You need not write error-handling code to handle the cases that sequences have different
lengths.
2b. Do as for 2a, but make your functions recursive (like OCaml).
Call them seqaddr and seqmultr.
2c. Do it again. This time use list comprehensions instead of iteration or recursion.
"""

#####################################
# Question 2a

# This seqaddi Function, it iteratively do addition of integer sequences.
def seqaddi(l1,l2):
    lst = []
    for i in range(len(l1)): 
        lst.append(l1[i] + l2[i])
    return lst    

# Examples for seqaddi Function.
print(seqaddi([1,2,3],[-1,2,2]))
print(seqaddi([4,6,8],[0,-2,7]))

# This seqmulti Function, it iteratively do multiplication of integer sequences.
def seqmulti(l1, l2):
    lst2 = [] 
    for i in range(len(l1)): 
        lst2.append(l1[i] * l2[i]) 
    return lst2

# Examples for seqmuli Function.
print(seqmulti([1,2,3],[-1,2,2]))
print(seqmulti([4,6,8],[0,-2,7]))

####################################
# Question 2b

# This seqaddr Function works same as seqaddi Function but this function is implemented in recursive way for addition of integer sequences.
def seqaddr(l1, l2):
    if len(l1) == 0:
        return l2
    elif len(l2) == 0:
        return l1
    return [l1[0] + l2[0]] + seqaddr(l1[1:], l2[1:])

# Examples for seqaddr Function.
print(seqaddr([1,2,3],[-1,2,2]))
print(seqaddr([4,6,8],[0,-2,7]))


# This seqmultr Function works same as seqmulti Function but this function is implemented in recursive way for multiplication of integer sequences.
def seqmultr(l1, l2):
    if len(l2) == 0:
        return l1
    elif len(l1) == 0:
        return l2
    return [l1[0] * l2[0]] + seqmultr(l1[1:], l2[1:])

# Examples for seqmultr Function.
print(seqmultr([1,2,3],[-1,2,2]))
print(seqmultr([4,6,8],[0,-2,7]))

#####################################
# Question 2c

# This seqaddlc Function works same as seqaddi and seqaddr Functions but this function is implemented in list comprehensions way for addition of integer sequences.
def seqaddlc(l1,l2):
    return list(( x + y for x in l1 for y in l2 if l1.index(x) == l2.index(y)))

# Examples for seqaddlc Function
print(seqaddlc([1,2,3],[-1,2,8]))
print(seqaddlc([4,6,8],[0,-2,7]))

# This seqmultlc Function works same as seqmulti and seqmultr Functions but this function is implemented in list comprehensions way for multiplication of integer sequences.
def seqmultlc(l1,l2):
    return list(( x * y for x in l1 for y in l2 if l1.index(x) == l2.index(y)))


# Examples for seqmultlc Function.
print(seqmultlc([1,2,3],[-1,2,3]))
print(seqmultlc([4,6,8],[0,-2,5]))


# END ANSWER TO Question 2
################################################################################

################################################################################
# Question 3

"""
Write functions
● ismatrix
This should input a list of list of integers (henceforth an intmatrix) and test whether a list
of lists of integers represents a matrix (so the length of each row should be equal).
● matrixshape
This should input an intmatrix and return the size of the matrix, which is the number of rows and the number of columns 
(traditionally the number of rows is given first, but if you have done it the other way around that’s fine; 
just make sure to clearly explain your code). 

● matrixadd
Matrix addition, which is simply pointwise addition.
● matrixmult
Similarly for matrix multiplication.
You do not need to write error-handling code, e.g. for the cases that inputs do not represent
matrices or represent matrixes of the wrong shapes; so for instance your matrixshape may 
assume that the argument has successfully passed the test ismatrix.
Your answer can use iteration, recursion, list comprehension, or anonymous functions. You
should not appeal to any libraries, e.g. for matrix processing.  Don't use zip.
"""

# This ismatrix function will check wether list of lists of integers represents a matrix and it returs true if length of each row is equal. 
def ismatrix(m):
    if len(m[0])==len(m[1]):
        return True 
    else:
        return False

# print(ismatrix([[2,3,4], [3,2,6,7], [2,3,4]]))
# print(ismatrix([[1,2,3], [3,4,6]]))   
# Examples for ismatrix Function.
print(ismatrix([[1,2,3], [1,2,4,7]]))   
print(ismatrix([[1,2,3], [1,2,4,]]))       

# This matrixshape function is returning the size of matrix and number of rows and the number of columns in matrix.
def matrixshape(m):
    Column = len(m[0])
    Row = len(m)
    return Row, Column
    
    

# Examples for matrixshape Function.
print(matrixshape([[1,2,3], [1,2,4,]]))
print(matrixshape([[4,5,6], [6,5,4,]]))

# This matrixadd function is adding the matrixs.
def matrixadd(m1,m2):
    Matrix = []
    for i in range(0, len(m1)):
        Matrix.append(seqaddlc(m1[i], m2[i]))
    return Matrix

# Examples for matrixadd Function.
print(matrixadd([[1,2,3], [1,2,4]], [[5,6,7], [5,6,7]]))
print(matrixadd([[7,3,5], [1,0,5]], [[7,9,4], [5,6,7]]))



# matrixmult helper function.
def dot(r1, r2):
    product = 0 
    for i in range(len(r1)):
        product += (r1[i] * r2[i])
    return product

# matrixmult helper function, rotates matrix so it can be multiplied.
def pose(m):
    newrow = []
    newmatrix = []

    for i in range(len(m[0])):
        for row in m:
            newrow.append(row.pop(0))
        newmatrix.append(newrow)
        newrow = []
    return newmatrix

def matrixmult(m1, m2):
    # flip 2nd matrix fist.
    m2 = pose(m2)
    # then multiply iteratively.
    newmatrix = []
    row = []
    # get the dot product for each row and add it to a new matrix row.
    for i in range(len(m1)):
        for j in range(len(m2)):
            row += [dot(m1[i], m2[j])]
        #append the row to the new matrix
        newmatrix.append(row)
        row = []
    return newmatrix

# print(matrixmult([[1,2,3], [1,2,4]], [[5,6,7], [5,6,7]]))

# END ANSWER TO Question 3
################################################################################


###############################################################################
# Question 4


"""
Write an essay on Python data representation. Be clear, to-the-point, and concise. Convince
your marker that you understand:
● Mutable vs immutable types. Give at least two examples of each, with explanation.
● Integer vs float types.
● Assignment = vs equality == vs identity is.
● The computational effects of a call to list on an element of range type, as in
list(range(5**5**5)).
● Slices, with examples. Including an explanation of the difference in execution between
 list(range(10**10)[10:10]) and
 list(range(10**10))[10:10]
Include short code-fragments where appropriate (as I do when lecturing) to illustrate your
observations.
"""


# Mutable vs Immutable 
# In mutable object can be changed after created, Object of built type are int, float, str, bool, tuple and Unicode.
# But, in Immutable we can't make changes after creating it is like constant, Object of built-in types are a list, set and dict.

# Examples
# Immutable
# Tuples are immutable, so I created a tuple in a variable "a" and then I tried to add another number to tuple but it raises an error because the tuple is immutable, so I can do any changes after creating.
a = (1,2,3,4)
# a.append(5) This command is an error so, I just kept in comments to run the program.
print(a)

#Same as above, Heare I tried to change the value in position "4" but when I tried it is raising an error because it is immutable.
b = (2,4,6,8,11)
# b[4] = 10 This command is an error so, I just kept in comments to run the program
print(b)

# Mutable
# In case of Mutable object, I created an object type int identifiers a and b are tagged to the same list object which is a collection of 3 immutable objects, Now poping an item from a list then, Object id will be changed. a and b will be pointing to the same object after modification, List will be [4,5].
 
a = [4,5,6]
b = a
print(id(a) == id(b))
a.pop()
print(id(a) == id(b)) 

# Here I created a list with integer values, Added value 6 to list c by using append and changed the value of position c[2] to 9. then printed c to check the value of c it is [1,2,9,4,5] it is updated because it is mutable. 
c = [1,2,3,4,5]
c.append(6)
c[2] = 9
print(c)

# Integer vs Floats
# Integers are often called integer or ints, No decimal points and there are two types in integers positive and negative, we can get integer by adding two floats.
# Floats are often called float they represent real numbers and with decimal points, Same as integers they have two types positive and negative. we can get float by dividing an integer.

# Examples
# Integers
# I declared a int vairable "x" and assigned a value 1 to it and showed type of "x".
x = 1
print(type(x))

# I declared an int variable "y" and assigned a value to it and showed the type of "y".
y = 1234567890
print(type(y))

# I declared an int variable "z" and assigned a value 1 to it and showed the type of "z".
z = 9876543210
print(type(z))

# Floats
# I declared a float vairable "x" and assigned a value to it and showed type of "x".
x = 1.024887567857
print(type(x))

# I declared a float variable "y" and assigned a value to it and showed the type of "y".
y = 5.7
print(type(y))

# I declared a float variable "z" and assigned a value to it and showed the type of "z".
z = 10/3
print(type(z))


# Assignment, equality and identity 
# Assignment it will assign a value to a variable and is represented by "=", Value can be anything str, float, int.bit_length
# Equality it will be checking whether two variables ane having same values are not and it represented by "==".
# Identity it is a function returns the identity of an object, It is represented by "id()". It remains constant during lifetime and This is an integer which is unique for the given object.

# Examples
# Assignment
# Assigning values to vairables "x", "y", "z".
x = 1
y = 2
z = 3
print(x, y, z)

# Equality
# It is checking wether same values or not in these vairables.
x = 1
y = 1
print(x == y)

# It is checking wether same values or not in these vairables.
p = 9.123
q = 9.123
print(p == q)

# Identity 
# Checking the identity of a and b.
a = 30
b = 30
print(id(a) == id(b))

# Checking the identity of x and y.
x = 2.98
y = 2.98
print(id(x) == id(y))

# list(range(5**5**5))
# The range function stores an object that creates some integers. 
# This function doesn't hold any values in memory but it holds mathematical computation that streams a sequence of integer numbers. 
# In constants, the list contains store a sequence of polymorphic elements. It is usually used to store integers in memory, without storing or referencing the mathematical computation which produced them.
# This function is overloaded but generally, the integer sequence has the minimum value of 0 and it is incremented by 1. The maximum integer is the value which has to be specified, at the least.
# Example, Function range "5**5**5" will generate integer values from 0 to 298,023,223,876,953,125, incrementing successively by one,which means that it will generate a stream with 298,023,223,876,953,125 integers. 
# The value is too big for a regular computer processing power to perform the result of a function, the integer stream is then stored into the memory using the list constructor.

# list(range(10**10)[10:10]) and list(range(10**10))[10:10]

# The difference between these two, 
# In case-1 ("list(range(10**10)[10:10])")
# It dosent break machine because its just 10 computations, the subsequenes are applyed to the range function.

# In case-2 ("list(range(10**10))[10:10]")
# It will break the machine, The subsequences are applied to the list function, the list will be computed first and it will crash the machine.
# so in the case one, the one to 5 is an argument to the range function, in other cases, it is to the list then first range as been called and range generated hole thing
# so created list and then [1:5] takes sub-list of hole list.

# END ANSWER TO Question 4
################################################################################


###############################################################################
# Question 5
# print()
# print('Question 5')

"""
Write a general encoding function encdat that will input an integer, float, complex number, or
string, and return it as a string.

So
• encdat(-5) should return '-5'
• encdat(5.0) should return '5.0'
• encdat(5+5j) should return '5+5j' (not '(5+5j)'; see hint below).
• encdat('5') should return '5'


"""

# This encdat function will convert integer, float, complex number and string to a string.
def encdat(dat):
    return str(dat).strip('()')

# Examples for encdat Function.
print(encdat(-5)) 
print(encdat(5.0))  
print(encdat(5+5j)) 
print(encdat("5"))  

# END ANSWER TO Question 5
################################################################################


###############################################################################
# Question 6


"""
An encoding f of numbers in lists is as follows:
• f(0) = [] (0 maps to the empty list)
• f(n+1) = [f(n),[f(n)]] (n+1 maps to the list that contains f(n) and singleton f(n))
Implement encode and decode functions in Python, that map correctly between nonnegative
integers and this representation. Call them fenc and fdec.
"""

# fenc function takes in one argument.
def fenc(i):
    # checks is x is 0.
    if i==0:
        return []
    # if not then.
    else: 
        # return the encoded version.
       return [fenc(i-1), [fenc(i-1)]]

# Examples for fenc Function.
print(fenc(1))
print(fenc(0))

# fdec function takes in one argument.
def fdec(l):
    # checks if x is an empty list.
    if l==[]:
        # it true that returns 0.
        return 0
    # if not then.
    else:
       # returns the decode version.
       return (fdec(l[0])+1) 

# Examples for fdec Function.
print(fdec([[], [[]]]))
print(fdec([]))


# END ANSWER TO Question 6
##################################################################### ###########


###############################################################################
# Question 7


"""
Implement a generator cycleoflife such that if we assign
 x = cycleoflife()
then repeated calls to
 next(x)
return the values
 eat
 sleep
 code
 eat
 sleep
 code
 ...
in an endless cycle. If you can’t manage an endless cycle, do a program that runs for 1000
cycles then stops.
Note that this question is not asking you to program an endless loop that prints these values.
In effect, I am asking you to implement what is called a stream (infinite list)
 x = [eat, sleep, code, eat, sleep, code, ...].
This does not mean the whole infinite datastructure is in memory at any time (which is 
impossible for a machine with finite memory), but for any finite but unbounded number of calls 
to next your generator behaves as if it were the infinite datastructure illustrated above.
"""

# This cycleoflife function returns life cycle  eat, sleep and code continuously and I used generator in this function. 
def cycleoflife():
    while True:
        yield "eat" 
        yield "sleep"
        yield "code"

# Exampls for cycleoflife Function.
x = cycleoflife()
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))

# END ANSWER TO Question 7
################################################################################


#################################################################################
# Question 8

"""
Call a *datum* something that is either an integer, or a list of data (datums).

Write a flatten function gendat that converts a datum to a list of integers.

So
- gendat(5) should return [5]
- gendat([])should return []
- gendat([5,[5,[]],[],[5]]) should return [5,5,5]

Do not use str.  You may find it useful to consider isinstance or the following code fragment
   type(5) == type([]) 
"""
# This gendat function will convert datum to a list of integers and "datum" can be an integer or list of data.
def gendat(datum):
    if type(datum) == int:
        return [datum]
    elif datum == []:
        return []
    else:
        while type(datum[0]) == list:
            if datum[0] == []:
                return gendat(datum[1:])
            temp = datum[0].pop()
            if temp != []:
                datum.append(temp)
        return datum[0:1] + gendat(datum[1:])

# Examples for gendat Function.
print(gendat(5))
print(gendat([]))
print(gendat([5,[5,[]],[],[5]]))

# END ANSWER TO Question 8
################################################################################


##########################################################
# Question 9

"""
Implement the Sieve of Eratosthenes
 https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
as a Python generator eratosthenes such that if we assign
 x = eratosthenes()
then repeated calls to
 next(x)
return the primes, starting from 2.
"""
def eratosthenes(n):
    p = [2]
    x = [True] * 5

    while True:
        lastPrime = len(p) - 1
        yield p[lastPrime]

        for y in range(p[lastPrime] + 1, len(x)):
            if x[y] == True:
                p.append(y)
                lastPrime = len(p) - 1
                ArrayLength = (p[lastPrime] ** 2) + 1
                temp = [True] * (ArrayLength - len(x))
                x += temp
                break

        for prime in p:
            for i in range(p[0], len(x) + 2, prime):
                x[i - 2] = False

x = eratosthenes(100)
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))

# This is not an endless generator (like you're asked to programme) this will only get primes upto the passed input or 40000
def eratosthenes(z=40000):
    # create an array of true values the size of z
    A = [True] * z
    # iterate over each value to z squared
    for x in range(2, int(z ** 0.5)):
        # if A[x] has a true value
        if A[x]:
            # iterate over a range starting from x*2 ending at z in jumps of x
            for z in range(x * 2, z, x):
                # set anything in the range to false
                A[z] = False
    # iterate over the array
    for y in range(2, len(A)):
        # if a value is true that index is a prime number
        if A[y]:
            # yield the current iterator location as it is a prime
            yield y




# END ANSWER TO Question 9
###############################################################################

