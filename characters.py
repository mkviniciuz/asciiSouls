class hero:
    def __init__(self, health, damage, experience, mana) -> None:
        self.health = health
        self.damage = damage
        self.experience = experience
        self.mana = mana
        self.maxhealth = health
        self.bag = []


    def attack(self, target) -> None:
        target.health -= self.damage
        print(f"The Hero attacked and deal {self.damage} DMG in the ENEMY!")
        print(f"Enemy actual life {target.health}/{target.maxhealth}")
    
    def showBag(self) -> None:
        if not self.bag:
            print(f"Your bag is empty for now")
        else:
            print("This is your bag actually")


            
hero1 = hero(10,5,5,0)

hero1.showBag()