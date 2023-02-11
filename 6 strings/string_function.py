s = "You know Who i am"
# lower()
# print(s.lower())  # you know who i am

# upper()
# print(s.upper())  # YOU KNOW WHO I AM

# title()
# print(s.title())  # You Know Who I Am

# capitalize()
# print(s.capitalize())  # You know who i am

# find() -> gives index number of desored character string if not found then returns -1
# print(s.find('k'))
# print(s.find('k', 5))


# index() -> same as find() except it gives error when character string not found
# print(s.index('m')) #16
# print(s.index('x')) #error


s0 = "iykyk"
s1 = "y0u kn0w wh0 1 am"
s2 = "1433000"
# isalpha() - returns true only if all the characters in string aare alphabates
# print(s0.isalpha())
# print(s1.isalpha())


# isdigit() - returns true only if all the characters in string are digits
# print(s0.isdigit())
# print(s1.isdigit())
# print(s2.isdigit())


s3 = "earth@universe"
s4 = "earth universe"
# isalnum() - returns true only if all the characters inn the string are either number or characters
# print(s0.isalnum())
# print(s1.isalnum())
# print(s2.isalnum())
# print(s3.isalnum())
# print(s4.isalnum())


# ord() -> converts character to its ascii int
# print(ord('p'))
# print(ord('y'))
# print(ord('t'))
# print(ord('h'))
# print(ord('o'))
# print(ord('n'))

# chr() -> converts integer to its ascii character
# print(chr(112))
# print(chr(121))
# print(chr(116))
# print(chr(104))
# print(chr(111))
# print(chr(110))


# format() - formats the given value and puts it in the string at the desired place
# x = 'parampara {smtng} anushashan'.format(smtng="prathishtha")
# print(x)

# x = 'parampara {} {}'.format("pratishtha", "anushashan")
# print(x)

x = "i am lacking the test {a:10} strings".format(a="yo")
y = "i am lacking the test {a:^10} strings".format(a="yo")
z = "i am lacking the test {a:>10} strings".format(a="yo")
print(x)
print(y)
print(z)
