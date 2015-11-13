import sys


def convert_data_svm(inputfilename,outputfilename):
	with open(inputfilename) as f:
			filelines = f.read().splitlines()
	document=""
	for line in filelines:
		token = line.split(" ",1)
		if(str(token[0]).lower()=="spam" or str(token[0]).lower()=="positive"):
			document+="1"+" "+str(token[1])+"\n"
		elif(str(token[0]).lower()=="ham" or str(token[0]).lower()=="negative"):
			document+="-1"+" "+str(token[1])+"\n"
		else:
			document+=str(line)
	outputfile = open(outputfilename,"w+")
	outputfile.write(document)

def convert_data_megam(inputfilename,outputfilename):
	with open(inputfilename) as f:
			filelines = f.read().splitlines()
	document=""
	for line in filelines:
		token = line.split(" ",1)
		if(str(token[0]).lower()=="spam" or str(token[0]).lower()=="positive"):
			document+="1"+" "+str(token[1]).replace(":"," ")+"\n"
		elif(str(token[0]).lower()=="ham" or str(token[0]).lower()=="negative"):
			document+="0"+" "+str(token[1]).replace(":"," ")+"\n"
		else:
			document+=str(line).replace(":"," ")+"\n"
	outputfile = open(outputfilename,"w+")
	outputfile.write(document)


inputfilename = sys.argv[1]
outputfilename = sys.argv[2]
megaM_svm	 = sys.argv[3]
if(str(megaM_svm).lower()=="svm"):
	convert_data_svm(inputfilename,outputfilename)
elif(str(megaM_svm).lower()=="megam"):
	convert_data_megam(inputfilename,outputfilename)

