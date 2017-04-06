import csv
import hashlib

def addInfo(dataString, dataTruth):
	csvfile = open('knowledgeBase.csv', 'a+')
	csvWriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
	if(not containsInfo(dataString)):
		hashVal = hashlib.md5(dataString.encode())
		csvWriter.writerow([hashVal.hexdigest(), dataTruth])
		return True
	return False

def readInfo(dataString):
	csvfile = open('knowledgeBase.csv', 'r+')
	csvReader = csv.reader(csvfile, delimiter=' ', quotechar='|')
	hashVal = hashlib.md5(dataString.encode())
	val = hashVal.hexdigest()
	for row in csvReader:
		tableVal = row[0].strip().split(',')[0]
		truthVal = row[0].strip().split(',')[1]
		if(tableVal == val):
			if(truthVal == 'True'):
				return True
			else:
				return False

def containsInfo(dataString):
	csvfile = open('knowledgeBase.csv', 'r+')
	csvReader = csv.reader(csvfile, delimiter=' ', quotechar='|')
	hashVal = hashlib.md5(dataString.encode())
	val = hashVal.hexdigest()
	for row in csvReader:
		tableVal = row[0].strip().split(',')[0]
		if(tableVal == val):
			return True
	return False

def deleteInfo(dataString):
	print "hi"
	
