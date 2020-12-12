#Coffee Machine
#Coffee ASCII art from https://www.asciiart.eu/food-and-drinks/coffee-and-tea

#Global Variables
program_end = False

#Recipes and Required Resources
espresso = {
	"price": 1.50, #$
	"water": 50, #mL
	'coffee': 18, #g
	'milk': 0, #mL
}

latte = {
	'price': 2.50,
	'water': 200,
	'coffee': 24,
	'milk': 150,
}

cappuccino = {
	'price': 3.00,
	'water': 250,
	'coffee': 24,
	'milk': 100,
}

#Coffee Art
coffee_art = """
    (  )   (   )  )
     ) (   )  (  (
     ( )  (    ) )
     _____________
    <_____________> ___
    |             |/ _ \
    |               | | |
    |               |_| |
 ___|             |\___/
/    \___________/    \
\_____________________/

"""

#Machine Resources
machine_water = 300
machine_coffee = 100
machine_milk = 200
machine_money = 0

has_water = True
has_coffee = True
has_milk = True

def report():
	print(f"Water: {machine_water}mL")
	print(f"Coffee: {machine_coffee}g")
	print(f"Milk: {machine_milk}mL")
	print(f"Money: ${machine_money}")

def take_money(price):
	print("Please insert coins.")
	coin_quarters = int(input("How many quarters?: "))
	coin_dimes = int(input("How many dimes?: "))
	coin_nickles = int(input("How many nickles?: "))
	coin_pennies = int(input("How many pennies?: "))

	money = coin_quarters*0.25 + coin_dimes*0.10 + coin_nickles*0.05 + coin_pennies*0.01
	has_change = 0
	if money > price:
		has_change = 2
	elif money < price:
		has_change = 0
	else:
		has_change = 1

	return [round(money,2), has_change]

def resource_check(coffee):
	global machine_money
	global machine_water
	global machine_coffee
	global machine_milk

	machine_money += coffee["price"]
	machine_water -= coffee["water"]
	machine_coffee -= coffee["coffee"]
	machine_milk -= coffee["milk"]

	if(machine_milk<0 or machine_coffee<0 or machine_water<0):
		machine_money -= coffee["price"]
		machine_water += coffee["water"]
		machine_coffee += coffee["coffee"]
		machine_milk += coffee["milk"]

		return 0
	else:
		return 1



def turn():
	global program_end
	type_coffee = input("What would you like?(espresso/latte/cappuccino): ")
	if type_coffee == "espresso":
		check_espresso = resource_check(espresso)
		if check_espresso == 0:
			print("Not enough resources. Try a different menu.")
		else:
			result_espresso = take_money(espresso['price'])
			if(result_espresso[1] == 0):
				print("Not enough money. Try Again")
			elif(result_espresso[1] == 1):
				print("There is no change")
				print(coffee_art)
				print("Here is your espresso. Enjoy!")
			else:
				print(f"Here is ${result_espresso[0]} in change.")
				print(coffee_art)
				print("Here is yout espresso. Enjoy!")
	elif type_coffee == "latte":
		check_latte = resource_check(latte)
		if check_latte == 0:
			print("Not enough resources. Try a different menu.")
		else:
			result_latte = take_money(latte['price'])
			if(result_latte[1] == 0):
				print("Not enough money. Try Again")
			elif(result_latte[1] == 1):
				print("There is no change")
				print(coffee_art)
				print("Here is your latte. Enjoy!")
			else:
				print(f"Here is ${result_latte[0]} in change.")
				print(coffee_art)
				print("Here is your latte. Enjoy!")
	elif type_coffee == "cappuccino":
		check_cappuccino = resource_check(cappuccino)
		if check_cappuccino == 0:
			print("Not enough resources. Try a different menu.")
		else:
			result_cappuccino = take_money(cappuccino['price'])
			if(result_cappuccino[1] == 0):
				print("Not enough money. Try Again")
			elif(result_cappuccino[1] == 1):
				print("There is no change")
				print(coffee_art)
				print("Here is your cappuccino. Enjoy!")
			else:
				print(f"Here is ${result_cappuccino[0]} in change.")
				print(coffee_art)
				print("Here is yout cappuccino. Enjoy!")
	elif type_coffee == "report":
		report()
	elif type_coffee == "exit":
		program_end = True
	else:
		print("Unknown Input")

while(program_end == False):
	turn()

