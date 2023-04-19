import random

print("Welcome to the Character generator!")
print("Lets name the brave adventurers: ")

character1 = input("Character 1: ")
character2 = input("Character 2: ")
character3 = input("Character 3: ")
character4 = input("Character 4: ")
character5 = input("Character 5: ")


print("***YOUR CHARACTERS ARE COMPLETE***")
print()

role_number = random.randint(1,3)

if role_number == 1:
    char_role = "Warrior"


elif role_number == 2:
    char_role = "Wizard"
    
else:
    char_role = "Potato"



print(character1, "is a", char_role)
strength = random.randint(5,10)
magic = random.randint(5,10)
health = random.randint(5,10)

if char_role == "Warrior":
    strength *= 3

elif char_role == "Wizard":
    magic *= 3

elif char_role == "Potato":
    health *= 3

print("Strength:", strength)
print("Magic:", magic)
print("Health:", health)

print()
print("------")
print()

print(character2, "is a", char_role)
strength = random.randint(5,10)
magic = random.randint(5,10)
health = random.randint(5,10)

if char_role == "Warrior":
    strength *= 3

elif char_role == "Wizard":
    magic *= 3

elif char_role == "Potato":
    health *= 3

print("Strength:", strength)
print("Magic:", magic)
print("Health:", health)

print()
print("------")
print()

print(character3, "is a", char_role)
strength = random.randint(5,10)
magic = random.randint(5,10)
health = random.randint(5,10)

if char_role == "Warrior":
    strength *= 3

elif char_role == "Wizard":
    magic *= 3

elif char_role == "Potato":
    health *= 3

print("Strength:", strength)
print("Magic:", magic)
print("Health:", health)

print()
print("------")
print()

print(character4, "is a", char_role)
strength = random.randint(5,10)
magic = random.randint(5,10)
health = random.randint(5,10)

if char_role == "Warrior":
    strength *= 3

elif char_role == "Wizard":
    magic *= 3

elif char_role == "Potato":
    health *= 3

print("Strength:", strength)
print("Magic:", magic)
print("Health:", health)

print()
print("------")
print()

print(character5, "is a", char_role)
strength = random.randint(5,10)
magic = random.randint(5,10)
health = random.randint(5,10)

if char_role == "Warrior":
    strength *= 3

elif char_role == "Wizard":
    magic *= 3

elif char_role == "Potato":
    health *= 3

print("Strength:", strength)
print("Magic:", magic)
print("Health:", health)

print()
print("Happy Adventuring!")









