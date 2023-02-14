
# normal way to create list with for loop
# l=[]
# for a in range(0,100):
#     l.append(a)
# print(l)

# using list compehension
# variable/expression - loop - filteration/condition
# l = [x for x in range(0,100)]
# prit if even
# l = [x for x in range(0,100) if x%2==0]
# print double
# l = [x*2 for x in range(0,100)]

# strinng to list using comprehension
s='hopelessness'
l = [x for x in s]
print(l)
