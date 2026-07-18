'''
ploymorphism
-------------
>>Polymorphism means many forms.
>>it allows same method,  function or operator to perform different tasks depending on the same object...

Types:
-------
>> 1)Method overloading : means having multiple methods with the same name but different parameters..
@eg:
class Cal:
    def add(self,num,num_2=0):
        print(num + num_2)
    def add(self,num,num_2=0,num_3=0):
        print(num + num_2+num_3)
obj = Cal()
obj.add(4,5)
obj.add(41,25,42)

2)Method overridding : this is occurs when a child class provides its own implementation of a method already defined in its parent class..

@Eg:
class animal:
    def sound(self):
        print("Animal make sounds")
class dog(animal):
    def sound(self):
        print("Dogs barks")
d = dog()
d.sound()

3)Operator Overloading : This allows operators (+, - , *) to work differntly for user-definded objects..

(i)  __add__(+)
(ii) __sub__(-)
(iii)__mul__(*)
(iv) __truediv__(/)
(v)  __eq__(==)
(vi) __It__(<)

class student:
    def __init__(self,marks):
        self.marks = marks
    def __add__(self,other):
        return self.marks - other.marks
s1 = student(50)
s2 = student(25)
print (s1 + s2)

**Data Abstraction:
--------------------
>>Data Abstraction is the process of hiding implementation details and showing only the essential data to the user

@eg
from abc import ABC,abstractmethod
class parent:
    @abstractmethod
    def display(self):
        pass

@eg2
from abc import ABC, abstractmethod
class bank:
    @abstractmethod
    def interest(self):
        raise NotImplementedError('subclass must implement interest()')
class SBI(bank):
    def interest(self):
        print('SBI interest rate: 6.5%')
class ICIC(bank):
    def interest(self):
        print('ICIC interest Rate: 5.5%')
class HDFC(bank):
    def interest(self):
        print('HDFC interest Rate: 5.2%')
banks = [SBI(),ICIC(),HDFC()]

for j in banks:
    j.interest()
'''



















        
