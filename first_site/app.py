# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 01:34:16 2020

@author: willh
"""

import flask

app = flask.Flask(__name__)

@app.route('/')
def index():
    return "Hello world"

app.run()