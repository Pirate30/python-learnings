# INHERITANCE
# You can create a class (like a bin) that contains common features or behavior, and then create sub-classes (like bins within the "vehicle" bin) that inherit those common features. The sub-classes can also add their own unique features or behavior.
# Synt: SubClass(SuperClaa)


# class Vehical:
#     def __init__(self, wheelsNum):
#         self.wheelsNum = wheelsNum

#     def drive(self):
#         print("vehical driving")


# class Car(Vehical):
#     def __init__(self):
#         super().__init__(wheelsNum=4)

#     def honk(self):
#         print("Beep beep!")


# class Truck(Vehical):
#     def __init__(self, extraWheels):
#         self.extraWheels = extraWheels
#         super().__init__(wheelsNum=6)

#     def tow(self):
#         print("The truck is towing.")

# # ? Multlevel Inheritance


# class SmallTruck(Truck):
#     def __init__(self, extraWheels):
#         super().__init__(extraWheels)

# # here wheelNum (which is property of vehical) is inherited by the other classes like car and truck


# car = Car()
# truck = Truck(extraWheels=3)
# smTruck = SmallTruck(extraWheels=2)

# print(car.wheelsNum)
# print(truck.wheelsNum, truck.extraWheels)
# print(smTruck.wheelsNum, smTruck.extraWheels)

# -------------------------------------------------------
# ? Multiple Inheritance
class A:
    def displayA(self):
        print("A")


class B:
    def displayB(self):
        print("B")


class C(A, B):
    def displayC(self):
        print("c")


obj = C()
obj.displayA()
obj.displayB()
obj.displayC()
