import sys
import random
import os
import shutil

def split_folder(input_foldername,split_percentage,output_folder1,output_folder2):
	"""
	SPLITS THE FOLDER INTO TWO FOLDERS - TRAINING AND DEVELOPMENT
	COPIES FILES FROM ORIGINAL FOLDER INTO TRAINING AND DEVELOPMENT
	python3 preprocessor_splitfile.py data/train 80 data/training data/development
	"""
		 	
	rand_filenames = []
	remaining_filenames =[]

	files = os.listdir(input_foldername)
	csv_files = [fi for fi in files if fi.endswith(".csv")]
	number_of_files = len(csv_files) 
	rand_files = random.sample(csv_files, round(number_of_files*int(split_percentage)/100))	
	remaining_files = [obj for obj in csv_files if obj not in rand_files]

	if not os.path.exists(input_foldername+"/"+output_folder1):
		os.makedirs(input_foldername+"/"+output_folder1)
	if not os.path.exists(input_foldername+"/"+output_folder2):
		os.makedirs(input_foldername+"/"+output_folder2)

	for files in rand_files:
		print(output_folder1+"/"+files)
		shutil.copyfile(input_foldername+"/"+files, input_foldername+"/"+output_folder1+"/"+files)

	for files in remaining_files:
		shutil.copyfile(input_foldername+"/"+files, input_foldername+"/"+output_folder2+"/"+files)
	

input_foldername = sys.argv[1]
split_percentage = sys.argv[2]
output_folder1= sys.argv[3]
output_folder2 = sys.argv[4]
split_folder(input_foldername,split_percentage,output_folder1,output_folder2)