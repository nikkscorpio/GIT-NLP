import sys
import collections

def arrange_increasing_features(inputfilename):
	"""This program is used to sort the feature names within the 
	training/testing file in increasing order."""
	
	with open(inputfilename) as f:
			inputlines = f.read().splitlines()
	document = ""
	for line in inputlines:

		token = line.split(" ",1)
		document+=str(token[0])
		new_dict = {}
		line_dict = collections.OrderedDict()
		line_dict = eval("{"+str(token[1]).replace(" ",",")+"}")
		line_dict = collections.OrderedDict(sorted(line_dict.items()))
		line_dict_str = str(line_dict).replace("), ("," ").replace(", ",":").replace("(","").replace(")","").replace("]","").replace("[","").replace("OrderedDict","")
		document+=" "+line_dict_str+"\n"
	outputfile = open(inputfilename,"w+")
	outputfile.write(document)

inputfilename = sys.argv[1]
arrange_increasing_features(inputfilename)