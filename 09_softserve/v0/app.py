# Clyde 'Thluffy' Sinclair
# SoftDev
# September 2024

from flask import Flask
app = Flask(__name__)          # create instance of class Flask

@app.route("/")                # assign function to route
def hello_world():
    print(__name__)            # print __main__ to console 
    return "No hablo queso!"   # response to browser

app.run()                      # start Flask application
                
'''
Running this will print __main__ to the console and display
"No hablo queso!" on the browser.
'''