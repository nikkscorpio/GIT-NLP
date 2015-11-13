import sys

def postprocess_sentiment(inputfilename):
	with open(inputfilename) as f:
			inputlines = f.read().splitlines()
	document = ""
	for line in inputlines:
		token = line.split()
		if(float(token[0])<1):
			document+="negative\n"
		else:
			document+="positive\n"
	outputfile = open(inputfilename,"w+")
	outputfile.write(document)

def postprocess_email(inputfilename):
	with open(inputfilename) as f:
			inputlines = f.read().splitlines()
	document = ""
	for line in inputlines:
		token = line.split()
		if(float(token[0])<1):
			document+="ham\n"
		else:
			document+="spam\n"
	outputfile = open(inputfilename,"w+")
	outputfile.write(document)

inputfilename = sys.argv[1]
sentiment_or_email = sys.argv[2]
if(str(sentiment_or_email).lower()=="sentiment"):
	postprocess_sentiment(inputfilename)
else:
	postprocess_email(inputfilename)
