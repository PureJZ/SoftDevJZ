from flask import Flask , render_template
import requests
import json

app=Flask(__name__)

@app.route('/', methods =["GET", "POST"])
def index():
    a=requests.get('https://api.pandascore.co/videogames?token=uYeuO5nr_hf24JDGeOdjD_eeal8He0hKwdXeGkGK9rCuhCuj_uA')
    b=a.json()
    return render_template('index.html',l=b['hdurl'], m=b['explanation'])
if __name__ == '__main__':
    app.debug = True
    app.run()
