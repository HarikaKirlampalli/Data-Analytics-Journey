'''
DAY-8:
     Statements
    ------------
1.Conditional statements:
if:
@code
num=12
if num%2==0:
    print(f"{num} is a even number")


if-else:
>>else is the fall-back statement incase the if codition is false,then this else will be executed.
@code
num=10
if num%2==0:
    print(f"{num} is a even number")
else:
    print(f"{num} is a even number")

@2code
harika_sbi_details = {"ATM PIN ": '2315'}
pin_=input("Enter your 4 digits pin:")
if pin_ in harika_sbi_deatils['ATM PIN']:
     print ("Welcome to SBI Bank")
else:
    print("Entered incorrect pin")

nested if:(if inside the if )
@code
harika_sbi_details = {"ATM PIN ": '2315'}
pin_= input("Enter your 4 digits pin:")
if len(pin_)==4:
    if pin_ in harika_sbi_details['ATM PIN']:
     print ("Welcome to SBI Bank")
    else:
     print("Entered incorrect pin")
else:
    print("Please enter only 4 digit pin")

elif:
@code
marks_= int(input("Enter your marks: "))
if marks_ >= 90:
    print("A+")
elif marks_ >= 80:
    print("B")
elif marks_ >70:
    print("B+")
elif marks_ > 50:
    print("C")
else:
    print("Failed")

'''
