import sys

def add_class(inputfilename):
	with open(inputfilename) as f:
			inputlines = f.read().splitlines()
	document = ""
	for line in inputlines:
		token = str(line).split()
		if(token[0]=="")
		document+="1 "+str(line).strip()+"\n"
	outputfile = open(inputfilename,"w+")
	outputfile.write(document)


inputfilename = sys.argv[1]
add_class(inputfilename)