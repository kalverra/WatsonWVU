import csv

csvfileRead = open('statements.csv')
csvfileWrite = open('cleanedstatements.csv', 'w+')
csvWriter = csv.writer(csvfileWrite)
csvReader = csv.reader(csvfileRead)

for row in csvReader:
	sentence = row[0]
	print sentence
	csvWriter.writerow([sentence])
