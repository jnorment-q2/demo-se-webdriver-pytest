#!/bin/sh

wget https://bootstrap.pypa.io/get-pip.py
python get-pip.py
pip install --user pipenv
echo 'Waiting for pip to install pipenv?'
pipenv install selenium
