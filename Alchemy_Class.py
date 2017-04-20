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
			keywords.append(removeURLs(row['text'])
		
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
		return re.findall("[$]*[\s]*[\d]+[\d,.]*[\s%]*", string)

	#Takes in a string and returns a list of all the dates present
	#Formats included: 4/4/2006 - October 26th, 1997 - 04/1996 - 2005 
	def getDatesStatement(self, string):
		string = self.removeURLs(string)
		dates = re.findall("[\d\/]*\d{4}", string)
		for date in re.findall("[\\bjanuary\\b|\\bfebruary\\b|\\bmarch\\b|\\barpil\\b|\\bmay\\b|\\bjune\\b|\\bjuly\\b|\\baugust\\b|\\bseptember\\b|\\boctober\\b|\\bnovember\\b|\\bdecember\\b)]{1}.*?\d{4}", string.lower()):
			dates.append(date)
		return dates

	#Takes in 2 strings with integer values, removes symbols and converts them to ints, and returns whether they are within 10% of eachother
	def compareNumStrings(self, string1, string2):
		num1 = int(re.sub("[^\d]", "", string1))
		num2 = int(re.sub("[^\d]", "", string2))
		if num1 > num2:
			return((num2/num1) >= .90)
		else:
			return((num1/num2) >= .90)

	#Takes in a string and returns a string with all URLs removed
	def removeURLs(self, string):
		return re.sub(r"http\S+", "", string)
		

#instantiate an instance of WATSON like so:
w = WATSON()

#You can call and get the info you want like so:

#print(w.getDatesStatement("4/4/2006, October 26th, 1997, 04/96, 2005 http://imgur.com/2005"))
#print(w.compareNumStrings("27%", "30%"))





