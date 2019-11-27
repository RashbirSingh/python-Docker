#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 11:48:58 2019

@author: ubuntu
"""

#!flask/bin/python
from flask import Flask
import os

value = os.getenv("PRINT", "value does not exist")
app = Flask(__name__)

from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return value

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug=True)
