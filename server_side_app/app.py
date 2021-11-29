from flask import Flask, request
from worker import buildIndex
import os, json, time

app = Flask(__name__)
UPLOAD_FOLDER = 'upload'

@app.route("/upload-files", methods=['POST'])
def uploadFiles():
    if request.method == "POST":
        # print("###### app.py #######")
        file = request.files['file']
        # print(file)
        
        fileName = request.form['file_name']
        # print(fileName)

        # create the upload folder
        if not os.path.isdir(UPLOAD_FOLDER):
            os.makedirs(UPLOAD_FOLDER)
        
        # save the uploaded file
        file.save(os.path.join(UPLOAD_FOLDER,fileName))

        # create index on this file
        execTime = buildIndex(fileName)

        return str(execTime)    

    return 'OK'

@app.route("/get-freq", methods=['POST'])
def getWordFreq():
    res = []

    if (request.method == "POST"):
        start_time = time.time()

        #print("####Get Word Frequency#####")

        term = request.form['term'].lower()
        #print(term)

        # load hash tables to memory and search for the term
        # only load file-related hashtables
        idxDirPath = os.curdir + "/index"
        idxFiles = os.listdir(idxDirPath)
        #print(idxFiles)

        for idxFile in idxFiles:
            fPath = os.path.join(idxDirPath, idxFile)
            if fPath != (idxDirPath+'/globalIndex'):
                with open(os.path.join(idxDirPath, idxFile),'r') as file:
                    wordDict = json.load(file)

                    #print(len(wordDict))
                    
                    if term in wordDict:
                        freq = wordDict[term]
                        cvtFilePath = fPath.lstrip(idxDirPath).replace('#','/')
                        # print(cvtFilePath +": "+ str(freq))
                        res.append((cvtFilePath, freq))

        #print(res)

        #print(response)

        end_time = time.time()

        exec_time = end_time - start_time

        #print('Execution time: '+str(exec_time))

        res.append((str(exec_time), -1))

        response = json.dumps(res)

        return response


    return 'OK'

@app.route("/get-top-n", methods=['POST'])
def getTopN():
    res = {}

    res['wordFreqList'] = []

    if (request.method == "POST"):
        start_time = time.time()

        #print("####Get Word Frequency#####")

        nVal = int(request.form['nVal'])
        #print(nVal)

        # load hash tables to memory and search for the term
        # only load file-related hashtables
        idxDirPath = os.curdir + "/index"
        globalIdxPath = idxDirPath + '/globalIndex'
        #print(globalIdxPath)

        with open(globalIdxPath,'r') as file:
            wordDict = json.load(file)

            cnt = 0
            for entry in wordDict:
                if cnt >= nVal:
                    break
                # print("Word: "+entry[0]+", freq: "+str(entry[1]))
                res['wordFreqList'].append((entry[0],entry[1]))
                cnt += 1
        
        #print(res)

        end_time = time.time()

        exec_time = end_time - start_time

        res['exec_time'] = exec_time

        response = json.dumps(res)

        return response


    return 'OK'
