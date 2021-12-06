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
  question=random.choice(q)
  question["answers"]=random.sample(question["answers"],len(question["answers"]))
  return render_template('quiz.html', question = question)

@app.route('/quiz/geo/')
def quiz_geo():
  ques=[]
  for qu in q:
    if qu["type"] == "geo-can" or qu["type"] == "geo-usa" or qu["type"] == "geo-eur" or qu["type"] == "geo":
      ques.append(qu)
  question=random.choice(ques)
  question["answers"]=random.sample(question["answers"],len(question["answers"]))
  return render_template('quiz.html', question = question)

@app.route('/quiz/geo/can/')
def quiz_geo_can():
  ques=[]
  for qu in q:
    if qu["type"] == "geo-can":
      ques.append(qu)
  question=random.choice(ques)
  question["answers"]=random.sample(question["answers"],len(question["answers"]))
  return render_template('quiz.html', question = question)

@app.route('/quiz/geo/usa/')
def quiz_geo_usa():
  ques=[]
  for qu in q:
    if qu["type"] == "geo-usa":
      ques.append(qu)
  question=random.choice(ques)
  question["answers"]=random.sample(question["answers"],len(question["answers"]))
  return render_template('quiz.html', question = question)

@app.route('/quiz/geo/eur/')
def quiz_geo_eur():
  ques=[]
  for qu in q:
    if qu["type"] == "geo-eur":
      ques.append(qu)
  question=random.choice(ques)
  question["answers"]=random.sample(question["answers"],len(question["answers"]))
  return render_template('quiz.html', question = question)

@app.route('/quiz/hist/')
def quiz_hist():
   ques=[]
   for qu in q:
     if qu["type"] == "hist" or qu["type"] == "hist-can" or qu["type"] == "hist-usa":
       ques.append(qu)
   question=random.choice(ques)
   question["answers"]=random.sample(question["answers"],len(question["answers"]))
   return render_template('quiz.html', question = question)

@app.route('/quiz/hist/can/')
def quiz_hist_can():
  ques=[]
  for qu in q:
    if qu["type"] == "hist-can":
      ques.append(qu)
  question=random.choice(ques)
  question["answers"]=random.sample(question["answers"],len(question["answers"]))
  return render_template('quiz.html', question = question)

@app.route('/quiz/hist/usa/')
def quiz_hist_usa():
  ques=[]
  for qu in q:
    if qu["type"] == "hist-usa":
      ques.append(qu)
  question=random.choice(ques)
  question["answers"]=random.sample(question["answers"],len(question["answers"]))
  return render_template('quiz.html', question = question)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

app.run(host='0.0.0.0', port = 8080)
