class Character:

    def __init__(self, name: str, health: int, damage: int, xp: int, dead: bool) -> None:
        self.name = name
        self.health = health
        self.maxhealth = health
        self.damage = damage
        self.xp = xp
        self.dead = dead


    def attack(self, target) -> None:

        enemy_bar = (target.health//5)*"▓"


        if self.health == 0:
            self.dead = True

        else:
            target.health -= self.damage
            target.health = max(target.health, 0)
            print(f"""You deal {self.damage} in the ENEMY!
            |{enemy_bar}|            
""")
            input()
