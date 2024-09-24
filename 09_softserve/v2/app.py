# Clyde 'Thluffy' Sinclair
# SoftDev
# September 2024

from flask import Flask
app = Flask(__name__)             #create instance of class Flask

@app.route("/")                   #assign fxn to route
def hello_world():
    print("about to print __name__...")
    print(__name__)               #where will this go? print __main__ to console
    return "No hablo queso!"      #response to browser

app.run()
'''
The browser still returns "No hablo queso!".
Prints "about to print ___name___..." before printing __main__.
'''
