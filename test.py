import KnowledgeManagement
import csv
from python_sdk_master.WINSTON.Alchemy_Class import WATSON

csvfile = open('economic_statements.csv', 'ra+')
csvReader = csv.reader(csvfile, delimiter=',', quotechar='|')
w = WATSON() 
for row in csvReader:
	print row
	data = row[0].strip().split(',')[0]
	print data
	truth = row[1].strip().split(',')
	print truth
	if("True" in truth):
		keywords = w.getKeywordsStatement(data, len(data)/2)
		numbers = w.getNumbersStatement(data)
		add = ''
		for words in keywords:
			add = add +' '+ words
		for number in numbers:
			add = add  + ' ' + number
		KnowledgeManagement.addInfo(add)
