'''
DAY-14
    LAMBDA FUNCTION:
 ---------------------
>>This is also called as annonymous function.
>>A lambda function can take n number of arguments but having only one expression.

Syntax:
 lambda arguments : expression
@code
some = lambda an,so : an + so #we can use all methmatical operators like + - *...
print(some(20,5))

**filter():
>>>The filter() function is a built-in function used to filter elements from an itterable such as list, tuple and set based on condition.
>>this filter() function returns filter object so we can convert that into list,set and tuple

Syntax--
   filter(function, itterable)
@code
nums = [1,2,3,4,5,6]
rev = filter(lambda a: a%2 ==0,nums)
print(list(rev))

   LIST COMPREHENSION:
   ------------------
>>This offers a shorter syntax when we want to create a new file from the old.

Syntax :-
  variable_name = [expression loop condition]
@code
old_ = [1,2,3,4,5,6]
new_ = [j for j in old_  if j%2==0]
print(new_)

   DICTIONARY COMPREHENSION:
   -------------------------
>>This offers a shorter syntax when we want to create a new dict from the old dict.

Syntax :-
  variable_name = [expression loop condition]

'''
old_dict = {1:2, 3:9, 5:6}
new_dict = {i:j for (i,j) in old_dict.items() if j % 2==0}
print(new_dict)



























































