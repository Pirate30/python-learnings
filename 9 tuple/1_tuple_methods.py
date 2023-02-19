# min
# max
# count
# index
# sum

t = (10, 20, 30, 40, 50, 60, 70, 80, 90, 20, 10, 20)

# min()
print(min(t))

# -----------------------------

# max()
print(max(t))

# -----------------------------

# count() - returns count of passed element from the tuple
print(t.count(10))
print(t.count(20))

# -----------------------------


# index() - returns index (first occurence) of passed element from the tuple
print(t.index(50))

# -----------------------------


# sum() - returns sum of all the elements in the passed tuple
# with single arg
print(sum(t))  # 500
# multi arg
print(sum(t, 10))  # 510
