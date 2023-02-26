# we can use encapsulation to protect our data and methods from being accessed or modified by other parts of our program or by outside users.
# Encapsulation is important because it allows us to protect our data and methods from unwanted changes or access, which can help prevent bugs and improve the overall security and stability of our programs.

class Parent:
    def __init__(self):
        self.name = ""

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name


obj = Parent()

print(obj.getName())
obj.setName("dummy")
print(obj.getName())

# so here no user can directly manipulate name variable in Parent, instead they can use getters and setter (which are user defined)
