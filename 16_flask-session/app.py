# Wen Zhang, Yinwei Zhang, Jackie Zeng
# Made In China
# SoftDev
# K16 <Flask Forms, Cookies>
# 2024-10-8
# Time Spent : 2 Hours

from flask import Flask, request, render_template, make_response

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    username = request.cookies.get('username')
    if username:
        return render_template('response.html', username=username, request="Already Logged In")
    return render_template('login.html')

@app.route('/response', methods=['GET', 'POST'])
def greetings_page():
    if request.method == 'POST':
        username = request.form['username']
        response = make_response(render_template('response.html', username=username, request="POST"))
        response.set_cookie('username', username)
        return response
    else:
        username = request.args.get('username')
        response = make_response(render_template('response.html', username=username, request="GET"))
        response.set_cookie('username', username)
        return response

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_response = make_response(render_template('logout.html'))
    logout_response.delete_cookie('username')
    return logout_response

if __name__ == '__main__':
    app.debug = True
    app.run()
