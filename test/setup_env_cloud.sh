#!/bin/sh

wget https://bootstrap.pypa.io/get-pip.py
python get-pip.py
pip install --user pipenv && pipenv install selenium
