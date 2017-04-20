import pprint
from python_sdk_master.WINSTON.Alchemy_Class import WATSON
import StatementComparitor
from bs4 import BeautifulSoup
from googleapiclient.discovery import build
#import urllib2
#import re
#import json
#google seach API keys:

#AIzaSyDIwiJp6e4KTXbU_qA9ZDnvBckCEBMTDlo
#AIzaSyAWQyVL1WzCLrYR7mkNSWcggNcSLfRjxVU
#AIzaSyBzReN1V9viA05Sqqo25KIrNl5oFfuQIsQ
#AIzaSyCmSI1Gd94Vy7j0oc_VDyLbEYkMnqZt9M0



def main():
	watson = WATSON()
#	pprint.pprint(watson.getKeywordsStatement("Donald Trump says he learned Obama tapped his phones from the New York Times", 10))
	print webSearch("Donald Trump New York Times Obama phones")
	
def webSearch(statement):
	watson = WATSON()
	numOfResults = 3
	sentences = []

	query = statement.replace (" ", "+")

	service = build("customsearch","v1",developerKey="AIzaSyDIwiJp6e4KTXbU_qA9ZDnvBckCEBMTDlo")

	#q is the query, cx specifies the custom search, num is number of results
	try:
		res = service.cse().list(q = query,cx="018123512344280340302:tqa4kiqukzs",num = numOfResults).execute()
		links = []
		count = 0
	
		if 'items' not in res:
			return False

		#parse the json for the desired links in the google search results
		while count < numOfResults:
			links.append(res["items"][count]["link"])
			count+=1
		count = 0
		pprint.pprint(links)

		for link in links:
			txt = watson.getCleanTextURL(link)
	#		print(txt.encode('utf-8').strip())
			keywords = statement.split(" ")
			while(len(keywords)>1):
				firstCheck = keywords.pop()
				for sentence in txt.split('.'):
					for secondCheck in keywords:
						if secondCheck in sentence and firstCheck in sentence:
							sentences.append(sentence)# adds a sentence to this list if it contains at least 2 or the keywords'''
					
		statement = statement.encode("ascii", "ignore")			
		for sentence in sentences:
			sentence = sentence.encode("ascii", "ignore")
			value = StatementComparitor.similarity(sentence, statement)
			if (value > 0.8 and watson.compareNumStrings(sentence, statement)):
				return True # we "confirmed" the fact
		return False
	except:
		pass


	


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
	main()
