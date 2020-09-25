import requests
from os import walk
import time
import os
import datetime

def log(log):
    now = datetime.datetime.now()
    print(now.strftime("%Y-%m-%d %H:%M:%S")+ " : " + log)

def uploadFilles(files):
    numFiles = len(files)
    reqUrl = response = 'http://localhost:3000/api/photo?numFiles=' + str(numFiles)
    response = requests.post(reqUrl, files=files)

#uploadFilles([('userPhoto', open('./screenshots/image_1601066435.png', 'rb')), ('userPhoto', 'a2'), ('userPhoto', 'a3'), ('userPhoto', 'a4')])

def readFiles():
        f = []
        for (dirpath, dirnames, filenames) in walk('./screenshots'):
            f.extend(filenames)
            break
        if(len(f) > 0):
                files = [('userPhoto', open('./screenshots/'+fileName, 'rb')) for fileName in f]
                try:
                    uploadFilles(files)
                    for i, j in files:
                        j.close()
                        os.remove(j.name)
                    log(str(len(f)) + ' files uploaded successfully')
                except:
                    for i, j in files:
                        j.close()
                    log('Error uploading files. Check your internet connection or try again later')
        else:
                log('No files found, please check if watcher is running')
                    
        

while(True):
        time.sleep(10)
        readFiles()
        
