#!/bin/sh

wget https://bootstrap.pypa.io/get-pip.py
python get-pip.py
virtualenv testenv
source testenv/bin/activate
pip install selenium