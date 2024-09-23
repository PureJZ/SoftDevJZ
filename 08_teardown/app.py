# your heading here

'''
DISCO:
<note any discoveries you made here... no matter how small!>
If I copy and paste the numbers of the servers into a browser, the website will have "NO Hablo Espanol"
When I changed what is in the return, the website also matches to what I changed

QCC:
0. In java, where we would create an object from a class. In this example, a Flask class.
1. This could be like going to the homepage
2. I think this will print to the console/terminal where the Flask server is running
3. I am not sure
4. I think it will appear on the website where the flask server is being runnmed
5. I have seen this in java, where we call a function of a class through an object of that class
 ...

INVESTIGATIVE APPROACH:
<We first tried seeing if we could find where the server was being hosted. We know that flask is used for websites
and we assumed it was going to be a localhost as well, so we copied and pasted the server address that was printed in the terminal.
We were able to get on the server and saw "No hablo queso!" printed on the website, and we tried changing the return
to something else to see if it would change the text and it did. We also changed the name app to something else to see
if the code would break but it didn't so it seems like app is just a variable name that could be anything.>
'''


from flask import Flask

app = Flask(__name__)                    # Q0: Where have you seen similar syntax in other langs?

@app.route("/")                          # Q1: What points of reference do you have for meaning of '/'?
def hello_world():
    print(__name__)                      # Q2: Where will this print to? Q3: What will it print?
    return "No hablo queso!"             # Q4: Will this appear anywhere? How u know?

app.run()                                # Q5: Where have you seen similar constructs in other languages?


