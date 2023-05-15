# from boss import Boss
# import json

# class MainMenu:
#     def __init__(self):
#         self.boss_records = {}

#     def display(self):
#         print("Welcome to Drop Chance Calculator!")
#         print("Type 'exit' at any time to exit the program.")
#         print("Type 'menu' at any time to return to the main menu.")
#         print("1. Tell me my drop chance")
#         print("2. How lucky are you?")
#         print("3. How lucky is this calculator?")
#         print("4. Store my boss stats")
#         print("5. List my boss stats")
#         print("6. Exit")
#         return self.safe_input("What would you like to do? (enter number then press enter)\n", int)
    

#     def safe_input(self, prompt, conversion_func=None):
#         user_input = input(prompt)
#         if user_input.lower() == "exit":
#             self.exit_program()
#         if user_input.lower() == "menu":
#             self.display()
#         elif conversion_func:
#             try:
#                 return conversion_func(user_input)
#             except ValueError:
#                 print("Invalid input!")
#                 return None
#         else:
#             return user_input
        
    
#     def exit_program(self):
#         print("Thank you for using Drop Chance Calculator!")
#         exit()

#     def load_boss_records(self):
#         try:
#             with open('boss_stats.json', 'r') as file:
#                 try:
#                     self.boss_records.update({key: Boss.from_dict(value) for key, value in json.load(file).items()})
#                 except json.decoder.JSONDecodeError:
#                     print("Warning: boss_stats.json is empty or not properly formatted. Continuing with an empty boss list.")

#         except FileNotFoundError:
#             pass

    
import json
from boss import Boss
from howlucky import HowLucky
from simulateattempts import SimulateAttempts
from storebossstats import StoreBossStats
from displaybossstats import DisplayBossStats

class MainMenu:
    def __init__(self):
        self.boss_records = {}

    def display(self):
        print("Welcome to Drop Chance Calculator!")
        print("Type 'exit' at any time to exit the program.")
        print("Type 'menu' at any time to return to the main menu.")
        print("1. Tell me my drop chance")
        print("2. How lucky are you?")
        print("3. How lucky is this calculator?")
        print("4. Store my boss stats")
        print("5. List my boss stats")
        print("6. Exit")
        return self.safe_input("What would you like to do? (enter number then press enter)\n", int)
    
    def how_lucky(self):
        how_lucky = HowLucky(self)
        how_lucky.calculate()

    def simulate_attempts(self):
        SimulateAttempts.calculate(self)
        pass

    def store_boss_stats(self):
        StoreBossStats.execute(self)
        pass

    def display_boss_stats(self):
        DisplayBossStats.execute(self)
        pass

    def safe_input(self, prompt, conversion_func=None):
        user_input = input(prompt)
        if user_input.lower() == "exit":
            self.exit_program()
        if user_input.lower() == "menu":
            self.display()
        elif conversion_func:
            try:
                return conversion_func(user_input)
            except ValueError:
                print("Invalid input!")
                return None
        else:
            return user_input
        
    
    def exit_program(self):
        print("Thank you for using Drop Chance Calculator!")
        exit()

    def load_boss_records(self):
        try:
            with open('boss_stats.json', 'r') as file:
                try:
                    self.boss_records.update({key: Boss.from_dict(value) for key, value in json.load(file).items()})
                except json.decoder.JSONDecodeError:
                    print("Warning: boss_stats.json is empty or not properly formatted. Continuing with an empty boss list.")

        except FileNotFoundError:
            pass 

