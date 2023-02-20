# importing
import random

# randint - takes lower and upper limits as a args and returns random number between them - both limits included
print(random.randint(1, 9))

# ----------------------------------------------

# randrange - same as randint but upper limit not included
print(random.randrange(1, 3))

# ---------------------------------------------

# choice - returns random element from the list
x = [1, 2, 'banana', '?']
print(random.choice(x))

# ---------------------------------------------
# random - gives random floating value between 0 to 1

print(random.random())

# ----------------------------------------------

# shuffle - takes sequence and rearranges random order - no returns
sq = [1, 2, 3, 4, 5, 6]
random.shuffle(sq)
print(sq)  # [6, 2, 1, 4, 3, 5]

# ----------------------------------------------

# uniform - takes 2 params and returns random float number between them

print(random.uniform(1, 5))  # 2.418473857298623

# ----------------------------------------------
