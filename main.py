import TwitterOAuthTool
import time
import SVM
import re
import KnowledgeManagement
import KnowledgeBase
import WebSearch
import StatementComparitor
from Alchemy_Class import WATSON

if '__main__' == __name__:
    #Instantiate important abjects
    tool = TwitterOAuthTool.TwittTool()
    svm = SVM.SVM('cleanedTrainingStatements.csv', 1000)
    wat = WATSON() 
    #Authorize the twitter bot
    auth_url = tool.get_authorization_url()
    print 'Visit the following url in a web-browser & authorize this app to access your twitter account.'
    print 'Once you are done authorizing, copy the PIN that twitter generates and paste it below.'
    print '\nURL: %s' %auth_url
    verifier_code = raw_input('PIN: ')
    (token, secret) = tool.get_token_and_secret(verifier_code)
    if (token and secret):
        me = tool.verify_authorization()
        print 'User @%s successfully authorized the app.' %me.screen_name
    else:
	print 'Failed to get the key and secret for the user.'
    tool.prepare_api()
    #Main loop of program
    prevStatus = ""
    while(True):
	#Reading in most recent status
	statuses = tool.read_timeline(1)
	status = statuses.next()
	author = tool.get_status_author(status)
	print author.id
	statusText = tool.get_status_text(status)
	if(statusText != prevStatus):
		#Start analyzing the new status
		statusText = re.sub('\@[^\s]+','', statusText).strip().encode("ascii", "ignore") 
		if(svm.classifyStatement(statusText) == 1):
			#Get the keywords and numbers from the text
			keywords = wat.getKeywordsStatement(statusText, len(statusText)/2)
			numbers = wat.getNumbersStatement(statusText)
			dates = wat.getDatesStatement(statusText)
			addKeys = ''
			addDates = ''
			addNums = ''
			for words in keywords:
				addKeys = addKeys +' '+ words
			for date in dates: 
				if(date not in addKeys):
					addDates = addDates + ' ' + date
			for number in numbers:
				if str(number) not in dates and str(number) not in addKeys:	
					addNums = addNums + ' ' + str(number)
			print "Just the keywords: " + addKeys
			isCorrect = False
			conclusive = False
			#Check the knowledge base for the keywords with the numbers
			print addNums + ' ' + addKeys + ' ' + addDates
			if(KnowledgeManagement.readInfo(addNums + ' ' +  addKeys + ' ' + addDates)):
				conclusive = True
				isCorrect = True
			else:
				#Search wolfram alpha for the keywords and number
				print addKeys + addDates
				wolf = KnowledgeBase.baseSearch(addKeys + addDates)
				print "Wolfram return type: " + str(type(wolf))
				if(isinstance(wolf, unicode)):
					wolf = wolf.encode('ascii', 'ignore')
					print "Wolfram return: " + wolf
					wolfKeys = wat.getKeywordsStatement(wolf, len(wolf))
					wolfDates = wat.getDatesStatement(wolf)
					wolfNums = wat.getNumbersStatement(wolf)
					print 'Result keywords: ' + str(wolfKeys)
					print 'Result Dates: ' + str(wolfDates)
					print ' Result Nums: ' + str(wolfNums)
					wolfState = ''
					for word in wolfKeys:
						wolfState = wolfState + ' ' + word
					for date in wolfDates: 
						if(date not in wolfKeys):
							wolfState = wolfState + ' ' + date
					for nums in wolfNums:
						if(nums not in wolfKeys and nums not in wolfDates):
							wolfState = str(nums) + ' ' + wolfState
					print "Wolfram Result: " + wolfState
					if(wat.compareNumStrings(float(addNums),float(wolfNums[0]))):
						conclusive = True
						isCorrect = True
					else:
						conclusive = True
						isCorrect = False
				else:
					#Search Google for the result
					if(WebSearch.webSearch(addNums + ' ' + addKeys + ' ' + addDates)):
						conclusive = True
						isCorrect = True
			statusId = tool.get_status_id(status)
			print statusText
			if(isCorrect and author.id != tool.get_me().id):
				authorScreenName = [tool.get_user_screenName(author)]
				print authorScreenName
				tool.reply_to_tweet(statusId, "This economic statement is truthful.", authorScreenName)
				KnowledgeManagement.addInfo(add)
			elif(not isCorrect and conclusive and author.id != tool.get_me().id):
				authorScreenName = [tool.get_user_screenName(author)]
				print authorScreenName
				tool.reply_to_tweet(statusId, "This economic statement is not truthful.", authorScreenName)
				
	#Twitter rate limit is 15 requests in 15 minutes or 180 requests in 15 minutes. I was breaking it at 15 second intervals.
	time.sleep(60)
	prevStatus = statusText
