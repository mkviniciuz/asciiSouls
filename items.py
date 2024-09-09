import characters
from characters import hero1

#HP Potions functions
def smallpotion(target):
    target.health += 5
    print(f"You have restored +5 HP")
    print(f"actual HP: {target.health}/{target.maxhealth}")
def mediumpotion(target):
    target.health += 25
    print(f"You have restored +5 HP")
    print(f"actual HP: {target.health}/{target.maxhealth}")
def largepotion(target):
    target.health += 50
    print(f"You have restored +5 HP")
    print(f"actual HP: {target.health}/{target.maxhealth}")
def wyvernpotion(target):
    target.health += target.maxhealth
    print(f"You have restored +5 HP")
    print(f"actual HP: {target.health}/{target.maxhealth}")

#List of HP items
hpItems = {
    #Restore +5 HP for the user
    smallpotion: lambda: smallpotion(hero),
    
    #Restore +25 HP for the user
    mediumpotion: lambda: mediumpotion(hero),

    #Restore +50 HP for the user
    largepotion: lambda: largepotion(hero),

    #Restore FULL HP for the user
    wyvernpotion: lambda: wyvernpotion(hero),
    }



#MP Potions functions
def smallmppotion(target):
    target.mana += 5
    print(f"You have restored +5 MP")
    print(f"actual MP: {target.mana}/{target.maxmana}")
def mediumpotion(target):
    target.mana += 25
    print(f"You have restored +5 MP")
    print(f"actual MP: {target.mana}/{target.maxmana}")
def largepotion(target):
    target.mana += 50
    print(f"You have restored +5 MP")
    print(f"actual MP: {target.mana}/{target.maxmana}")
def hydrapotion(target):
    target.mana += target.maxmana
    print(f"You have restored +5 MP")
    print(f"actual MP: {target.mana}/{target.maxmana}")

mpItems = {
    #Restore +5 MP for the user
    'Small MP potion': lambda: smallmppotion(hero),
    
    #Restore +25 MP for the user
    'Medium MP potion': lambda: mediummppotion(hero),

    #Restore +50 MP for the user
    'Large MP potion': lambda: largemppotion(hero),

    #Restore FULL MP for the user
    'Hydra MP potion': lambda: hydrapotion(hero),
    }

hydrapotion(hero1)