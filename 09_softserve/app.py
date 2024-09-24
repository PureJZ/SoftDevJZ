from flask import Flask
import random
import csv


app = Flask(__name__)           #create instance of class Flask

@app.route("/")                 #assign fxn to route
def numbercruncher():
    list1=[]
    percentage=[]
    job=[]
    print("the __name__ of this module is... ")
    print(__name__)
    with open('occupations.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            list1.append(row)
    for dict1 in list1:
        percentage.append(float(dict1.get("Percentage")))
    for dict1 in list1:
        job.append(dict1.get("Job Class"))
    job.pop()
    percentage.pop()
    return job
    return(random.choices(job, weights=percentage))
app2= Flask(__name__)
@app2.route("/")
def returnlist():
    list1=[]
    job=[]
    print("the __name__ of this module is... ")
    print(__name__)
    with open('occupations.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            list1.append(row)
    for dict1 in list1:
        job.append(dict1.get("Job Class"))
    job.pop()
    return job


if __name__ == "__main__":      # true if this file NOT imported
    app.debug = True            # enable auto-reload upon code change
    app.run()
    app2.run()