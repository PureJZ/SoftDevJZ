from flask import Flask
import random
import csv


app = Flask(__name__)           #create instance of class Flask

@app.route("/")                 #assign fxn to route
def numbercruncher():
    list1=[]
    percentage=[]
    jobs=[]
    print("the __name__ of this module is... ")
    print(__name__)
    with open('occupations.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            list1.append(row)
    for dict1 in list1:
        percentage.append(float(dict1.get("Percentage")))
    for dict1 in list1:
        jobs.append(dict1.get("Job Class"))
    jobs.pop()
    percentage.pop()
    hi=(random.choices(jobs, weights=percentage))[0]
    joblist = "<table><tr><th>Job List</th></tr>"
    for job in jobs:
        joblist += "<tr><td>" + job + "</td></tr>"
    return ("China Rats plus One with Jackie Zeng, Wen Zhang, Yinwei Zhang and Traveling Team: Jackie Zeng and Chloe Wong" +"<br><br>"+"Chosen Occupation: "+str(hi) + "<br><br>"  + joblist + "</table>")


if __name__ == "__main__":      # true if this file NOT imported
    app.debug = True            # enable auto-reload upon code change
    app.run()
