# List- mutable
   # 0  1 2   3     4
l = [1,2,3,'hello',5]
   #-5-4-3  -2    -1
   
print(l)
print(type(l))

# slicing
# list[start:end:skip]
# print(l[0:])
# print(l[0:5])
# print(l[0:4:2])
# not mentioning end will by default go to the end
# print(l[0::2])

# reverse using slicing
# print(l[-1::-1])
# skipping 2 in reverse
# print(l[-1::-2])


# mutable
l[0]='updated value'
print(l)