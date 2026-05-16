#!/bin/bash

python3 -m venv venv
source venv/bin/activate

pip install -r client/requirements.txt
pip install -r relay/requirements.txt
