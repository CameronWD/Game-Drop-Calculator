from prettytable import PrettyTable
from termcolor import cprint

class BossStatDisplayer:
    def __init__(self, boss_records):
        self.boss_records = boss_records

    def execute(self):
        table = PrettyTable(["Boss", "Kill count", "Total drops"])
        for boss in self.boss_records.values():
            total_drops = sum(item['count'] for item in boss.items_dropped.values())
            table.add_row([boss.name, boss.kill_attempts, total_drops])
        cprint(table, "light_yellow")

        for boss in self.boss_records.values():
            cprint(f"\nBoss: {boss.name}, Kill count: {boss.kill_attempts}", "light_yellow", attrs=["bold"])
            item_table = PrettyTable(["Item dropped", "Count", "Drop rate"])
            for item, details in boss.items_dropped.items():
                item_table.add_row([item, details['count'], details['drop_rate']])
            cprint(item_table, "light_yellow")

        input("\nPress any key to return to the main menu\n")
