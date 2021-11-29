from flask import Flask, render_template
import json
import random

with open("static/questions.json") as f:
	q = json.load(f)["questions"]

def shuffle(l):
	random.shuffle(l)
	return l

app = Flask(__name__)

@app.route('/')
def homepage():
	return render_template('index.html')

@app.route('/play/')
def play():
	ques = random.choice(q)
	return render_template('play.html', question = ques)


app.run(host='0.0.0.0', port = 8080)