from Character import Character
import random

class baseEnemy:

    def __init__(self, health, damage, xp, dead):
        self.health = health
        self.damage = damage
        self.xp = xp
        self.dead = dead


    def attack(self, target) -> None:

        if self.health == 0:
            self.dead = True

        else:
            target.health -= self.damage
            target.health = max(target.health, 0)

def create_enemys(quantity):
    enemys = []
    for _ in range(quantity):
        health = random.randint(6,9)
        damage = random.randint(1, 2)
        xp = random.randint(3,4)
        dead = False
        enemy = baseEnemy(health,damage,xp, dead)
        enemys.append(enemy)
    return enemys
first_enemys = create_enemys(10)



hero = Character(name="Hero", health=110, damage=random.randint(4,5), xp=0, dead=False)




while hero.dead == False:
    enemy_count = 0
    while enemy_count <= 10:
        hero.attack(first_enemys[enemy_count])

    input()

