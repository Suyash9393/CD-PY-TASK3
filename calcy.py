# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 19:13:56 2024

@author: suyash morye
"""

print("####***~CALCULATOR~***####")


num1 = float(input("Enter a first number:"))
num2= float(input("Enter a second number:"))


print("press 1 for addition \npress 2 for subtraction \npress 3 for multiplication \npress 4 for divition ")
                   

choise = int(input("enter your choice form 1-5:"))


if choise ==1:
    print("The addition of given two number is", num1 + num2)
elif choise ==2:
    print("The subtraction of given two number is",num1 - num2)
elif choise ==3:
    print("The multiplication of given two number is",num1*num2)
elif choise ==4:
    print("The divition of given two number is",num1/num2)
elif choise ==5:
    print("The modulus of given two number is",num1%num2)
else :
    print(" invalid input")
    