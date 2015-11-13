import sys

inputfilename = sys.argv[1]

with open(inputfilename) as f:
	correctly_classified = 0
	total_tags = 0
	for line in f:
		if(line.strip()!=""):
			split = line.split()
			if(split[0]==split[1]):
				correctly_classified+=1
			total_tags+=1
	accuracy = float(correctly_classified/total_tags)
	print(accuracy)
