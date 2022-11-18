from flask import Flask, render_template
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
freqWheel = 2000
freqArm = 50

#SETUP CATERPILLAR MOTOR PINS:
engPin = [5, 6, 20, 13]
pwmPin = [19, 12]

for pin in engPin:
    GPIO.setup(pin, GPIO.OUT)
for pin in pwmPin:
    GPIO.setup(pin, GPIO.OUT)
PWM1 = GPIO.PWM(pwmPin[0], freqWheel)
PWM2 = GPIO.PWM(pwmPin[1], freqWheel)
PWM1.start(0)
PWM2.start(0)

GPIO.output(engPin[0], False)
GPIO.output(engPin[1], True)
GPIO.output(engPin[2], False)
GPIO.output(engPin[3], True)
currentposition = 0

#SETUP PINS (CARD ARM)
armDir1 = 17
armDir2 = 27
armPWM = 18

GPIO.setup(armDir1, GPIO.OUT)
GPIO.setup(armDir2, GPIO.OUT)
GPIO.setup(armPWM, GPIO.OUT)
pwm = GPIO.PWM(armPWM, freqArm)
pwm.start(0)

GPIO.output(armDir1, True)
GPIO.output(armDir2, False)

def setdirection(direction):
    if direction == 1:
        GPIO.output(engPin[0], True)
        GPIO.output(engPin[1], False)
        GPIO.output(engPin[2], True)
        GPIO.output(engPin[3], False)
    elif direction == 0:
        GPIO.output(engPin[0], False)
        GPIO.output(engPin[1], True)
        GPIO.output(engPin[2], False)
        GPIO.output(engPin[3], True)
        
    else:
        print("Valid direction wasn't set")
    

def move(currentLocation, location):
    if currentLocation < location:
        setdirection(1)
    else:
        setdirection(0)
    location = abs(location - currentLocation)
    """for i in range(1,101):
        PWM1.ChangeDutyCycle(i)
        PWM2.ChangeDutyCycle(i)"""
    PWM1.ChangeDutyCycle(100)
    PWM2.ChangeDutyCycle(100)
    sleep(location*2)
    PWM1.ChangeDutyCycle(0)
    PWM2.ChangeDutyCycle(0)
    sleep(1)
    
def resetposition(currentposition):
    setdirection(0)
    for i in range(1,101):
        PWM1.ChangeDutyCycle(i)
        PWM2.ChangeDutyCycle(i)
    sleep(currentposition*2)
    PWM1.ChangeDutyCycle(0)
    PWM2.ChangeDutyCycle(0)
    sleep(1)

#START FLASK WEBSERVER
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("home.html")

####"ifconfig + :5000/player/1/card/1/currentposition/0####
@app.route("/player/<int:player>/card/<int:card>")
def deal(player, card):
    global currentposition
        #RESET POSITION
    if card == 0:
        resetposition(currentposition)
        currentposition = 0
    #MOVE TO PLAYER    

    else:
        move(currentposition, player)
        currentposition = player
    
    #DEAL CARDS
    sleep(0.5)
    pwm.ChangeDutyCycle(80)
    sleep(0.2)
    pwm.ChangeDutyCycle(0)
    sleep(0.5)
        
    return render_template("home.html")
        
app.run(debug=True, host="0.0.0.0")
