import json
from os.path import join, dirname
from watson_developer_cloud import AlchemyLanguageV1

#Overview on Alchemy found at: https://www.ibm.com/watson/developercloud/doc/alchemylanguage/
#API Refrerence can be found at: https://www.ibm.com/watson/developercloud/alchemy-language/api/v1/

alchemy_language = AlchemyLanguageV1(api_key='9d64e0467f09d220d4fc29cc503bf0f40ec9b73f')

#// Targetted sentiment on a text statement \\
print(json.dumps(
	alchemy_language.targeted_sentiment(text='I love cats! Dogs are smelly.',
                                        targets=['cats', 'dogs'],
                                        language='english'), indent=2))

url = "https://www.washingtonpost.com/powerpost/gop-health-care-plan-hangs-in-balance-as-house-leaders-push-for-thursday-floor-vote/2017/03/23/6e8bf05a-0fbd-11e7-9d5a-a83e627dc120_story.html?hpid=hp_hp-top-table-main_obamacare-805a%3Ahomepage%2Fstory&utm_term=.533458f0ccb2"

statement1 = "The unemployment rate is 10%"
statement2 = "10% is the unemployment rate"

#// One can run multiple anaylsis on a statment using combined operations \\

#combined_operations = ['title, 'author', 'keywords', 'entities', 'emotion']
#print(json.dumps(alchemy_language.combined(url=url, extract=combined_operations),indent=2))

#// Using the Keyword module with the emotional analysis turn on. 
#Gives the top 6 keywords with corresponding ratings in:
#anger, joy, fear, sadness, disgust \\

j = json.dumps(alchemy_language.keywords(max_items=6, text=statement1, language='english'), indent=2)
print(j)

j = json.dumps(alchemy_language.keywords(max_items=6, text=statement2, language='english'), indent=2)
print(j)

#// Using the Keyword module with the sentiment analysis turn on. 
#Gives the top 6 keywords with neutral, negative, and positive types,
#and corresponding scores \\

#j = json.dumps(alchemy_language.keywords(max_items=6, url=url, sentiment = 1), indent=2)



