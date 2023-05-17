$ErrorActionPreference = "Stop"

try {
    $pyv = (python --version 2>&1)
    if ($pyv -notmatch "Python 3\.[8-9]|3\.1[0-9]") {
        throw "Your python version is too old. Please update Python and try again."
    }
}
catch {
    Write-Host $_
    exit 1
}

python -m venv venv

. .\venv\Scripts\Activate.ps1

python -m pip install --upgrade pip
python -m pip install -r requirements.txt

python src\main.py

