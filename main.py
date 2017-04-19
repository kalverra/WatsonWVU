import TwitterOAuthTool
import time
import SVM
import re
import KnowledgeManagement
#import KnowledgeBase
from python_sdk_master.WINSTON.Alchemy_Class import WATSON

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
		statusText = re.sub('\@[^\s]+','', statusText).strip()
		if(svm.classifyStatement(statusText) == 1):
			#Get the keywords and numbers from the text
			keywords = wat.getKeywordsStatement(statusText, len(statusText)/2)
			numbers = wat.getNumbersStatement(statusText)
			add = ''
			for words in keywords:
				add = add +' '+ words
			for number in numbers:
				add = add  + ' ' + number
			isCorrect = False
			if(KnowledgeManagement.readInfo(add)):
				isCorrect = True
			#else:
				#KnowledgeBase.baseSearch(add)	
				#if():
				#
				#else:
			statusId = tool.get_status_id(status)
			print statusText
			if(isCorrect and author.id != tool.get_me().id):
				authorScreenName = [tool.get_user_screenName(author)]
				print authorScreenName
				tool.reply_to_tweet(statusId, "This economic statement is truthful.", authorScreenName)
			elif(not isCorrect and author.id != tool.get_me().id):
				authorScreenName = [tool.get_user_screenName(author)]
				print authorScreenName
				tool.reply_to_tweet(statusId, "This economic statement is not truthful.", authorScreenName)
	#Twitter rate limit is 15 requests in 15 minutes or 180 requests in 15 minutes. I was breaking it at 15 second intervals.
	time.sleep(60)
	prevStatus = statusText
"""
		
    authorList = tool.get_status_author(statuses)
    userRetweetList = tool.get_highest_retweet_status(20)
    for status in userRetweetList['statuses']:
	print userRetweetList['retweets']
    '''
    for status in statuses:
	print tool.get_readable_date(tool.get_status_datetime(status)) + "\n"
    tool.get_readable_date(tool.get_status_date(status)) + " " + 
    for auth in authorList:
	print "Screen Name: " + tool.get_user_screenName(auth)
	print "\nName: " + tool.get_user_name(auth) + " \n" 
    for text in statusText:
	print text + "\n"
    '''
    #Sprint "Enter a new status to post!"
    #newStatus = raw_input("Status: ")
    #tool.post_status(newStatus)
"""
    
