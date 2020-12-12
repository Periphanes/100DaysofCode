#Password Generator

from random import randint
from random import choice
from random import shuffle

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
symbols = ['@','#', '$', '%', '^', '&', '*', '(', ')']

print('Welcome to the Password Generator')

num_letters = int(input("How Many letters would you like in your password?\n"))
num_symbols = int(input("How many symbols would you like in your password?\n"))
num_numbers = int(input("How many numbers would you like?\n"))
password_length = num_numbers + num_symbols + num_letters

'''
password_length = num_numbers + num_symbols + num_letters
password = ''

def letter():
	global num_letters
	if(num_letters > 0):
		let = choice(letters)
		num_letters -= 1
		return(let)
	else:
		symbol()

def symbol():
	global num_symbols
	if(num_symbols > 0):
		sym = choice(symbols)
		num_symbols -= 1
		return(sym)
	else:
		number()

def number():
	global num_numbers
	if(num_numbers > 0):
		num = str(randint(0,9))
		num_numbers -= 1
		return(num)
	else:
		letter()

'''

password = ''

for i in range(num_letters):
	let = choice(letters)
	password += let

for i in range(num_symbols):
	sym = choice(symbols)
	password += sym

for i in range(num_numbers):
	num = str(randint(0,9))
	password += num

password = list(password)

for i in range(password_length):
	swap_place = randint(0, password_length-1)
	original = password[i]
	swap_sym = password[swap_place]
	password[swap_place] = original
	password[i] = swap_sym

print(''.join(password))

'''

for i in range(password_length):
	select = randint(0,2)
	if(select == 0):
		let = letter()
		print(let)
		password += let
	elif(select == 1):
		sym = symbol()
		print(sym)
		password += sym
	else:
		num = number()
		print(num)
		password += num


print(password)

'''