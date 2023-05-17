#!/bin/bash
if [[ -x "$(command -v python3)" ]]
then
    pyv="$(python3 -V 2>&1)"
    if [[ $pyv == "Python 3.8"* ]] || [[ $pyv == "Python 3.9"* ]] || [[ $pyv == "Python 3.10"* ]]
    then
        python3 -m venv venv
        source venv/bin/activate
        pip3 install --upgrade pip
        pip3 install -r requirements.txt
        python3 src/main.py
    else
        echo "Your python version is too old. Please update Python and try again." >&2
        exit 1
    fi 
else
    echo "You don't have python installed. Please go to https://www.python.org to download it." >&2
    exit 1
fi
