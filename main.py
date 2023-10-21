# Import Libraries below
import os
import cv2
from flask import Flask, render_template, request, redirect, url_for, send_file
from werkzeug.utils import secure_filename
# Define flask 
app = Flask(__name__)

# Define upload_form() and route the webapp 
@app.route('/')
def upload_form():
    return render_template('upload.html')
# Define upload_video() to get video in defined folder and route the webapp  
@app.route('/', methods=['POST'])
def upload_video():
    file = request.files['file']
    filename = secure_filename(file.filename)
    file.save(os.path.join('static', filename))
    return render_template("upload.html", filename=filename)
# Define display_video() to Display video in defined folder and route the webapp  
@app.route('/display/')
def display_video(filename):
    return redirect(url_for('static', filename = filename))

if __name__ == "__main__":
    app.run()