import requests

def uploadFilles(files):
	numFiles = len(files)
	reqUrl = response = 'http://localhost:3000/api/photo?numFiles=' + str(numFiles)
	response = requests.post(reqUrl, files=files)
	print(files)
	print(numFiles)
	print(reqUrl)
	print(str(response))

uploadFilles([('userPhoto', 'a1'), ('userPhoto', 'a2'), ('userPhoto', 'a3'), ('userPhoto', 'a4')])
