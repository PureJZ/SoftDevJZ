# Clyde 'Thluffy' Sinclair
# SoftDev
# September 2024

from flask import Flask
app = Flask(__name__)            #create instance of class Flask

@app.route("/")                  #assign fxn to route
def hello_world():
    return "No hablo queso!"     # response to browser

app.run()
'''
No print() statement for __name__.
This will return "No hablo queso!" on the browser
without printing anything to the console
'''
