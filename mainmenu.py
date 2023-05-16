    
import json
from boss import Boss
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
        print("2. How lucky is this calculator?")
        print("3. Store my boss stats")
        print("4. List my boss stats")
        print("5. Exit")
        return self.safe_input("What would you like to do? (enter number then press enter)\n", int)
    
    def simulate_attempts(self):
        SimulateAttempts.calculate()
        pass

    def store_boss_stats(self):
        StoreBossStats.execute(self)
        pass

    def display_boss_stats(self):
        DisplayBossStats.execute(self)
        pass

    def safe_input(self, prompt, conversion_func=None):
        readable_error = {
            'int': 'numbers',
            'float': 'numbers',
            'str': 'text'
        }

        while True:
            user_input = input(prompt)
            if user_input.lower() == "exit":
                self.exit_program()
            elif user_input.lower() == "menu":
                self.display()
            elif conversion_func:
                try:
                    converted = conversion_func(user_input)
                    if isinstance(converted, int) or isinstance(converted, float):
                        if user_input.isnumeric():
                            return converted
                        else:
                            print(f"Invalid input! - Please enter {readable_error[conversion_func.__name__]}.")
                    else:
                        if user_input.isalpha():
                            return converted
                        else: print(f"Invalid input! - Please enter {readable_error[conversion_func.__name__]} without special characters or numbers.")
                except ValueError:
                    print(f"Invalid input! - Please enter {readable_error[conversion_func.__name__]}.")
            else:
                return user_input

        # user_input = input(prompt)
        # if user_input.lower() == "exit":
        #     self.exit_program()
        # if user_input.lower() == "menu":
        #     self.display()
        # elif conversion_func:
        #     try:
        #         return conversion_func(user_input)
        #     except ValueError:
        #         print(f"Invalid input! - Please enter a {conversion_func.__name__}.")
        #         return None
        # else:
        #     return user_input
        
    
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
            print("boss_stats.json not found. Creating a new file now.")
            with open('boss_stats.json', 'w') as file:
                pass

