'''DAY-12
-----------
FUNCTIONS:
>>Functions is a block of code that can be reusable.
>>Function can avoid the repeated lines of code.
>>Functions are 2 types:
(i) built-in:
eg: print(),max(),type(),min(),sum()
(ii) user-define:
>>This function starts with the keyword (def).
syntax:
def func_name(parameters):
    -----------  #we have to give tab space in starting
    -------------
    -----------
func_name(arguments)
eg:
def add():
    print("Hello")
add()
***Types Of arguments:
1.Required argument :- We have to pass same no.of arguments with definition of the function.
eg:
def add(a,b)#in the required arg we should not write code like this.
    print(a)
add(5)

2.Default argm :-
@eg-1:
def add(a,b):
    print(a)
add(a=5,b=6)

@eg-2:
num = 5
num_2 = 6
def add(a,b):
    print(a)
    print(b)
add(num,num_2)

3.Keyword argm :- We can pass as a pair like (variable = datatype).
eg:
def add(a,b):
    print(a+b)
add(a=5,b=6)

4.variable length argm :- It can pass 'n' no.of arguments and just use args in the parameters,will receive tuple of arguments
Eg:
num = 5
num_2 = 6
num_3 = 7
num_4 = "Hello"
def add(*a):
    print(a)
add(num,num_2,num_3,num_4)

Eg--(**asterisk)
--   
def all_(**Any):
    print(Any['Age'])
all_(Name = "Harika",Age = 18)

**Global variable:
>>This global varaible used through out the prgrm.
eg:
num = 5
def func_():
    print(num)
func_()

Note:
  To change the global variable by using keyword (global) that can be change completly inside and outside of the function.

**Local vaariable:
>>
'''
num = 5
def func_():
    global num
    num = 25
    print(num)
func_()
print(num)







































