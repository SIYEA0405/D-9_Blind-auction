from replit import clear
from art import logo
print(logo)

question = True
information = []

while question:
	name = input("What's your name?: ")
	price = input("How much?: $")
	next_person = input("next person? choose 'yes' or 'no': ").lower()
	def dictionary(name_value, price_value, next_person_value):
		hdd_dictionary = {}
		hdd_dictionary["name"] = name_value
		hdd_dictionary["price"] = int(price_value)
		information.append(hdd_dictionary)
	if next_person == "yes":
		dictionary(name_value=name, price_value=price, next_person_value=next_person)
		question = True
		clear()
	elif next_person == "no":
		dictionary(name_value=name, price_value=price, next_person_value=next_person)
		question = False
		clear()

zero = 0
winner = ""
for X in information:
	if X["price"] > zero:
		zero = X["price"]
		winner = X
winner_name = winner["name"]
winner_price = winner["price"]


print(logo)
print(f"The winner is {winner_name} with a bid of {winner_price}$.")

