import sys
import os
vocablines = []

def check_training_testing(inputfilename,outputfilename):
	""" If there are folders within the input folder, then the data is classified as training data with labels
	Else if there are only text files, then the data is classified as testing data with no labels
	"""
	assign_identifiers()
	# retrieve the folders and files within the input directory
	
	for directory in inputfilename:
		folders = os.listdir(directory)   #Folders --> HAM SPAM
		training_set = False
		for f in folders:
			if os.path.isdir(os.path.join(directory,f)):
				training_set = True
		if training_set ==  True:
			classify_training_data(directory,folders,outputfile)
		else:
			classify_testing_data(directory,folders,outputfile)


def classify_training_data(inputfilename,folders,outputfile):
	for f in folders:
		#Only for directories(classes) within the folder we perform combining the files
		folder_path = os.path.join(inputfilename,f)
		class_name = os.path.basename(folder_path)
		folder_files = []
		if os.path.isdir(folder_path):
			folder_files = os.listdir(folder_path)

			combine_files(folder_files,folder_path,class_name,outputfile)

def classify_testing_data(inputfilename,folders,outputfile):

	folder_path = os.path.abspath(inputfilename)
	class_name = ""

	combine_files(folders,folder_path,class_name,outputfile)

def combine_files(folder_files,folder_path,class_name,outputfile):
	global vocab_filename,vocablines
	
	for filename in folder_files:
		if not filename.startswith('.'):
		#print(filename)
			
			wordcount = dict()
			wordcountstr = ""
			print(os.path.join(folder_path,filename))
			with open(os.path.join(folder_path,filename),encoding="latin1") as f:
				filelines = f.read().splitlines()
			#print(filelines)
			for line in filelines:
				words = line.split()
				#print("word"+str(words))
				for word in words:
					if word in vocablines:
						index = vocablines.index(word)+1
						if index in wordcount:
							wordcount[index]+=1
						else:
							wordcount[index] = 1
			#print(wordcount)
			wordcountstr = str(wordcount).replace(": ",":")
			wordcountstr = class_name+" "+wordcountstr.replace(",","").replace('{',"").replace('}',"")
			#print(wordcountstr)
			outputfile.write(wordcountstr+"\n")
			



		


def assign_identifiers():
	global vocab_filename,vocablines
	with open(vocab_filename,encoding="latin1") as f:
		vocablines = f.read().splitlines()






outputfilename = sys.argv[1]
vocab_filename = sys.argv[2]
inputfoldername = []
# If there are more than three system Varible Arguments then it is Training Data
outputfile = open(outputfilename,"w+")
if len(sys.argv) >3:
	for i in range(3,len(sys.argv)):
		inputfoldername.append(sys.argv[i])
else:
	inputfoldername.append(sys.argv[3])


check_training_testing(inputfoldername,outputfilename)