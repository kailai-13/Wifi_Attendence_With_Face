import os
import time
import cv2
from flask import Flask, request, render_template
from multiping import MultiPing
from datetime import date, datetime
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import joblib

app = Flask(__name__)

# Define global variables and constants
kailai = ["192.168.123.153", "KAILAINATHAN"]
ironman = ["192.168.168.1", "GAUSIC"]
mentor = ["192.168.123.153", "SHERIN"]
kishan = ["192.168.123.153", "kishan"]

list1 = [mentor, kishan]
list2 = [kailai, ironman]

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
nimgs = 10

# Define utility functions
def studentsearch(ip):
    mp = MultiPing([ip])
    mp.send()
    responses, _ = mp.receive(1)
    return bool(responses)

def extract_faces(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face_points = face_detector.detectMultiScale(gray, 1.2, 5, minSize=(20, 20))
    return face_points

# Define Flask routes
@app.route('/')
def check_students():
    for depname in [list1, list2]:
        for emp in depname:
            time.sleep(2)  # Consider reducing sleep time
            EmpStatus = studentsearch(emp[0])
            if EmpStatus:
                print("Student {} Is Here - Time Stamp {}".format(emp[1], datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
                os.system('python main.py')
            else:
                print("Student {} Is Not Here - Time Stamp {}".format(emp[1], datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    return "No students found."


if __name__ == "__main__":
    app.run(debug=True)


