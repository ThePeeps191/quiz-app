from flask import Flask, render_template
from data import questions
import random

q = questions

app = Flask(__name__)

@app.route('/')
def homepage():
	return render_template('index.html')

@app.route('/quiz/')
def quiz():
	return render_template('quiz.html', question = random.choice(q))

@app.route('/quiz/geo/')
def quiz_geo():
  ques=[]
  for qu in q:
    if qu["type"] == "geo-can" or qu["type"] == "geo-usa":
      ques.append(qu)
  return render_template('quiz_geo.html', question = random.choice(ques))

app.run(host='0.0.0.0', port = 8080)