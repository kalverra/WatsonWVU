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
		j = json.dumps(self.alchemy_language.keywords(max_items=num, text=string, language='english'), indent=2)
		data = json.loads(j)
		for row in data['keywords']:a
			keywords.append(row['text'])
		
		return keywords

	#Takes in the string of a statement and integer num, and returns a list of num tuples. 
	#Each tuple consists of: (keyword : relevance score)
	def getKeywordsRelevanceStatement(self, string, num):
		keywords = []
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
			keywords.append(row['text'])
		
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
		return re.findall("[$]*[\s]*[\d]+[\d,.]*[\s%]*", string)
		

		

#instantiate an instance of WATSON like so:
w = WATSON()

#You can call and get the info you want like so:

#print(w.getNumbersStatement("$5,000  700.26 5.6 % 6.7% $ 43,000,126.37"))





