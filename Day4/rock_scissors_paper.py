#Rock Scissors Paper
#ASCII Art from https://gist.github.com/wynand1004/b5c521ea8392e9c6bfe101b025c39abe

from random import randint

user_input = input("Whar do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n")
if(user_input != "0" and user_input != "1" and user_input != "2"):
	print("Please choose between 0,1 and 2")
	exit()

computer_input = str(randint(0,2))

def rsp_art(rsp):
	if(rsp == "0"):
		print("""
		    _______
		---'   ____)
		      (_____)
		      (_____)
		      (____)
		---.__(___)
		""")

	elif(rsp == "1"):
		print("""
		     _______
		---'    ____)____
		           ______)
		          _______)
		         _______)
		---.__________)
		""")

	elif(rsp == "2"):
		print("""
		    _______
		---'   ____)____
		          ______)
		       __________)
		      (____)
		---.__(___)
		""")

print("\n")
rsp_art(user_input)
print("\nComputer chose: \n")
rsp_art(computer_input)
print("\n")

if(user_input == computer_input):
	print("It's a tie!")
elif((user_input == "0" and computer_input == "1") or (user_input == "1" and computer_input == "2") or (user_input == "2" and computer_input == "0")):
	print("You lose")
else:
	print("You Win!!")