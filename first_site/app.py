# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 01:34:16 2020

@author: willh
"""

import flask

app = flask.Flask(__name__)

def main():
    register_blueprints()
    app.run()
    
def register_blueprints():
    from views import home_views
    from views import package_views
    
    app.register_blueprint(home_views.blueprint)
    app.register_blueprint(package_views.blueprint)
    
if __name__ == '__main__':
    main()