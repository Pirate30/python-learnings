# we can use polymorphism to create different behaviors or outputs using the same method or function, depending on the input or context.
# We can do this by defining a class (like a crayon) that contains methods, and then creating subclasses (like different colors of crayons) that inherit those methods and can modify or extend them as needed.
# same function name but can be used in different ways depending on the context

class Animal:
    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        return "Woof!"


class Cat(Animal):
    def make_sound(self):
        return "Meow!"


dog = Dog()
cat = Cat()

print(dog.make_sound())
print(cat.make_sound())


# ------------------------------------------------

# function overloading: when we define multiple functions with the same name, but with different parameters. It's like having different toys that look similar but perform different actions.

# def play(ball):
#     print("Throwing the ball!")


# def play(truck):
#     print("Driving the truck!")


# def play(doll):
#     print("Dressing up the doll!")

# ? EG
class Area:
    def findArea(self, l=None, w=None):
        if (l != None and w != None):
            print("area", l*w)
        elif (l != None):
            print("area", l*l)
        else:
            print("lol")


obj = Area()
obj.findArea(5, 6)  # area 30
obj.findArea(5)  # area 25
obj.findArea()  # lol
# --------------------------------------------------

# function overriding: when we create a new function with the same name as an existing function in a parent class, but with a different implementation in the child class. It's like having a toy that looks similar to another toy, but performs a different action.


class Toy:
    def play(self):
        print("Playing with the toy!")


class Truck(Toy):
    def play(self):
        print("Driving the truck!")


obj = Truck()
obj.play()  # Driving the truck!

# "Truck" class inherits the "play" method from the "Toy" class, but overrides it with a new implementation that prints "Driving the truck!" instead of "Playing with the toy!".
