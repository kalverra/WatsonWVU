import json
import re
from os.path import join, dirname
from watson_developer_cloud import AlchemyLanguageV1

class WATSON:

	alchemy_language = None

	def __init__(self):
		self.alchemy_language = AlchemyLanguageV1(api_key='9d64e0467f09d220d4fc29cc503bf0f40ec9b73f')


	#Takes in the string of a statement and integer num, and returns a list of num keywords
	def getKeywordsStatement(self, string, num):
		keywords = []
		string = self.removeURLs(string)
		j = json.dumps(self.alchemy_language.keywords(max_items=num, text=string, language='english'), indent=2)
		data = json.loads(j)
		for row in data['keywords']:
			keywords.append(row['text'])
		
		return keywords

	#Takes in the string of a statement and integer num, and returns a list of num tuples. 
	#Each tuple consists of: (keyword : relevance score)
	def getKeywordsRelevanceStatement(self, string, num):
		keywords = []
		string = self.removeURLs(string)
		j = json.dumps(self.alchemy_language.keywords(max_items=num, text=string, language='english'), indent=2)
		data = json.loads(j)
		for row in data['keywords']:
			keywords.append((row['text'], row['relevance']))
		
		return keywords

	#Takes in the string of a url and integer num, and returns a list of num keywords
	def getKeywordsURL(self, website, num):
		keywords = []
		j = json.dumps(self.alchemy_language.keywords(max_items=num, url=website, language='english'), indent=2)
		data = json.loads(j)
		for row in data['keywords']:
			keywords.append(removeURLs(row['text']))
		return keywords

	#Takes in the string of a url and integer num, and returns a list of num tuples. 
	#Each tuple consists of: (keyword : relevance score)
	def getKeywordsRelevanceURL(self, website, num):
		keywords = []
		j = json.dumps(self.alchemy_language.keywords(max_items=num, url=website, language='english'), indent=2)
		data = json.loads(j)
		for row in data['keywords']:
			keywords.append((row['text'], row['relevance']))
		return keywords

	#Takes in the string of a url, and returns a string containing 'relatively' clean text
	#The raw text in comparison includes html notation
	def getCleanTextURL(self, website):
		keywords = []
		j = json.dumps(self.alchemy_language.text(url=website), indent=2)
		data = json.loads(j)
		return data['text']

	#Takes in a string and returns a list of all numerical figures including percentages and currency
	def getNumbersStatement(self, string):
		string = self.removeURLs(string)
		numbers =  re.findall("[\d]+[\d,.]*[\\bhundred\\b | \\bthousand\\b | \\bmillion\\b | \\bbillion\\b | \\btrillion\\b]*", string.lower())
		actual_numbers = []
		for num in numbers:
			actual_numbers.append(self.convertNums(num))
		return actual_numbers

	#Takes in a string and returns a list of all the dates present
	#Formats included: 4/4/2006 - October 26th, 1997 - 04/1996 - 2005 
	def getDatesStatement(self, string):
		string = self.removeURLs(string)
		dates = re.findall("[\d\/]*\d{4}[\s]+", string)
		for date in re.findall("[\\bjanuary\\b|\\bfebruary\\b|\\bmarch\\b|\\barpil\\b|\\bmay\\b|\\bjune\\b|\\bjuly\\b|\\baugust\\b|\\bseptember\\b|\\boctober\\b|\\bnovember\\b|\\bdecember\\b)]{1}.*?\d{4}[\s]+", string.lower()):
			dates.append(date.strip())
		return dates

	#Takes in 2 strings with integer values, removes symbols and converts them to ints, and returns whether they are within 10% of eachother
	def compareNumStrings(self, float1, float2):
		if float1 > float2:
			return((float2/float1) >= .90)
		else:
			return((float1/float2) >= .90)

	#Takes in a string and returns a string with all URLs removed
	def removeURLs(self, string):
		return re.sub(r"http\S+", "", string)
	
	#Takes in a spelled out version of a number in the format 6.2 million and returns the float/integer equivalent	
	def convertNums(self, string):
		if "hundred" in string:
			num  = float(re.sub("[^\d.]", "", string))
			return num * 100
		elif "thousand" in string:
			num  = float(re.sub("[^\d.]", "", string))
			return num * 1000
		elif "million" in string:
			num  = float(re.sub("[^\d.]", "", string))
			return num * 1000000
		elif "billion" in string:
			num  = float(re.sub("[^\d.]", "", string))
			return num * 1000000000
		elif "trillion" in string:
			num  = float(re.sub("[^\d.]", "", string))
			return num * 1000000000000
		else:
			return float(re.sub("[^\d.]", "", string))

#instantiate an instance of WATSON like so:
w = WATSON()

#You can call and get the info you want like so:

#print(w.getNumbersStatement("2,675,435  4.2 6 billion 17.72 trillion 600 thousand"))
#print(w.getDatesStatement("4/4/2006, October 26th, 1997, 04/96, 2005 http://imgur.com/2005"))
#print(w.compareNumStrings("27%", "30%"))






