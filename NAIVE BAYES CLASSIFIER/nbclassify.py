import sys
import operator,math
classes = {}
class_names = []
total_training_documents = 0

def associate_sentiment(label):
		if(label >=7):
			return "positive"
		if(label <= 4 ):
			return "negative"
		else:
			return "NA"

def read_model_file(model_file):
	global classes,class_names,total_training_documents
	total_training_documents = model_file[0].split(":")[1]
	class_names = eval(model_file[1].split(":")[1])
	classes = eval(model_file[2])

def classify_documents(test_file):
	global classes,class_names,total_training_documents
	counter = 1
	
	for document in test_file:
		document_prob = {}
		token = document.split()
		
		for j in class_names:
			document_prob_class = math.log((float(classes[j]["probabilty"])))
			#print("document pro "+str(j)+"  "+str(document_prob_class))
			for i in range(1,len(token)):
				if ':' in token[i]: 
					feature_name = token[i].split(":")[0]
					feature_value = int(token[i].split(":")[1])
					if str((feature_name)+'_probabilty') in classes[j]:
						#print("feature name "+str(feature_name)+str((classes[j][str(feature_name)+'_probabilty'])))
						feature_prob = 0
						for f in range(0,feature_value):
							feature_prob += math.log(float(classes[j][str(feature_name)+'_probabilty']))
						document_prob_class += feature_prob
			document_prob[j] = document_prob_class
		#print(document_prob)
		maxvalue = max(document_prob, key=lambda k: document_prob[k])
		print(maxvalue)

		## Comment it out for actual execution
		
		outputfile.write(str(maxvalue)+"\n")

		# if maxvalue == associate_sentiment(int(token[0])):
		# 	print("correct")
		# else:
		# 	print("innnnn correct"+str(counter))
		# 	counter+=1
		#print(str(max(document_prob.values(),  key=lambda k: document_prob[k])))

	


test_file_name = sys.argv[2]

outputfile = open("classified_output.txt","w+")
model_file_name = sys.argv[1]
with open(model_file_name) as f:
		model_file = f.read().splitlines()
read_model_file(model_file)
with open(test_file_name) as f:
		test_file = f.read().splitlines()
classify_documents(test_file)