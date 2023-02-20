import random

while True:
    x = int(input('''
        choose a number:
        1. Rock
        2. Paper
        3. Scissors
    '''))

    y = random.choice([1, 2, 3])

    cases = ['Rock', 'Paper', 'Scissors']

    wins = [
        [1, 3],
        [3, 2],
        [2, 1]
    ]

    print('you chose: ', cases[x-1])
    print('computer chose: ', cases[y-1])

    youwon = False

    for win in wins:
        if (x == win[0] and y == win[1]):
            youwon = True
    if (x == y):
        print('Tied')
    elif (youwon == True):
        print('You Won!')
    elif (youwon == False):
        print('You Lost!')
