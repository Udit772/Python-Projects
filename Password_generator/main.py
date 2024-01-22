# make a password generator - used LIST in python 
import random

charac = ['a', 'b', 'c', 'd']  # List of characters
num = ['0', '1', '2']  # List of numbers
symb = ['!', '@', '#']  # List of symbols

print("------------------------------- Welcome to Password Generator -------------------------------")

character = int(input("Enter the number of characters you want: "))
number = int(input("Enter the number of numbers you want: "))
symbol = int(input("Enter the number of symbols you want: "))

total_password = number + character + symbol
password = []

for i in range(character):
    password += random.choice(charac)
    
for i in range(number):
    password += random.choice(num)
    
for i in range(symbol):
    password += random.choice(symb)

random.shuffle(password)

print("\nGenerated password:", password)
total_length = character + number + symbol
print("Total length:", total_length)

final_password = "".join(password)
print("Your final password:", final_password)
print("\n\nYour password consists of:", total_password, "characters.")
print("Thank you for using our Password Generator!")