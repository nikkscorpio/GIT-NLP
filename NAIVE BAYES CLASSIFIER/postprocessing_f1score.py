import sys

 ## Lists with lines corresponding to the classes in the coresponding files
classified_class1 = []
classified_class2 = []

original_class1 = []
original_class2 = []

score = {}


def f1score(classified_class,original_class,class_name):
	count_correctly_classified = 0
	for line in classified_class:
		if line in original_class:
			count_correctly_classified+=1
	recall = count_correctly_classified/len(original_class)
	precision = count_correctly_classified/len(classified_class)
	f1scorestat= (2*precision*recall)/ (precision+recall)
	print(str(class_name)+" count_correctly_classified"+str(count_correctly_classified)+" original_class"+str(len(original_class))+" classified_class"+str(len(classified_class)))

	score[class_name]= dict()
	score[class_name]["recall"] = recall
	score[class_name]["precision"] = precision
	score[class_name]["f1score"] = f1scorestat
	



def create_classes():
	global classified_class1,classified_class2, original_class1,original_class2,class_name1,class_name2
	with open(classified_filename) as f:
			classified_lines = f.read().splitlines()
	with open(original_filename) as f:
			original_lines = f.read().splitlines()

	for i in range(0,len(classified_lines)):
		if classified_lines[i] == class_name1:
			classified_class1.append(i)
		else:
			classified_class2.append(i)

	for i in range(0,len(original_lines)):
		if original_lines[i].split(" ",1)[0] == class_name1:
			original_class1.append(i)
		else:
			original_class2.append(i)
	f1score(classified_class1,original_class1,class_name1)
	f1score(classified_class2,original_class2,class_name2)


classified_filename = sys.argv[1]
original_filename = sys.argv[2]
class_name1 = sys.argv[3]
class_name2 = sys.argv[4]

create_classes()
print(score)
	





