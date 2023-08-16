from dataclasses import dataclass

@dataclass
class CoffeeMaker:
    water: int  = 1000
    milk: int   = 1000
    coffee: int = 1000    

    def ingredient_report(self):
        print(f"Water: {self.water}ml")
        print(f"Milk: {self.milk}ml")
        print(f"Coffee: {self.coffee}g")
    
    def check_resources(self, water, milk, coffee):
        if self.water >= water and self.milk >= milk and self.coffee >= coffee:
            return True
        else:
            return False
        
    def make_coffee(self, cap_water, cap_milk, cap_coffee):
        self.water  -= cap_water
        self.milk   -= cap_milk
        self.coffee -= cap_coffee

    


class Latte(CoffeeMaker):
    latte_use_water: int  = 200
    latte_use_milk: int   = 150
    latte_use_coffee: int = 25
    latte_price: int      = 75

    def make_latte(self):
        if self.check_resources(self.latte_use_water, self.latte_use_milk, self.latte_use_coffee):
            self.make_coffee(self.latte_use_water, self.latte_use_milk, self.latte_use_coffee)
            print(f"Here is your latte. Enjoy!")
        else:
            print("Sorry, not enough ingredients.")

class Espresso(CoffeeMaker):
    espresso_use_water: int  = 50
    espresso_use_milk: int   = 0
    espresso_use_coffee: int = 18
    espresso_price: int      = 50

    def make_espresso(self):
        if self.check_resources(self.espresso_use_water, self.espresso_use_milk, self.espresso_use_coffee):
            self.make_coffee(self.espresso_use_water, self.espresso_use_milk, self.espresso_use_coffee)
            print(f"Here is your espresso. Enjoy!")
        else:
            print("Sorry, not enough ingredients.")

class Cappuccino(CoffeeMaker):
    cappuccino_use_water: int  = 250
    cappuccino_use_milk: int   = 50
    cappuccino_use_coffee: int = 24
    cappuccino_price: int      = 80

    def make_cappuccino(self):
        if self.check_resources(self.cappuccino_use_water, self.cappuccino_use_milk, self.cappuccino_use_coffee):
            self.make_coffee(self.cappuccino_use_water, self.cappuccino_use_milk, self.cappuccino_use_coffee)
            print(f"Here is your cappuccino. Enjoy!")
        else:
            print("Sorry, not enough ingredients.")

@dataclass
class MoneyMachine:
    money100b : int = 0
    money50b  : int = 0
    money20b  : int = 0
    money10b  : int = 0
    money5b   : int = 0
    mymonney : int = 0

    def total_money(self):
        total = self.money100b*100 + self.money50b*50 + self.money20b*20 + self.money10b*10 + self.money5b*5
        return total

    def keep_money(self, coffee_price):
        self.mymonney += coffee_price


class Report(CoffeeMaker, MoneyMachine):
    def report(self):
        print(f"Water: {self.water}ml")
        print(f"Milk: {self.milk}ml")
        print(f"Coffee: {self.coffee}g")
        print(f"Money: {self.mymonney} bath")
    


customer = input("What would you like? (espresso/latte/cappuccino): ")

if customer == "report":
    customerA = Report()
    customerA.report()
elif customer == "off":
    print("Machine is off.")
elif customer == "espresso" or customer == "latte" or customer == "cappuccino":
    if customer == "espresso":
        customerA = Espresso()
        coffee_price = customerA.espresso_price
    if customer == "latte":
        customerA = Latte()
        coffee_price = customerA.latte_price
    if customer == "cappuccino":
        customerA = Cappuccino()
        coffee_price = customerA.cappuccino_price

    print(f"Please insert coins.")
    money100b = int(input("How many 100 bath coins?: "))
    money50b  = int(input("How many 50 bath coins?: "))
    money20b  = int(input("How many 20 bath coins?: "))
    money10b  = int(input("How many 10 bath coins?: "))
    money5b   = int(input("How many 5 bath coins?: "))
    money = MoneyMachine(money100b, money50b, money20b, money10b, money5b)
    if money.total_money() < coffee_price:
        print("Sorry, that's not enough money. Money refunded.")
    elif money.total_money() >= coffee_price:
        total_money = money.total_money()-coffee_price
        money.keep_money(coffee_price)
        print(f"Here is {total_money} bath in change.")
        print(f"Here is your {customer}. Enjoy!")








