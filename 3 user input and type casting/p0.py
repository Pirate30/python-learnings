# input() - to take use input - by default converts it to as a string
# int() - to convert to int datatype
# float() - to convert to float datatype
# eval() - dynamically evaluates a string as a Python expression


## input
# a=input("please enter the value a:")
# b=input("please enter the value b:")
# print(a+b)

## type casting
# a=int(input("please enter the value a:"))
# b=int(input("please enter the value b:"))
# c=float(input("please enter the value c:"))
# print(a+b+c)

## general type casting can be done with eval() - it parses both int and float
a= eval(input("please enter the value a:"))
b= eval(input("please enter the value b:"))
print(a+b)