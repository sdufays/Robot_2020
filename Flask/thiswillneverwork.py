from flask import Flask, escape, request, render_template, Response
from robotClass import robot
import time
import picamera
import socket
import io
import logging
import os

app = Flask(__name__)
rc = robot()
camera = picamera.camera

#fwd 3, right 0.75, fwd 1.75, rev 0.8, right 0.75, fwd 3.05

@app.route('/streamtest')
def stream():
    x=0
    for x in range(1000000000):
        camera.capture('image.jpg')
        time.sleep(0.1)
        os.remove('image.jpg')

#<img src="image.jpg" alt="lmao alizain can't code we're all failing this project">

@app.route('/')
def home():
    return render_template("home.html")

# move the robot fwd
@app.route('/fwd', methods=['POST'])
def fwd():
    rc.forward(0.1, 30)
    return render_template("home.html")

# move the robot rev
@app.route('/rev', methods=['POST'])
def rev():
    rc.reverse(0.1, 30)
    return render_template("home.html")

# move the robot left
@app.route('/left', methods=['POST'])
def left():
    rc.left(0.05)
    return render_template("home.html")

# move the robot right
@app.route('/right', methods=['POST'])
def right():
    rc.right(0.05)
    return render_template("home.html")

# run the predetermined course
@app.route('/run')
def run():
    a = request.args.get('a')
    b = request.args.get('b')
    c = request.args.get('c')
    d = request.args.get('d')
    e = request.args.get('e')
    f = request.args.get('f')
    rc.forward(float(a), 15)
    time.sleep(0.5)
    rc.right(float(b))
    time.sleep(0.5)
    rc.forward(float(c), 15)
    time.sleep(0.5)
    rc.reverse(float(d), 15)
    time.sleep(0.5)
    rc.right(float(e))
    time.sleep(0.5)
    rc.forward(float(f), 15)
    return "robot work yes"

# @app.route('/streamlog')
# def terminal():
#     logFormatter = logging.Formatter("%(asctime)s [%(levelname)-5.5s] %(message)s")
#     rootLogger = logging.getLogger()

#     fileHandler = logging.FileHandler(loggingfile)
#     fileHandler.setFormatter(logFormatter)

#     consoleHandler = logging.StreamHandler()

#     rootLogger.addHandler(consoleHandler)
#     rootLogger.addHandler(fileHandler)


app.run(host= '0.0.0.0', port=8080)
