from character import Character


def create_characters():
    hero = Character("Hero", 100, 20)
    enemy = Character("Enemy", 80, 15)

    return hero, enemy
   
def start_battle():
    hero, enemy = create_characters()

    while hero.is_alive() and enemy.is_alive():
        print(f"\nYour turn: ")
        print("1. Attack")
        print("2. Heal")

        choice = input("Choose an action: ")

        if choice == '1':
            hero.attack_target(enemy)
        elif choice == '2':
            old_health = hero.health
            hero.health = min(hero.health + 10, hero.max_health)

            healed_amount = hero.health - old_health
            print(f"{hero.name} heals for {healed_amount} health points! "
                  f"Current health: {hero.health}")
        else:
            print("Invalid choice.")
            continue

        if not enemy.is_alive():
            break

        enemy.attack_target(hero)

    if hero.is_alive():
        print(f"\nYou win! {enemy.name} has been defeated!")
    else:
        print(f"\nGame Over! {hero.name} has been defeated!")

def view_character_stats():
    hero, enemy = create_characters()

    print(f"\nCharacter Stats:")
    print(f"{hero.name} - Health: {hero.health}/{hero.max_health}, "
          f"Attack: {hero.attack}")
    print(f"{enemy.name} - Health: {enemy.health}/{enemy.max_health}, "
          f"Attack: {enemy.attack}")


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