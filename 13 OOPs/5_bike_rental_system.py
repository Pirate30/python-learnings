class BikeShop:
    def __init__(self, availableStock):
        self.availableStock = availableStock

    def getAvailableBikes(self):
        print("availale stock", self.availableStock)

    def rentCalc(self, qty):
        if qty <= 0:
            print("enter a positive value")
        elif qty == 0:
            print("0")
        elif qty > self.availableStock:
            print("not in stock")
        else:
            self.availableStock = self.availableStock - qty
            print("total price", qty*100)
            print("now avalable bikes", self.availableStock)


# bikeShop = BikeShop(100)
# bikeShop.getAvailableBikes()
# bikeShop.rentCalc(1000)

while True:
    bikeShop = BikeShop(100)
    ipt = int(input('''
    1 Get Available Stock   
    2 Rent Bike
    3 Exit
    '''))

    if ipt == 3:
        break
    elif ipt == 1:
        bikeShop.getAvailableBikes()
    elif ipt == 2:
        n = int(input("enter the qty"))
        bikeShop.rentCalc(n)
    else:
        print("input is invalid")
