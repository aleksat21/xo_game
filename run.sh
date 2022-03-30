#!/usr/bin/bash

pyuic5 -x xo.ui -o xo_ui.py
pyuic5 -x beginDialog.ui -o beginDialog_ui.py
python3 main.py
