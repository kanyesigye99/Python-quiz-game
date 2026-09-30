#python for loops
#fruits=["apple", "pineapple","cherry"]
#for x in fruits:
#    print(x)
#restaurant ordering system
class Restaurant:
    def __init__(self):
        self.menu = {
            "Burger":5000,
            "Pizza": 8000,
            "Coke": 3000,
            "Tea": 5000,
            "Chocolate": 7000,
            "Milk": 2000,
            "Beef": 18000,
        }
        self.orders = []

    def show_menu(self):
        print("\n====ISAAC RAMS RESTAURANT====")
        print("\n==Tel: 0784746534==")
        print("\n______MENU______")
        for item, price in self.menu.items():
            print(f"{item} -- {price}")

    def order(self,item):
        if item in self.menu:
            print(f"{item} -- {price}")

    def order(self, item):
        if item in self.menu:
            self.orders.append(item)
            print(item, "added to cart.")
        else:
            print("item not available.")

    def bill(self):
        total = 0

        print("\n_______Your Order_________")
        for item in self.orders:
            print(item, "-", self.menu[item])
            total += self.menu[item]
        print("-----------")
        print("Total Bill:",total)

r = Restaurant()
while True:
    r.show_menu()

    food = input("Enter food name:")
    r.order(food)

    more = input("Order more (yes/no):")
    if more.lower() != "yes":
        break
r.bill()



