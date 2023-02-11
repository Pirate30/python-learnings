# String: sequence of character

# Indexing in string
# String: W  h  a   t     u  p     b  i  y  a  c  h
# LTR:    0  1  2   3  4  5  6  7  8  9  10 11 12 13
# RTL:   -14-13-12 -11 -10-9 -8 -7 -6 -5 -4 -3 -2 -1


s = "welcome to hell"
# print(s[0])
# print(s[-1])

# --------------------------------------------------------------
# slicing :
# lrt
# print(s[0:7])
# print(s[0::3])
# rtl
# print(s[-1::-1])

# ------------------------------------------------------------------
# iteration of string
# with for loop
# print(len(s)) #15
# for a in range(len(s)):
#     print(s[a])

# reverse iteration way:1
# s = s[-1::-1]
# for a in range(len(s)):
#     print(s[a])

# reverse iteration way:2
for a in range(len(s)-1, -1, -1):  # !revisit the basics of range()
    print(s[a])
