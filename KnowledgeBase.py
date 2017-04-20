import wolframalpha, re
#Wolframalpha library originates from this link: https://github.com/jaraco/wolframalpha
#To install, type 'pip install wolframalpha' in command prompt

#Retrieves answers from the WolframAlpha knowledge base
def baseSearch(searchTerms):
    client = wolframalpha.Client('RVL9QV-96EGP47QLU')

    res = client.query(searchTerms)
    
    try:
        #Queries are broken down into pods, which contain different types of information
        for pod in res.pods:
            #Locates the first pod with 'result' in the tile - this is necessary as pod titles can vary slightly
            if "Result" in pod.title or "result" in pod.title:
                #Parses the first statement in the list, dividing it up into the answer and the individual background tokens in parenthesis
                ansFormat = r"\(?[^()]+\)?"

                #re.search only returns the first match found, starting from the beginning of the string - re.match is used for finding multiple matches
                processed = re.search(ansFormat, pod.text)

                #Returns the result parsed from the regular expression
                return(processed.group(0))
                #return pod.text
    #Attribute errors arise when queries Wolfram Alpha can't understand are entered - move onto a different method
    except AttributeError:
        print("Nonapplicable terms")
        pass

#terms = raw_input("Enter your search terms: ")
#print(baseSearch(terms))
