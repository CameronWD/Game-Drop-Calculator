# import math

# class Boss:
#     def __init__(self, name, killcount, dropchance):
#         self.name = name
#         self.killcount = killcount
#         self.dropchance = dropchance

#     def LuckCalculator(self, n, p, k):
#         self.n = n
#         self.p = p
#         self.k = k
#         q = 1-p

#         chance = math.comb(n, k) * (p ** k) * (q **(n - k))
#         return chance


class MainMenu:
    def __init__(self, options):
        self.options = options

    def display_menu(self):
        print("Select an option: ")
        for item, option in enumerate(self.options):
            print(f"{item+1}. {option}")

    def get_user_choice(self):
        choice = input("Enter option: ")
        return int(choice)
