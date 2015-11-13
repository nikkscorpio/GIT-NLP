from collections import namedtuple
import csv
import sys
import os
import hw3_corpus_tool



DialogUtterance = namedtuple(
	"DialogUtterance", ("act_tag", "speaker", "pos", "text"))

PosTag = namedtuple("PosTag", ("token", "pos"))				
			

	
	# print(split)
	# dg = DialogUtterance._make(split[0].split("act_tag=")[0],split[0].split("speaker="),split[0].split("pos="),split[0].split("text="))
	# print(str(dg))

inputfilename = sys.argv[1]
outputfilename = inputfilename+".out"


mainstr = ""
count = 0

if(".csv" in inputfilename):
	speakerlist = []
	#files = open(inputfilename,"r")
	dict_items = hw3_corpus_tool.get_utterances_from_filename(inputfilename)
	
	for items in dict_items:
		POSTAGS = ""
		TOKENS = ""

		dial = DialogUtterance(getattr(items,"act_tag"),getattr(items,"speaker"),getattr(items,"pos"),getattr(items,"text"))
		#Check for unlabelled data! Label with "sd" if data is unlabelled
		if dial.act_tag:
			mainstr+=dial.act_tag
		else:
			mainstr+="sd"
		if count==0:
			mainstr+="\tNEWSEQ"
		if len(speakerlist)>1 and dial.speaker != "" and dial.speaker!=speakerlist[len(speakerlist)-1]:
			mainstr+="\t+SPEAKER"
		speakerlist.append(dial.speaker)
		if(dial.pos and dial.pos != 'none'):
			pos = eval(str(dial.pos))
			for p in pos:
				insidetag = PosTag(p.token,p.pos)
				POSTAGS+="\tPOS_"+insidetag.pos
				if insidetag.token == ':':
					TOKENS+="\t[colon]"
				if insidetag.token == '\\':
					TOKENS+="\tBACKSLASH"
				else:
					TOKENS+="\tTOKEN_"+insidetag.token
				
		mainstr+=POSTAGS+TOKENS+"\n"
		count = count+1

outputfile = open(outputfilename,"w+")		
outputfile.write(mainstr+"\n") 

	   







		
			