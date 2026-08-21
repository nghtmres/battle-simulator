from character import Character
import random

def create_characters():
    hero = Character("Hero", 100, 20, 100)
    enemy = Character("Enemy", 80, 25, 80)

    return hero, enemy
   
def start_battle():
    hero, enemy = create_characters()

    hero_defending = False
    enemy_defending = False

    heals_remaining = 2
    enemy_heals_remaining = 2

    while hero.is_alive() and enemy.is_alive():
        print(f"\nYour turn: ")
        print("1. Attack")
        print(f"2. Heal ({heals_remaining} remaining)")
        print("3. Defend")

        choice = input("Choose an action: ")

        if choice == '1':
            hero.attack_target(enemy, enemy_defending)
            enemy_defending = False
        elif choice == '2':
            if hero.health >= hero.max_health:
                print("You are already at full health!")
                continue

            if heals_remaining <= 0:
                print("No heals remaining!")
                continue
            
            heals_remaining -= 1
            healed_amount = hero.heal(30)
            print(f"{hero.name} heals for {healed_amount} health points! "
                  f"Current health: {hero.health}")
            
        elif choice == '3':
            hero_defending = True
            print(f"{hero.name} is defending!")
        else:
            print("Invalid choice.")
            continue
        if not enemy.is_alive():
            break


        enemy_heals_remaining, hero_defending, enemy_defending = enemy_turn(
            enemy, hero, enemy_heals_remaining, hero_defending, enemy_defending)

    if hero.is_alive():
        print(f"\nYou win! {enemy.name} has been defeated!")
    else:
        print(f"\nGame Over! {hero.name} has been defeated!")

def enemy_turn(enemy, hero, enemy_heals_remaining, hero_defending, enemy_defending):
    
    enemy_choice = random.choice(["attack", "heal", "defend"])


    if enemy_choice == "attack":
        enemy.attack_target(hero, hero_defending)
        hero_defending = False
    elif enemy_choice == "heal":
        if enemy.health >= enemy.max_health or enemy_heals_remaining <= 0:
            enemy.attack_target(hero, hero_defending)
            hero_defending = False
        else:
            enemy_heals_remaining -= 1
            healed_amount = enemy.heal(30)
            print(f"{enemy.name} heals for {healed_amount} health points! "
                f"Current health: {enemy.health}")
    elif enemy_choice == "defend":
        enemy_defending = True
        print(f"{enemy.name} is defending!")
    return enemy_heals_remaining, hero_defending, enemy_defending

def view_character_stats():
    hero, enemy = create_characters()

    print(f"\nCharacter Stats:")
    print(f"{hero.name} - Health: {hero.health}/{hero.max_health}, "
          f"Attack: {hero.attack - 5}-{hero.attack + 5}, "
          f"Critical Hit Chance: 15%")
    print(f"{enemy.name} - Health: {enemy.health}/{enemy.max_health}, "
          f"Attack: {enemy.attack - 5}-{enemy.attack + 5}, "
          f"Critical Hit Chance: 15%")


def main():

    while True:
        print("\nBattle Simulator")
        print("1. Start Battle")
        print("2. View Character Stats")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            start_battle()
        elif choice == '2':
            view_character_stats()
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()