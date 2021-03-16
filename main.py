from flask import Flask, redirect, url_for, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/', defaults={'_id': None})
@app.route('/<string:_id>')
def index(_id):
    try:
        if open("summary.json", "r").read() == requests.get('https://api.covid19api.com/summary').text:return render_template('index.html', data=json.load(open("summary.json")), id=_id)
        elif not json.loads(requests.get('https://api.covid19api.com/summary').text)[success]:return render_template('index.html', data=json.load(open("summary.json")), id=_id)
        else:
            f = open('summary.json', 'w')
            f.write(requests.get('https://api.covid19api.com/summary').text)
            f.close()
            return render_template('index.html', data=json.loads(requests.get('https://api.covid19api.com/summary').text), id=_id)
    except:
        return render_template('index.html', data=json.load(open("summary.json")), id=_id)

@app.route('/iframe/confirmed', defaults={'_id': None})
@app.route('/iframe/confirmed/<string:_id>')
def confirmed(_id):
    try:return render_template('iframe/confirmed.html', data=json.loads(requests.get('https://api.covid19api.com/summary').text), _id=_id)
    except:return render_template('iframe/confirmed.html', data=json.load(open("summary.json")), _id=_id)

@app.route('/iframe/recovered', defaults={'_id': None})
@app.route('/iframe/recovered/<string:_id>')
def recovered(_id):
    try:return render_template('iframe/recovered.html', data=json.loads(requests.get('https://api.covid19api.com/summary').text), _id=_id)
    except:return render_template('iframe/recovered.html', data=json.load(open("summary.json")), _id=_id)

@app.route('/iframe/deaths', defaults={'_id': None})
@app.route('/iframe/deaths/<string:_id>')
def deaths(_id):
    try:return render_template('iframe/deaths.html', data=json.loads(requests.get('https://api.covid19api.com/summary').text), _id=_id)
    except:return render_template('iframe/deaths.html', data=json.load(open("summary.json")), _id=_id)

@app.route('/router', methods=["POST"])
def router():
    if request.form["selectid"] == "None": _id = None
    else: _id = request.form["selectid"]
    return redirect(url_for('index', _id=_id))

if __name__ == "__main__":
    app.run(host='192.168.1.95', port=80, debug=True) 