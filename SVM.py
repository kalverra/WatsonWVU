import pandas as pd
import re
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import LinearSVC
from nltk.corpus import stopwords

class SVM:
	
	vectorizer = None
	svm = None

	#The SVM constructor takes in the csv file name containing the preproccessed text statments
	#and the max num_features you would like for the SVM to look for.
	#A higher max_feature number seems to give us less reliable results. 
	def __init__(self, file_name, num_features):
		self.vectorizer = CountVectorizer(analyzer = "word",   \
                             tokenizer = None,    \
                             preprocessor = None, \
                             stop_words = None,   \
                             max_features = num_features)
		
		self.svm = LinearSVC()		

		train_csv = pd.read_csv(file_name)

		train_statements = []
		econ_value = []
		
		for statement in train_csv["Statement"]:
			train_statements.append(statement.strip())
		
		for econ in train_csv["Economics (T/F)"]:
			if econ.strip() == "T":
				econ_value.append(1)
			else:
				econ_value.append(0)

		train_features = self.vectorizer.fit_transform(train_statements)

		self.svm.fit(train_features, econ_value)

	#Takes in a string statement, and returns a 1 if it is considered economic, and a 0 if not
	def classifyStatement(self, statement):

		stops = set(stopwords.words("english"))		
		
		statement = re.sub("[^a-zA-Z0-9\s]", "", statement)
		statement = re.sub("(\d+(\d)*)", "NUM", statement)
		words = statement.split(" ")
		string = ""
		for w in words:
			if not w in stops:
				string += w + " " 
		
		test_feature = self.vectorizer.transform([statement])

		return self.svm.predict(test_feature)[0]

	def printVocab(self):
		vocab = self.vectorizer.get_feature_names()
		print(vocab)


#Create an instantiation of the classifier like so:
clf = SVM("cleanedTrainingStatements.csv", 1000)
#call to the functions like so: 
clf.printVocab()

#Testing
test = pd.read_csv("testingStatements.csv")

#for statement in test["Statement"]:
#	print(clf.classifyStatement(statement))



