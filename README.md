# T1A3 - Terminal Application
# **Drop Chance Calculator**

## Introduction

## System REquirments

- OS - Any that can run Python (more niche OS's may have issues with certain packages running correctly but this should not effect funtionality)
- Python 3

## Dependencies

This application requires the following Python packages:

- prettytable==3.7.0
- termcolor==2.3.0
- tqdm==4.65.0
- wcwidth==0.2.6

## Installation

1. Confirm that your system has Python 3.x or higher. You can download Python from X link if you do not have it installed. You can confirm your python version in the console by running the following command:
    ``` python3 --version ```
2. Download or clone this respository to your local machine.

3. Navigate to the location of the reposityory on your local system in the terminal. 

4. Install the Python packages that are required to run this program using pip. This will install the dependesicis listed in the requirments.txt file. 

    ``` pip install -r requirments.txt ```

5. You should now be able to run the program from the terminal by running the following command:

    ``` pyton3 main.py ```

## How to use 

After starting the application you are greeted with main menu screen. Entering the number that corropsonds with the feature you would like. 

1. Calcualte Drop Chance: This option asks you to enter the boss name, the drop rate and the amount of attempts you have had. You are then shown the drop rate chance per kill and the chance of being succusful once within the amount of attmeps you have had. 
2. Simulate Drop: You can enter the name, drop rate and how many succusful attempts you would like for the program to simulate. The output displays a confirmation of the amount of succusful attempts the program ran. Displaying the lowest amount of attempts it took to be succusful as well as the most. Finally it displays the average drop rate for the simulation. 
3. Store Boss Stats: You can enter the details for a boss including name, drop rate, kill attempts and differnt items. You can enter the individual drop rate for differnt items too. 
4. Display Boss Stats: This function displays the entered boss data. It is presented in tables. One header table shows the different entered bosses with the kill counts on each one. The second group of tables shows the breakdown per boss. Breaking up individaul items withint he boss. 
5. This is the exit option. Typing exit anywhere in the program will close the program. 

## Tests

### Test Case 1: Testing the Drop Rate Calculation
Goal:

* Test 1.1: 
    ** Expected Result:

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