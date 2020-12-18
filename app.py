import requests
from flask import Flask, render_template, request, redirect, url_for, flash, session
from api.requets_api import RequestsApi
from models.vote import Vote
import random


app = Flask(__name__)
app.secret_key = "2515navoy"


@app.route('/')
def index():
    res = RequestsApi.get_all_api()
    #print(res)
    return render_template('index.html', votes=res)


@app.route('/delete/<id>')
def delete(id):
    res = RequestsApi.delete_api(id)
    #print(res)
    return redirect(url_for('index'))


@app.route('/new')
def new():
    return render_template('create.html')


@app.route('/save', methods=['POST'])
def save():
    if request.method == 'POST':
        try:
            imgList = ['1d0', 'aqm', 'ckf', 'asm', '47c', '6mq']
            img = random.choice(imgList)
            valueInput = request.form['valueInput']
            vote = Vote(value=int(valueInput), image_id=img)
            res = RequestsApi.save_api(vote)
            #print(res)
            return redirect(url_for('index'))
        except:
            return "Not saved"

@app.route('/view/<id>')
def view(id):
    res = RequestsApi.get_one_api(id)
    #print(res)
    return render_template('view.html', vote = res)

if __name__ == '__main__':
    app.run(port=8081, debug=True)
