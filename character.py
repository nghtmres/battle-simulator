import random

class Character:
    def __init__(self, name, health, attack, max_health=100):
        self.name = name
        self.health = health
        self.attack = attack
        self.max_health = max_health

    def heal(self, amount):
        old_health = self.health
        self.health = min(self.health + amount, self.max_health)
        healed_amount = self.health - old_health
        return healed_amount

    def is_alive(self):
        return self.health > 0

    def attack_target(self, target, defending=False):
        damage = random.randint(self.attack - 5, self.attack + 5)

        if random.random() < 0.15:
            damage *= 2      
            critical = True         
        else:    
            critical = False
            
        if defending:
            damage //= 2
            print(f"{target.name} blocks part of the attack!")

        if critical:
            print(f"CRITICAL HIT! {self.name} attacks "
                f"{target.name} for {damage} damage!")
        else:
            print(f"{self.name} attacks "
                f"{target.name} for {damage} damage!")

        target.health -= damage
        print(f"{target.name}'s HP: {max(target.health, 0)}/{target.max_health}.")