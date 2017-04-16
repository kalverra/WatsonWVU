import pprint
from bs4 import BeautifulSoup
from googleapiclient.discovery import build
#import urllib2
#import re
#import json
#google seach API key: AIzaSyDIwiJp6e4KTXbU_qA9ZDnvBckCEBMTDlo

def webSearch(keyWordString):
	numOfResults = 10
	query = keyWordString

	query = query.replace (" ", "+")

	service = build("customsearch","v1",developerKey="AIzaSyDIwiJp6e4KTXbU_qA9ZDnvBckCEBMTDlo")

	#q is the query, cx specifies the custom search, num is number of results
	res = service.cse().list(q = query,cx="018123512344280340302:tqa4kiqukzs",num = numOfResults).execute()
	links = []
	count = 0
	#parse the josn for the desired links in the goggle search results
	while count < numOfResults:
		links.append(res["items"][count]["link"])
		count+=1
	count = 0
	pprint.pprint(links)
	
	
#	while count < numOfResults:
		
		#send link to watson to return weighted keywords to check against fact keywords

		#compare two sets of keywords against eachother semantically
		
		
		
   
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