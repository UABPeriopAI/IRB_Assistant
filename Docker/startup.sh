#!/bin/sh

#to test the package as you go
python3 -m pip install pip setuptools wheel
python3 -m pip install -e ".[dev]"

# bash check if a folder exists
# if DATASCI not exist
# then mkdir -p each of raw, intermediate, 
