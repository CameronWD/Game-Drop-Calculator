from prettytable import PrettyTable
from termcolor import cprint

class DisplayBossStats:
    @staticmethod
    def execute(menu):

        # Creates a table that has each boss, the kill count and the total number of drops
        table = PrettyTable(["Boss", "Kill count", "Total drops"])
        for boss in menu.boss_records.values():
            total_drops = sum(item['count'] for item in boss.items_dropped.values())
            table.add_row([boss.name, boss.kill_attempts, total_drops])
        cprint(table, "light_yellow")

        # Create table for each boss's item drops
        for boss in menu.boss_records.values():
            cprint(f"\nBoss: {boss.name}, Kill count: {boss.kill_attempts}", "light_yellow", attrs=["bold"])
            item_table = PrettyTable(["Item dropped", "Count", "Drop rate"])
            for item, details in boss.items_dropped.items():
                item_table.add_row([item, details['count'], details['drop_rate']])
            cprint(item_table, "light_yellow")

        input("\nPress any key to return to the main menu\n")
