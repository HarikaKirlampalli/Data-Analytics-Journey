'''
DAY-5:
   Dictionaries
-------------------
>>Dic is a key : Value pair separated by (:) and keys are unique.
>>in the place of keys we have use immutable  data type..

eg code:
details_={"name":"Harika",
          1:"number",(6,7):[1,2]}
print(details_)

**Methods:
-----------
1.keys():
>>Used to get all keys from the dictionary ( colon left side values)
>>Syntax: variable_name.keys()
 eg code:
details_={"Name" : "Harika",
          "Age": 22,
          "Gender": "Female"}
print(details_.keys())

2.values():
>>Used to get all vlaues from the dictionary ( colon right side values)
>>Syntax--variable_name.values()

eg code:
details_={"Name" : "Harika",
          "Age": 22,
          "Gender": "Female"}
print(details_.values())

3.items():
>> get keys and values both.
>>Syntax--variable_name.items()
eg code:
details_={"Name" : "Harika",
          "Age": 22,
          "Gender": "Female"}
print(details_.values())

4.clear():
details_={"Name" : "Harika",
          "Age": 22,
          "Gender": "Female"}
details_.clear()
print(details_)

5.Update():

details_={"Name" : "Harika",
          "Age": 22,
          "Gender": "Female"}
details_.update("Name" : "priyadarshini")
print(details_)

any_=[22,35,32,53]
print(any_[3])
details_={"Name" : "Harika",
          "Age": 22,
          "Gender": "Female"}
print(details_['Gender'])


 **SET:
 --------
 >> set is a collection of  unordered elements that are separated by(,).
 >>set is muttable
 >> can remove duplicate value by itself...
eg code:
go = {1,2,3,4,2}
print(go)
 

***Methods:
 -----------
1.union():

>>symbol(|)
>>combine the elements from both set
syntax--> set_1.union(set_2)
 eg code:
go = {1,2,3,4,2}
so = {4,6,3,5}
print(go|so)#print(go.union(so))

2intersection():

>>symbol(&)
>>common elements from both sets
>>syntax: set_1.intersection(set_2)

eg code:
go = {1,2,3,4,2}
so = {4,6,3,5}
print(go&so)#print(go.intersection(so))

3.Symetric Difference():
>>symbol(^)
>>all different elements from both sets
syntax --set_1.symmetric_difference(set_2)
eg code:
go = {1,2,3,4,2}
so = {4,6,3,5}
print(go^so)#print(go.symmetric_difference(so))

4.add():
>>used to add new elements to the set.
eg code:
go = {1,2,3,4}
go.add(5)
print(go)

5.remove():
>>>to delete the elements from set based on element.
>.it throws error if the element is not found.

eg code:
go = {1,2,3,4,5,6}
go.remove(5)
print(go)

6.discard():
>>it discards the given element but it doesn't throw error
go = {1,2,3,4,5,6}
go.discard(7)
print(go)
'''


 
