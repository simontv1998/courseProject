from flask import Flask, request
import os
from worker import buildIndex

app = Flask(__name__)
UPLOAD_FOLDER = 'upload'

@app.route("/upload-files", methods=['POST'])
def uploadFiles():
    if request.method == "POST":
        print("###### app.py #######")
        file = request.files['file']
        print(file)
        
        fileName = request.form['file_name']
        print(fileName)

        # create the upload folder
        if not os.path.isdir(UPLOAD_FOLDER):
            os.makedirs(UPLOAD_FOLDER)
        
        # save the uploaded file
        file.save(os.path.join(UPLOAD_FOLDER,fileName))

        # create index on this file
        buildIndex(fileName)
        

    return 'OK'

@app.route("/get-freq", methods=['POST'])
def getWordFreq():
    if (request.method == "POST"):
        word = request.form['word']

    return 'Ok'
