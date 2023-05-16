import json
from boss import Boss
from simulateattempts import SimulateAttempts
from storebossstats import StoreBossStats
from displaybossstats import DisplayBossStats
from dropcalculator import DropCalculator
from termcolor import cprint
from inpututil import safe_input

class MainMenu:
    def __init__(self):
        self.boss_records = {}
    
    def display(self):
        cprint("Welcome to the Drop Chance Calculator!", 'light_magenta', attrs=['bold', 'underline'])
        cprint("1. Whats my chance of having a drop by now?", "light_green")
        cprint("2. Simulate drop attempts", "light_cyan")
        cprint("3. Store my boss stats", "light_blue")
        cprint("4. List my boss stats", "light_yellow")
        cprint("5. Exit", "red")
        cprint("Type 'exit' at any time to exit the program.", 'dark_grey')
        cprint("Type 'menu' at any time to return to the main menu.", "dark_grey")
        return safe_input("What would you like to do? (enter number then press enter): \n", int)
    
    def drop_calculator(self):
        DropCalculator(self).calculate()

    def simulate_attempts(self):
        SimulateAttempts(self).calculate()
        pass

    def store_boss_stats(self):
        StoreBossStats(self).execute()
        pass

    def display_boss_stats(self):
        DisplayBossStats.execute(self)
        pass

    def display_boss_stats(self):
        DisplayBossStats(self.boss_records).execute()
        pass
        
    def exit_program(self):
        print("Thank you for using Drop Chance Calculator!")
        exit()

    def load_boss_records(self):
        try:
            with open('boss_stats.json', 'r') as file:
                try:
                    self.boss_records.update({key: Boss.from_dict(value) for key, value in json.load(file).items()})
                except json.decoder.JSONDecodeError:
                    print("Warning: boss_stats.json is empty or not properly formatted. Will create a new one now.")

        except FileNotFoundError:
            print("boss_stats.json not found. Creating a new file now.")
            with open('boss_stats.json', 'w') as file:
                pass

