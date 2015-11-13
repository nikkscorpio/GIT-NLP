import sys

total_training_documents = 0
class_names = []
classes = {}
vocabulary = []  # Set of unique words occuring in training set
#total_training_documents ==> Total Number of training documents
#classes['POSITIVE']
#classes['POSITIVE']['Total Documents'] =  20 ==> Number of Documents of POSITIVE sentiment
#classes['POSITIVE'][0] = 20 ==> NUmber of times 0 has occured in POSITIVE Documents
#classes['POSITIVE']['TOTAL Words'] = 100 ==> Number of words in POSTIVE Documents
#classes['POSITIVE']["probabilty"] ==> Final Probabilty of class POSITIVe  prob(Positive)
#classes['POSITIVE']['1_probabilty'] ==> prob(1|Positive)



def create_class_dict(training_input):
	
	global classes,vocabulary,class_names
	for document in training_input:
		#Get each word in a document
		token = document.split()
		#Token[0] will have the class name
		current_class_name = token[0]
		# try:
		# 	sentiment_value = int(current_class_name)
		# 	current_class_name = associate_sentiment(sentiment_value)
		# except ValueError:
		# 	continue
		
		if current_class_name in class_names:
			# Calculate number of each Class documents
			classes[current_class_name]['Total Documents']  += 1
			
		else:
			classes[current_class_name] = dict()
			class_names.append(current_class_name)
			# Calculate number of each Class documents
			classes[current_class_name]['Total Documents'] = 1
			#classes['Total '+current_class_name+' Documents'] = 1

		#Retrieve each feature in the current line
		for i in range(1,len(token)):
			feature_name = token[i].split(":")[0]
			feature_value = int(token[i].split(":")[1])
			# Calculate Number of times feature_name is occuring in current class
			if(feature_name in classes[current_class_name]):
				classes[current_class_name][feature_name]+=feature_value
			else:
				vocabulary.append(feature_name)
				classes[current_class_name][feature_name]=feature_value
			# calculate Total words occuring in the current Class
			if 'Total Words' in classes[current_class_name]:
				classes[current_class_name]['Total Words']+=feature_value
			else:
				classes[current_class_name]['Total Words']=feature_value

# # Function to associate Positive to sentiments >=7 and 
# # negative to sentiments <=4
# def associate_sentiment(label):
# 	if(label >=7):
# 		return "positive"
# 	if(label <= 4 ):
# 		return "negative"
# 	else:
# 		return "NA"
def find_feature_probability(training_file,model_file):
	global total_training_documents,classes,class_names
	with open(training_file) as f:
		training_input = f.read().splitlines()
	total_training_documents = len(training_input)
	print(total_training_documents)
	create_class_dict(training_input)

	#Probabilty of classes
	for i in class_names:
		classes[i]["probabilty"]= str(float(classes[i]['Total Documents'])/float(total_training_documents))
		#Probabilty of each feature
		for j in vocabulary:
			if j in classes[i]:
				classes[i][j+"_probabilty"] = str((float(classes[i][j])+1)/(float((classes[i]['Total Words'])+len(vocabulary))))
			else:
				classes[i][j+"_probabilty"] = str(1/(float((classes[i]['Total Words'])+len(vocabulary))))
	outputfile = open(model_file, 'w+')
	outputfile.write("total_training_documents :" +str(total_training_documents)+"\n")
	outputfile.write("class_names :" +str(class_names)+"\n")
	outputfile.write(str(classes)+"\n")

	
 	






filename = sys.argv[1]
model_file = sys.argv[2]
find_feature_probability(filename,model_file)
