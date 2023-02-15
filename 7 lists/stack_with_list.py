# STACK - linear data structure
# string manner: LIFO / FILO
# STACK OPS- push, pop, peek, display

l = []

while True:
    op = int(input('''
        CHOOSE AN OPERATION:
        1. Push
        2. Pop
        3. Peek
        4. Display
        5. Exit
    '''))
    if op==1:
        n=input("enter the value to push: ")
        l.append(n)
        print('result: ', l)
    elif op==2:
        if len(l)==0:
            print("stack is empty, nothing to pop")
        else:
            p = l.pop()
            print('popped', p)
            print('result', l)
    elif op==3:
        if len(l)==0:
            print("stack is empty, nothing to show")
        else:
            print('peeked value: ', l[-1])
    elif op==4:
        print("displaying stack", l)
    else:
        break

