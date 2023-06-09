import json
from boss import BossStore
from simulateattempts import AttemptSimulator
from storebossstats import StoreBossStats
from displaybossstats import BossStatDisplayer
from dropcalculator import DropCalculator
from termcolor import cprint
from inpututil import safe_input
from art import tprint , aprint

class MainMenu:
    def __init__(self):
        self.boss_records = {}
    
    def display(self):
        tprint("Drop Chance Calculator!")
        cprint("1. Whats my chance of having a drop by now?", "light_green")
        cprint("2. Simulate drop attempts", "light_cyan")
        cprint("3. Store my boss stats", "light_blue")
        cprint("4. Display my boss stats", "light_yellow")
        cprint("5. Exit", "red")
        cprint("Type 'exit' at any time to exit the program.", 'dark_grey')
        return safe_input("What would you like to do? (enter number then press enter): \n", int)
    
    def drop_calculator(self):
        DropCalculator(self).calculate()

    def simulate_attempts(self):
        AttemptSimulator(self).calculate()

    def store_boss_stats(self):
        StoreBossStats(self).execute()

    def display_boss_stats(self):
        BossStatDisplayer(self.boss_records).execute()
        
    def exit_program(self):
        cprint("Thank you for using Drop Chance Calculator!" , "cyan")
        aprint("sad face")
        exit()

    def load_boss_records(self):
        try:
            with open('boss_stats.json', 'r') as file:
                try:
                    self.boss_records.update({key: BossStore.from_dict(value) for key, value in json.load(file).items()})
                except json.decoder.JSONDecodeError:
                    cprint("Warning: boss_stats.json is empty or not properly formatted. Will create a new one now.", "red" ,attrs=['bold'])

        except FileNotFoundError:
            cprint("boss_stats.json not found. Creating a new file now.", "red", attrs=["bold"])
            with open('boss_stats.json', 'w') as file:
                pass

