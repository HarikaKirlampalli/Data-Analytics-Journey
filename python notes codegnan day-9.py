'''
DAY-9
  LOOPS
  -----
1.for loop
>>A for loop is ussed to itterate over Aa sequance, list, tuple
@code
any_= [1,2,3,4,5,6]
for j in any_:# j is instance variable.
    print(j)
@code2
any_= {"Name" : "Harika",
       "Age" : "22"}
for key in any_.values():
    print(key)
    
**else in for loop:
------------------
>>the else block will be executed after the for loop, but incase the loop is breaked then it will never entered in the else block
@code
any_= [1,2,3,4,5,6]
for val in any_:
    print(val)
else:
    print("program ended")

2.while loop
>>The while loop will execute untill the condition is true.
@code
i = 1
while i < 5:
    print(i)
    i += 1

***CONTROL STATEMENTS***
------------------------
1.break
>>THe break statement is used to exit from loop
@code1
any_= [1,2,3,4,5,6]
for j in any_:
    print(j)
    
else:
    print("Entered")

@code2
any_= [1,2,3,4,5,6]
for j in any_:
    print(j)
    if j == 4 :
        break
else:
    print("Entered")

2.continue
>>The continue will skip the current itteration.
@code
any_= [1,2,3,4,5,6]
for j in any_:
   
    if j == 4 :
        continue
    print(j)
else:
    print("Entered")

3.pass
>>space holder
@code
any_= [1,2,3,4,5,6]
for j in any_:
    pass

**range()
---------
>>range() is a in built-function that is used to generate a sequance upto a limit.
SYNTAX --> range(start, end, step)
@code
all_= [1,2,3,4,5,6]
for j in range(1,25):
    print(j)

assert keyword
--------------
>> it will used to check the condition, but it will raise an error incase it is false... 
@code
num = int(input("Enter your age:"))
assert num >= 18, "you must have 18 yrs"

 
'''













