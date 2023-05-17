# T1A3 - Terminal Application
# **Drop Chance Calculator**

# Table of Contents

1. [Links](#ImportantLinks)
2. [Introduction](#Introduction)
3. [SystemRequirments](#system-requirments)
4. [Dependencies](#Dependencies)
5. [Installation](#Installation)
6. [How To Use](#how-to-use)
7. [Tests](#tests)

## Important Links <a name="ImportantLinks"></a>

* [GitHubRepo](https://github.com/CameronWD/T1A3)
* [TrelloBoard](https://trello.com/b/3npKVqHD/t1a3-drop-rate-calculator)
* [Presentation]()
* [StyleGuide](https://peps.python.org/pep-0008/)
* [Help File]()

## Introduction <a name="Introduction"></a>

Welcome to my Python program, *Drop Chance Calculator*. 

Designed to provide simple and easy to use utility for gamers who frequently engage in boss fights where luck is an aspect of getting rewards. If you are someone who has wondered how lucky or unlucky you are currently, this program may provide you with some insight. 

Before diving into the functionality of the program, it is important to clarify some terminologies and concepts that are frequent within the world of video games. 

**Kill count:** This referes to the number of times a player has defeated a specific boss. This number is important to track as its relation to the odds of recieving certain items helps users gain insight into how lucky they are. 

**Drop:** A drop is a broad term used for items that are recieved from a boss. Similar words like loot or rewards could also be used. 

**Drop rate:** This is the probaiblity of a boss dropping a specific item when defeated. While many games have many differing mechanics surronding this certain assumptions have been made for drop rate calculations in this program. It is assumed that drop rate has no memory or 'bad luck' mechanic. Every kill attempt results in the same chance of recieving the drop. The fancier term being a series of Bernoulli trials. Often these rates can be given as a percentage or out 1/droprate, e.g 5%, 0.05 or 1/20.  Most games have a way to know what the drop rate of an item is. Which is really helpful for our purpose!

What draws many gamers to video games is the aspect of chance and earning drops from particular bosses gives an element of earning rewards which can be a satisfying, albeit frustrating at times, gameplay loop. By comparing your kill count in relation to the drop rate and the number of items you have recieved, players are able to learn more about how lucky or unlucky they are. This program allows users to see what percentile of probability they are in relation to their kill count and the drop rate of a specific item. It allows users to simulate recieveing X amount of drops from a boss, displaying the average rate the program recieved drops in addition to the luckiest and unluckiest streaks. Finally, users can store their kill count, boss names, drop rate and succusful occurances too. 

This program is desinged to be simple to use and a little bit of fun.

Best of luck!

## System Requirments <a name="System"></a>

- OS: Any that can run Python (more niche OS's may have issues with certain packages running correctly, but this should not affect functionality).
- Python 3

## Dependencies <a name="Dependencies"></a>

This application requires the following Python packages:

- prettytable==3.7.0
- termcolor==2.3.0
- tqdm==4.65.0
- wcwidth==0.2.6

## Installation and Running the Program<a name="Installation"></a>

- [Mac or Linux](helpMacLinux.md)
- [Windows](helpWindows.md)

    ``` pip install -r requirments.txt ```

5. You should now be able to run the program from the terminal by running the following command:

    ``` pyton3 main.py ```

## How to use <a name="How"></a>

After starting the application, you are greeted with the main menu screen. Enter the number that corresponds with the feature you would like to use:

1. **Calcualte Drop Chance:** This option asks you to enter the boss name, the drop rate, and the number of attempts you've made. You are then shown the drop rate chance per kill and the likelihood of being successful at least once within the number of attempts you have made.
2. **Simulate Drop:** You can enter the name, drop rate, and the number of successful attempts you would like for the program to simulate. The output displays a confirmation of the number of successful attempts the program ran, the minimum and maximum number of attempts it took to be successful, and the average drop rate for the simulation.
3. **Store Boss Stats:** You can enter the details for a boss, including name, drop rate, kill attempts, and different items. You can also enter the individual drop rate for different items.
4. **Display Boss Stats:** This function displays the entered boss data in a tabular format. One header table shows the different entered bosses with the kill counts for each one. The second set of tables shows the breakdown per boss, separating individual items within the boss.
5. **Exit option:** Typing 'exit' anywhere in the program will close it.

## Tests <a name="Test"></a>

### Test Case 1: Testing the Drop Rate Calculation
Goal:

* Test 1.1: 
     Expected Result:

* Test 1.2: 
** Expected Result:

### Test Case 2: Testing Drop Simulation
Goal:

* 1. Test 2.1: 
** Expected Result:

* 2. Test 2.2: 
** Expected Result:

### Test Case 3: Testing Boss Data Storage
Goal:

* 1. Test 3.1: 
** Expected Result:

* 2. Test 3.2: 
** Expected Result: