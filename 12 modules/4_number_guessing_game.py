import random

while True:

    x = int(input("enter a random number between 1 to 10: "))

    y = random.randint(1, 10)
    if x > 10:
        print('your guess', x)
        print('your number should be in range 1 to')
    elif x > y:
        print('your guess', x)
        print('computer guess', y)
        print('your guess is higher than the computer guess')
    elif x < y:
        print('your guess', x)
        print('computer guess', y)
        print('your guess is lower than the computer guess')
    else:
        print('your guess', x)
        print('computer guess', y)
        print('cheeers')
