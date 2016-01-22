def getDevKey():
	with open('developerkey.txt','r') as file:
		return file.readlines()[0]