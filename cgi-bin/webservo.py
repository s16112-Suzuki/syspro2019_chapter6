#!/usr/bin/env python
# coding:utf-8
import cgi
import cgitb
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
servo = GPIO.PWM(2, 50)
servo.start(0.0)
def setservo(theta):
    duty = ((0.01055555555 * theta) + 1.45)/20 * 100
    servo.ChangeDutyCycle(duty)
    time.sleep(1.0)

print('Content-type: text/html; charset=UTF-8\r\n')
print('Web Servo')
print('<form action="" method ="post">')
print('角度(-90~90)を入力')
print('<input type="number" name="servo">')
print('</form>')


form =cgi.FieldStorage()
value=form.getvalue("servo")

setservo(int(value))
