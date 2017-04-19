import wolframalpha, re
#Wolframalpha library originates from this link: https://github.com/jaraco/wolframalpha
#To install, type 'pip install wolframalpha' in command prompt

#Retrieves answers from the WolframAlpha knowledge base
def baseSearch(searchTerms):
    client = wolframalpha.Client('RVL9QV-96EGP47QLU')

    res = client.query(searchTerms)
    
    #Prints the entire 'answer' string returned by WolframAlpha 
    #print(next(res.results).text)

    #Parses the first statement in the list, dividing it up into the answer and the individual background tokens in parenthesis
    ansFormat = r"\(?[^()]+\)?"

    #re.search only returns the first match found, starting from the beginning of the string - re.match is needed for finding multiple matches
    processed = re.search(ansFormat, next(res.results).text)

    #Returns the result parsed from the regular expression
    #print(processed.group(0))
    return(str(processed.group(0)))

print(baseSearch("trump taxes economy"))
