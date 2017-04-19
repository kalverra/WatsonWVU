import csv 
import hashlib
import StatementComparitor
import nltk

def addInfo(dataString):
	csvfile = open('knowledgeBase.csv', 'a+')
	csvWriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
	if(not containsInfo(dataString)):
		csvWriter.writerow([dataString])
		return True
	return False

def readInfo(dataString):
	csvfile = open('knowledgeBase.csv', 'r+')
	csvReader = csv.reader(csvfile, delimiter=' ', quotechar='|')
	for row in csvReader:
		tableVal = row[0]
		if(tableVal == dataString or StatementComparitor.similarity(tableVal, dataString) > 0.80):
			return True

def containsInfo(dataString):
	csvfile = open('knowledgeBase.csv', 'r+')
	csvReader = csv.reader(csvfile, delimiter='\n', quotechar='|')
	for row in csvReader:
		tableVal = row[0]
		if(tableVal == dataString or StatementComparitor.similarity(tableVal, dataString) > 0.80):
			return True
	return False
