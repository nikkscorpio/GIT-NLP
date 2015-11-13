import sys
import random


def split_filename(input_filename,split_percentage,output_filename1,output_filename2,email_or_sentiment):
	"""
	split_file function splits the input file(input_filename) into two parts of size split_percentage and 1-split percentage sizes
	and writes the specific lines to the output files
	""" 	 	
	rand_lines = []
	with open(input_filename) as f:
		print(input_filename)
		file_lines = f.read().splitlines()
	number_of_lines = len(file_lines)
	print(number_of_lines)
	# Assigning "positive" or "negative" values to sentiment data 
	if(email_or_sentiment == "sentiment"):
		i=0
		for line in file_lines:
			token = line.split(" ",1)
			#Token[0] will have the class name
			current_class_name = token[0]

			try:
				sentiment_value = int(current_class_name)
				current_class_name = associate_sentiment(sentiment_value)
			except ValueError:
				continue
			file_lines[i] = current_class_name+" "+token[1]
			i=i+1


	




	#Generate a list of random numbers in the range of (0,input_file_length)
	#the list will contain split_percentage number of lines
	rand_lines = random.sample(range(0,number_of_lines), round(number_of_lines*int(split_percentage)/100))
	# Read the random lines from input file and write to the output files
	outputfile1 = open(output_filename1,"w+")
	for i in rand_lines:
		outputfile1.write((file_lines[i])+"\n")
	outputfile2 = open(output_filename2,"w+")
	# Calculate the reamining line numbers from the input file
	remaining_lines = [obj for obj in range(0,number_of_lines) if obj not in rand_lines]
	for j in remaining_lines:
		outputfile2.write(file_lines[j]+"\n")
	outputfile1.close()
	outputfile2.close()



# Function to associate Positive to sentiments >=7 and 
# negative to sentiments <=4
def associate_sentiment(label):
	if(label >=7):
		return "positive"
	if(label <= 4 ):
		return "negative"
	else:
		return ""



input_filename = sys.argv[1]
split_percentage = sys.argv[2]
output_filename1 = sys.argv[3]
output_filename2 = sys.argv[4]
email_or_sentiment = sys.argv[5]   ### email or sentiment for classifying sentiments values into positive or negative
split_filename(input_filename,split_percentage,output_filename1,output_filename2,email_or_sentiment)