from flask import Flask, escape, request
from robotClass import robot


app = Flask(__name__)

rc = robot()

@app.route('/')
def menu():
    return "we are not smart enough to have links here"


# move the robot fwd
@app.route('/fwd')
def fwd():
    rc.forward(1, 15)
    return 'moved fwd!'

# move the robot rev
@app.route('/rev')
def rev():
    rc.reverse(1, 15)
    return 'moved rev!'

# move the robot left
@app.route('/left')
def left():
    rc.left()
    return 'moved left!'

# move the robot right
@app.route('/right')
def right():
    rc.right()
    return 'moved right!'

# run the predetermined course
@app.route('/run')
def run():
    rc.forward(5, 15)
    rc.right()
    rc.forward(3, 15)
    rc.reverse(1, 15)
    rc.right()
    rc.forward(5, 15)



app.run(host= '0.0.0.0', port=8080)