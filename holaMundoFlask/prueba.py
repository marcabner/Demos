from flask import Flask, json, request, jsonify
import os
import sys
import numpy as np
import cv2
import base64
import urllib.request
from selenium import webdriver
import time
import os, time
from selenium.webdriver.common.by import By
from werkzeug.utils import secure_filename

sys.path.insert(0, os.path.dirname(__file__))

app = Flask(__name__)
application = app

UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
 
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
 
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
    
@app.route("/")
def server_info():
    message = 'Hello world, Flask!'
    version = 'Python %s\n' % sys.version.split()[0]
    message = ' '.join([message, version])
    return jsonify({"message": message, "calculate": calculate()})

@app.route("/upload", methods=['POST'])
def upload_file():
    # check if the post request has the file part
    if 'files[]' not in request.files:
        resp = jsonify({'message' : 'No file part in the request'})
        resp.status_code = 400
        return resp
 
    files = request.files.getlist('files[]')
     
    errors = {}
    success = False
     
    for file in files:      
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            success = True
        else:
            errors[file.filename] = 'File type is not allowed'
 
    if success and errors:
        errors['message'] = 'File(s) successfully uploaded'
        resp = jsonify(errors)
        resp.status_code = 500
        return resp
    if success:
        image_as_text = read_convert_image(file.filename)
        resp = jsonify({'message' : 'Files successfully uploaded', 'savedFile' : file.filename, 'imageAsText' : image_as_text})
        resp.status_code = 201
        return resp
    else:
        resp = jsonify(errors)
        resp.status_code = 500
        return resp

@app.route("/notificarEvento", methods=['POST'])
def notificar_evento():
    driver = webdriver.Chrome(executable_path=r"C:\SW\chromedriver_win32\chromedriver.exe")
    message = 'Automatizacion de mensajes whatsApp con Selenium y Flask!'
    version = 'Python %s\n' % sys.version.split()[0]
    message = ' '.join([message, version])
    driver.get("https://web.whatsapp.com/")
    time.sleep(10)

    celular = "5215517791884"
    mensaje = "Hola, mi primer BOT con Selenium."

    driver.get("https://wa.me/" + celular + "?text=" + mensaje)
    time.sleep(5)

    btn = driver.find_element(By.ID, "action-button")
    btn.click()
    time.sleep(5)
    btn = driver.find_element(By.XPATH, "//*[@id='fallback_block']/div/div/h4[2]/a")
    btn.click()
    time.sleep(30)

    # boton enviar                        //*[@id='main']/footer/div[1]/div[3]
    btn = driver.find_element(By.XPATH, "//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[2]")
    btn.click()
    time.sleep(5)

    print("-- Fin de Bot--")

    time.sleep(180)

    driver.get("https://web.whatsapp.com/")
    time.sleep(10)

    celular = "5215527631812"
    mensaje = "*Hola, mi primer BOT con Selenium.*"

    driver.get("https://wa.me/" + celular + "?text=" + mensaje)
    time.sleep(5)

    btn = driver.find_element(By.ID, "action-button")
    btn.click()
    time.sleep(5)
    btn = driver.find_element(By.XPATH, "//*[@id='fallback_block']/div/div/h4[2]/a")
    btn.click()
    time.sleep(30)

    # boton enviar                        //*[@id='main']/footer/div[1]/div[3]
    btn = driver.find_element(By.XPATH, "//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[2]")
    btn.click()
    time.sleep(5)

    print("-- Fin de Bot--")

    time.sleep(180)

    driver.close()

    return jsonify({"message": message, "calculate": calculate()})

def calculate():
    v1 = np.array([123, 456, 789])
    v2 = 0.5 * v1
    return np.arccos(v1.dot(v2)/(np.linalg.norm(v1)*np.linalg.norm(v2)))

def read_convert_image(fname):
    path = './static/uploads/' + fname
    img = cv2.imread(path, 0)
    img_str = base64.b64encode(cv2.imencode('.jpg', img)[1]).decode()
    cv2.imwrite('./static/uploads/gray_' + fname, img)
    return img_str

if __name__ == "__main__":
    app.run()

