# import random
# import json
# from boss import Boss
# from mainmenu import MainMenu
# from DropCalculator import DropCalculator

# boss_records = {}


# def main():
#         main_menu = MainMenu()
#         main_menu.load_boss_records()
#         calculate = DropCalculator()

#         while True:
#             choice = main_menu.display()
#             if choice == 1:
#                 calculate.calculate()
#             elif choice == 2:
#                 main_menu.how_lucky()
#             elif choice == 3:
#                 main_menu.simulate_attempts()
#             elif choice == 4:
#                 main_menu.store_boss_stats()
#             elif choice == 5:
#                 main_menu.display_boss_stats()
#             elif choice == 6:
#                 main_menu.exit_program()
#             else:
#                 print('Invalid choice. Please enter a number from 1 to 6.')

# # def drop_chance():
# #     boss_name = boss_name.safe_input("Enter boss name:\n")
# #     if boss_name is None: return

# #     drop_rate = drop_rate.safe_input("Enter drop rate (e.g. 0.01 or 100 for a 1/100 chance):\n", float)
# #     if drop_rate is None: return
# #     if drop_rate > 1:
# #         drop_rate = 1 / drop_rate

# #     attempts = attempts.safe_input("Enter number of attempts:\n", int)
# #     if attempts is None: return

# #     success_prob = 1 - (1 - drop_rate) ** attempts
# #     print(f'There is a {drop_rate * 100:.3f}% chance per kill to receive the drop you want from {boss_name}')
# #     print(f'After {attempts} attempts, you had a {success_prob * 100:.3f}% chance of being successful at least once.')
# #     input("Press any key to return to main menu\n")

# def how_lucky():
#     # To be implemented
#     pass

# def simulate_attempts():
#     drop_rate = input("Drop rate (e.g. 0.01 for 1/100 or 100 for 1/100):\n")
#     # Convert input to float if in decimal format, otherwise calculate inverse
#     try:
#         drop_rate = float(drop_rate)
#         if drop_rate > 1:
#             drop_rate = 1 / drop_rate
#     except ValueError:
#         print("Invalid input for drop rate. Please enter a decimal or a whole number.")
#         return

#     boss_name = input("Boss name:\n")
#     simulated_successful_occurrences = int(input("Simulated successful occurrences (1-1000):\n"))
    
#     attempts_per_success = []
#     for _ in range(simulated_successful_occurrences):
#         attempts = 0
#         while random.random() >= drop_rate:
#             attempts += 1
#         attempts_per_success.append(attempts)

#     min_attempts = min(attempts_per_success)
#     max_attempts = max(attempts_per_success)
#     avg_attempts = sum(attempts_per_success) / len(attempts_per_success)

#     print(f"Program successfully got the drop {simulated_successful_occurrences} times.")
#     print(f"The fewest attempts it took was {min_attempts} and the most attempts was {max_attempts}.")
#     print(f"Average attempts to be successful was: {avg_attempts:.3f}")
#     input("Press any key to return to main menu\n")


# def store_boss_stats():
#     boss_name = input("Boss name:\n")
#     kill_attempts = int(input("How many kill attempts do you have?\n"))
#     items_dropped = {}
#     while True:
#         item_name = input("Enter the name of the item dropped, or 'done' to finish:\n")
#         if item_name.lower() == 'done':
#             break
#         item_drop_rate = float(input("Enter the drop rate of the item:\n"))
#         item_count = int(input(f"How many times have you received {item_name}?\n"))
#         items_dropped[item_name] = {'count': item_count, 'drop_rate': item_drop_rate}
#     save = input("Save? Y/N\n")
#     if save.lower() == 'y':
#         boss = Boss(boss_name, kill_attempts, items_dropped)
#         boss[boss_name] = boss
#         with open('boss_stats.json', 'w') as file:
#             json.dump({key: value.to_dict() for key, value in boss.items()}, file)
#         print(f"Boss {boss_name} saved successfully.")
#     input("Press any key to return to main menu\n")


# def display_boss_stats():
#     for boss in boss.values():
#         print(f"\nBoss: {boss.name}, Kill count: {boss.kill_attempts}, Total drops: {sum(item['count'] for item in boss.items_dropped.values())}")
#         for item, details in boss.items_dropped.items():
#             print(f"Item dropped: {item} - {details['count']}, Drop rate: {details['drop_rate']}")
#     input("\nPress any key to return to main menu\n")

# # def exit_program():
# #     print("Thank you for using Drop Chance Calculator!")
# #     exit()

# # def main():
# #     try:
# #         with open('boss_stats.json', 'r') as f:
# #             try:
# #                 boss_records.update({key: Boss.from_dict(value) for key, value in json.load(f).items()})
# #             except json.decoder.JSONDecodeError:
# #                 print("Warning: boss_stats.json is empty or not properly formatted. Continuing with an empty boss list.")
# #     except FileNotFoundError:
# #         pass  # It's okay if the file doesn't exist yet

# #     while True:
# #         choice = main_menu()
# #         if choice == 1:
# #             drop_chance()
# #         elif choice == 2:
# #             how_lucky()
# #         elif choice == 3:
# #             simulate_attempts()
# #         elif choice == 4:
# #             store_boss_stats()
# #         elif choice == 5:
# #             display_boss_stats()
# #         elif choice == 6:
# #             exit_program()
# #         else:
# #             print("Invalid choice. Please enter a number from 1 to 6.")

# # if __name__ == "__main__":
# #     main()

from mainmenu import MainMenu
from DropCalculator import DropCalculator

def main():
    main_menu = MainMenu()
    main_menu.load_boss_records()
    calculate = DropCalculator()

    while True:
        choice = main_menu.display()
        if choice == 1:
            calculate.calculate()
        elif choice == 2:
            main_menu.how_lucky()
        elif choice == 3:
            main_menu.simulate_attempts()
        elif choice == 4:
            main_menu.store_boss_stats()
        elif choice == 5:
            main_menu.display_boss_stats()
        elif choice == 6:
            main_menu.exit_program()
        else:
            print('Invalid choice. Please enter a number from 1 to 6.')

if __name__ == "__main__":
    main()


