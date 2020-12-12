#TIP CALCULATOR

print("Welcome to the Tip Calculator")

bill = float(input("What was the total bill? $"))

tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
if(tip_percentage != 10 and tip_percentage != 12 and tip_percentage != 15):
	print("Please enter between 10, 12, or 15")
	exit()

num_people = int(input("How many people to split the bill? "))

personal_bill = round(bill * ((100 + tip_percentage)/100) / num_people, 2)

print(personal_bill)