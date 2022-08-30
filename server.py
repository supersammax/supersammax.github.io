from flask import Flask,render_template,request, redirect
from threading import Thread
from replit import db
from random import choice

def listSplit(lst, splitter):
  out = []
  current = []
  for item in lst:
    if item == splitter:
      out.append(current)
      current = []
    else:
      current.append(item)
  out.append(current)
  return out

# i'm really proud of this formatting, not a joke this is a thing of beauty
laws = open("laws.txt", "r").read().replace("  ", " ").split("\n")
laws2 = []
for law in listSplit(laws, ""):
  laws2.append([law[0], "".join(law[1:])])

app = Flask(__name__)
 
@app.route('/')
def form():
  law = choice(laws2)
  return(render_template("form.html", name=law[0], text=law[1]))
 
def run():
  app.run(host='0.0.0.0',port=8080)

def run_server():
    t = Thread(target=run)
    t.start()