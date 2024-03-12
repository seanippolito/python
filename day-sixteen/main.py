# from turtle import Turtle, Screen
# from prettytable import PrettyTable

# timmy = Turtle()

# timmy.shape("arrow")
# timmy.color("blue")

# for _ in range(4):
#     timmy.forward(100)
#     timmy.right(90)

# # screen = Screen()
# # screen.exitonclick()

# table = PrettyTable()
# table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
# table.add_column("Type", ["Electric", "Water", "Fire"])
# table.align = "l"
# print(table)

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_running = True
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
while is_running:

    drink = input(f"What would you like? ({menu.get_items()}): ")
    if drink == "report":
        coffee_maker.report()
        money_machine.report()
    elif drink == "latte" or drink == "espresso" or drink == "cappuccino":
        order = menu.find_drink(drink)
        if coffee_maker.is_resource_sufficient(order):
            if money_machine.make_payment(order.cost):
                coffee_maker.make_coffee(order)
                print("Enjoy your drink!")
                coffee_maker.report()
    elif drink == "off":
        is_running = False
        print("Goodbye!")
    else:
        is_running = False
        print("Invalid input.")