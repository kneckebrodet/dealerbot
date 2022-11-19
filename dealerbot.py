## IMPORT FLASK LIBRARY FOR WEBAPPLICATION
from flask import Flask, render_template
## IMPORT RASPBERRY PI & TIME LIBRARY
import RPi.GPIO as GPIO
from time import sleep

## SETUP INPUT/OUTPUT PINS
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

## VARIABLES TO CHANGE FREQUENCY FOR DC-MOTORS
FREQWHEEL = 2000
FREQARM = 50

## SETUP PINS FOR CATERPILLAR DUALMOTORS
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

## SET DIRECTION (WHEELS) & START-POSITION
GPIO.output(engPin[0], False)
GPIO.output(engPin[1], True)
GPIO.output(engPin[2], False)
GPIO.output(engPin[3], True)
current_position = 0

## SETUP PINS FOR DEALERARM
armDir1 = 17
armDir2 = 27
armPWM = 18

GPIO.setup(armDir1, GPIO.OUT)
GPIO.setup(armDir2, GPIO.OUT)
GPIO.setup(armPWM, GPIO.OUT)
pwm = GPIO.PWM(armPWM, freqArm)
pwm.start(0)

## SET DIRECTION (ARM)
GPIO.output(armDir1, True)
GPIO.output(armDir2, False)

## DEFINE FUNCTION TO SET THE DIRECTION BEFORE MOVING
def set_direction(direction):
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

## CREATE MOVE FUNCTION
def move(currentLocation, location):
    # If current location is less than target location: move forward
    # If current location is bigger than target location: move backwards
    if currentLocation < location:
        set_direction(1)
    else:
        set_direction(0)
        
    # Get the transportation range by calculating the gap between current location and target
    location = abs(location - currentLocation)
    PWM1.ChangeDutyCycle(100)
    PWM2.ChangeDutyCycle(100)
    sleep(location*2)
    PWM1.ChangeDutyCycle(0)
    PWM2.ChangeDutyCycle(0)
    sleep(0.5)

## CREATE RETURN TO STARTPOSITION FUNCTION
def reset_position(currentposition):
    set_direction(0)
    PWM1.ChangeDutyCycle(100)
    PWM2.ChangeDutyCycle(100)
    sleep(currentposition*2)
    PWM1.ChangeDutyCycle(0)
    PWM2.ChangeDutyCycle(0)
    sleep(0.5)

## START FLASK WEBAPPLICATION
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/player/<int:player>/card/<int:card>")
def deal(player, card):
    global current_position
    # IF RESET-BUTTON IS PRESSED(card=0): RETURN TO START POSITION
    if card == 0:
        reset_position(currentposition)
        currentposition = 0
    #TAKE VALUES FROM PRESSED BUTTON, MOVE TO PLAYER
    #AND DEAL CARDS
    else:
        move(currentposition, player)
        current_position = player
    
        # DEAL CARDS
        sleep(0.5)
        pwm.ChangeDutyCycle(80)
        sleep(0.2)
        pwm.ChangeDutyCycle(0)
        sleep(0.5)
        
    return render_template("home.html")
        
app.run(debug=True, host="0.0.0.0")
