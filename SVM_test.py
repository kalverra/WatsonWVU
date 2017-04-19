import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import LinearSVC

vectorizer = CountVectorizer(analyzer = "word",   \
                             tokenizer = None,    \
                             preprocessor = None, \
                             stop_words = None,   \
                             max_features = 100)

train = pd.read_csv("trainingStatements.csv")
test = pd.read_csv("cleandTestStatements.csv")

train_statements = []
econ_value = []
test_statements = []

for statement in train["Statement"]:
	train_statements.append(statement.strip())

for statement in test["Statement"]:
	test_statements.append(statement.strip())

for econ in train["Economics (T/F)"]:
	if econ == "T":
		econ_value.append(1)
	else:
		econ_value.append(0)

train_features = vectorizer.fit_transform(train_statements)

#train_features = np.array(train_features.toarray())
#econ_features = np.array(econ_value)

svm = LinearSVC()
svm.fit(train_features, econ_value)

test_feature = vectorizer.transform(test_statements)
#test_feature = np.array(test_feature.toarray())

#print(svm.predict(test_feature))
print(svm.predict(test_feature)[0])

