class hero:
    def __init__(self, health, damage, experience, mana) -> None:
        self.health = health
        self.damage = damage
        self.experience = experience
        self.mana = mana


    def attack(self, target) -> None:
        target.health -= self.damage
        print(f"The Hero attacked and deal {self.damage}DMG in the ENEMY!")
        print(f"Enemy actual life {target.healt}/{max(target.health, 0)}")
            
hero1 = hero(10,5,0,0)
hero2 = hero(15,10,10,10)

hero1.attack(hero2)