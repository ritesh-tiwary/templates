#!/bin/bash
# Usage: source start.sh

python3 -m venv myapp-venv

source ./myapp-venv/bin/activate

python3 -m pip install --upgrade pip

python3 -m pip install --use-pep517 -qr requirements.txt
