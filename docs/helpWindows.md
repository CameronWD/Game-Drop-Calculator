# Drop Calculator Help Document - Windows

## System Requirments 
- Operating System: Windows. Using anything older than 10 may result in some unintended issues.
- Powershell 3.0
- Python 3 installed

## Dependencies
This information is also available in the requirements.txt file

- prettytable==3.7.0
- termcolor==2.3.0
- tqdm==4.65.0
- wcwidth==0.2.6
- art==5.9
- setuptools==59.6.0

## How to Install and Run

### Automatic

1. Download or clown this repository to your local machine. 
2. Navigate to the source folder of the repository on your local system in the powershell terminal
3. Type ```.\dropcalculator.ps1``` into the powershell. This script confirms you have python installed, starts a vertiual environment, updates pip, installs dependencies and then runs the main.py.
4. The program is interacted with by typing in the terminal and pressing enter. 

### Manual

1. Confirm that your system has Python 3.8 or higher installed. You can download Python from [link](https://python.org) if you do not have it installed. You can confirm your python version in the console by running the following command: ```python3 --version```
2. Download or clone this repository to your local machine.
3. Navigate to the root location of the repository on your local system in the terminal(powershell).
4. Create a virtual environment by first inputting.
    ```python3 -m venv venv```
    then entering
    ```source venv\bin\activate```
5. Install the pip packages by entering the following.
    ```pip3 install -r requirements.txt```
6. Enter ```python3 src/main.py``` for the program to run.



## Troubleshooting

1. If you are getting an error with a permission policy you can attempt to correct this by running the following code in the powershell terminal. This allows for downloaded scripts to run, hopefully.
``` Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser ```