import TwitterOAuthTool

if '__main__' == __name__:
    tool = TwitterOAuthTool.TwittTool()
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
    #print 'Input the status that you would like to update!'
    tool.prepare_api()
    prevStatus = ""
    while(True):
	#Reading in most recent status
	statuses = tool.read_timeline(1)
	author = tool.get_status_author(statuses[0])
	print author
	statusText = tool.get_status_text(statuses)
	if(statusText[0] != prevStatus):
		#Start analyzing the new status
		statusId = tool.get_status_id(statuses[0])
		tool.reply_to_tweet(statusId, "My reply to you goes here I guess.")
		time.sleep(15)
	prevStatus = statusText[0]
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
    
