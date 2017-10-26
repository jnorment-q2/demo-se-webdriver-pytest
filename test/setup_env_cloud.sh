#!/bin/sh

curl https://bootstrap.pypa.io/get-pip.py
python get-pip.py
virtualenv testenv
source testenv/bin/activate
pip install selenium