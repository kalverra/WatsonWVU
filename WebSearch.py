import pprint
from bs4 import BeautifulSoup
from googleapiclient.discovery import build
#import urllib2
#import re
#import json
#google seach API key: AIzaSyDIwiJp6e4KTXbU_qA9ZDnvBckCEBMTDlo

def main():
	webSearch("Donald Trump")

def webSearch(keyWordString):
	numOfResults = 10
	query = keyWordString

	query = query.replace (" ", "+")

	service = build("customsearch","v1",developerKey="AIzaSyDIwiJp6e4KTXbU_qA9ZDnvBckCEBMTDlo")

	#q is the query, cx specifies the custom search, num is number of results
	#res = service.cse().list(q = query,cx="018123512344280340302:tqa4kiqukzs",num = numOfResults).execute()
	links = []
	count = 0
	#parse the josn for the desired links in the goggle search results
	while count < numOfResults:
#		links.append(res["items"][count]["link"])
		count+=1
	count = 0
	pprint.pprint(links)
	
	
	sentences = []
	keywords = []
	keywords.append("Donald")
	keywords.append("Trump")
	keywords.append("taxes")
	
	txt = "Donald is lame. he is not a good guy. I  dont like Donald Trump. Trump knows taxes. The Donald won't release his taxes. Donald Trump has paid many taxes"	#send link to watson to return String body of text.
	
	while count < 1 :
		while(len(keywords)>1):
			firstCheck = keywords.pop()
			for secondCheck in keywords:
				for sentence in txt.split('.'):
					if secondCheck in sentence and firstCheck in sentence:
						sentences.append(sentence)# adds a sentence to this list if it contains ataleast 2 or the keywords
	
				count+=1
			

#	for sentence in sentences:
		#get keywords from watson
		#compare the keywords of each sentance to the keywords of the fact we're checking
		
		
	pprint.pprint(list(set(sentences)))
	
	
	
	

#This is some code we probably can't really use, but it 
#checks each link for an exact matching string within the page
'''	
print(links)
for link in links:
	print(link.split('&sa=')[0])
	html_content = urllib2.urlopen(link.split('&sa=')[0]).read()
	matches = re.findall('This is the search string', html_content);

	if len(matches) == 0: 
		print 'I did not find anything'
	else:
		print 'My string is in the html'
'''		


if '__main__' == __name__:
	webSearch("Donald Trump")