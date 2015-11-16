#!/usr/bin/bash

cd /opt/portal
git checkout master && git pull --ff-only
bower install
. env/bin/activate
pip install -r requirements.txt
python main.py build
