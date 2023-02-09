num1 = eval(input('enter a first number'))
num2 = eval(input('enter a second number'))
op = input('choose the operation[+ , - , % , / , *]')

if op=='+':
    print('o/p is', num1+num2)
elif op=='-':
    print('o/p is', num1-num2)
elif op=='%':
    print('o/p is', num1%num2)
elif op=='/':
    print('o/p is', num1/num2)
elif op=='*':
    print('o/p is', num1*num2)
else:
    print('in-valid operator')