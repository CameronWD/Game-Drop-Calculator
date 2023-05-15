# from numpy import random

# x = random.binomial(n=10, p=0.5, size = 1000)

# x.sort()

# print(x)
# # print("Smallest value is:", x[0])

# import boss_details

# ### drop chance

# boss = str(input('What is the name of the boss?: '))
# kc = int(input('What is your kill count?: '))
# dc = int(input('What is the drop chance of the item?: '))

# dropchance = boss_details.Boss(boss, kc, dc)

# dropchance.LuckCalculator(boss, kc, dc)

# print (dropchance.__dict__)
# ## How lucky are you


# ## Simulate attempts


# ## store boss info

import boss_details

options = [
    "Drop chance calculator", 
    "How lucky are you?", 
    "Simulate attempts",
    "Store boss stats"
    ]

menu = MainMenu(options)

menu.display_menu()
user_choice = menu.get_user_choice()

print(f"You have selected option {user_choice}: {options[user_choice-1]}")