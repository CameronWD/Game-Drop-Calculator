#!/bin/bash
function version_ge() { test "$(printf '%s\n' "$@" | sort -V | head -n 1)" != "$1"; }

command -v python3 &>/dev/null
if [ $? -ne 0 ]; then
    echo "Python 3 not found. Installing..."
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        sudo apt-get install python3
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        brew install python3
    else
        echo "Unknown OS type. Please install Python 3 manually."
        exit 1
    fi
fi

python_version=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:3])))')
if version_ge '3.8' $python_version; then
    echo "Python 3 is out of date. Please update it manually."
    exit 1
fi
s
python3 -m venv env
source env/bin/activate
python3 -m pip install -r requirements.txt

python3 src/main.py
