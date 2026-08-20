

class Character:
    def __init__(self, name, health, attack, max_health=100):
        self.name = name
        self.health = health
        self.attack = attack
        self.max_health = max_health

    def is_alive(self):
        return self.health > 0

    def attack_target(self, target):
        target.health -= self.attack
        print(f"{self.name} attacks {target.name} for {self.attack} damage!")