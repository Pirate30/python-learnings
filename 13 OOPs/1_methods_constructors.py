# METHODS:

# class DemoClass:
#     x = 5

#     def func(self):
#         print('func')
#         # class variables can not be used directlu but use self.(variable name)
#         print(self.x)

# # methods with args
#     def func1(self, x):
#         print('func1', x)


# demoObj = DemoClass()
# demoObj.func()
# demoObj.func1(10)


# CONSTRUCTOR:
class DemmoClass:
    def __init__(self):
        print("in constructor")

    def func0(self):
        print("func0")


obj = DemmoClass()
obj.func0()
