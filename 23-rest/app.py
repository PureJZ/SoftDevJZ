import flask from Flask , render_template
import requests
import json

app=Flask(__main__)

@app route('/', methods =["GET", "POST"])
def index():
    a=requests.get('https://api.nasa.gov/planetary/apod?api_key=i8i0oQRp50cOmZRCfMT6o7PgdI1xkNK9bCmNBAno')
    b=a.json()
    return render_template('index.html',l=b['hdurl'])
if __name__ == '__main__':
    app.debug = True
    app.run()
