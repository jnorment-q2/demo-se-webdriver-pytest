#!/bin/sh

wget https://bootstrap.pypa.io/get-pip.py
python get-pip.py
pip install pipenv
pipenv install selenium