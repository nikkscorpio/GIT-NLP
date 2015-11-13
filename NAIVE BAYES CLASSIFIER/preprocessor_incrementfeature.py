import sys

def increment_sentiment_feature(inputfilename):
	"""
	Adds 1 to the feature_name token so that the feature_names are read correctly by SVM
	The original file will contain feature_names starting from 0
	New file will have feature_names starting from 1
	This program is used only for Sentiment data.
	"""
	document = ""
	with open(inputfilename) as f:
		inputlines = f.read().splitlines()
	for line in inputlines:
		tokens = line.split()
		for token in tokens:
			if ":" in token:
				feature_name = int(token.split(":")[0])+1
				feature_value = token.split(":")[1]
				document+=str(feature_name)+":"+str(feature_value)+" "
			else:
				document+=str(token)+" "
		document+="\n"

	inputfile = open(inputfilename,"w+")
	inputfile.write(document)



inputfilename = sys.argv[1]
increment_sentiment_feature(inputfilename)