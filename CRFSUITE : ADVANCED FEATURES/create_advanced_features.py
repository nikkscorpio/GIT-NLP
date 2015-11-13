from collections import namedtuple
import csv
import sys
import os
import hw3_corpus_tool



DialogUtterance = namedtuple(
	"DialogUtterance", ("act_tag", "speaker", "pos", "text"))

PosTag = namedtuple("PosTag", ("token", "pos"))				
			


inputfilename = sys.argv[1]
outputfilename = inputfilename+".adv.out"


mainstr = ""
count = 0

if(inputfilename.endswith(".csv")):
	speakerlist = []
	#files = open(inputfilename,"r")
	dict_items = hw3_corpus_tool.get_utterances_from_filename(inputfilename)
	
	for items in dict_items:
		POSTAGS = ""
		TOKENS = ""
		BIPOSTAGS =""
		BITOKENS = ""
		TRIPOSTAGS = ""
		TRITOKENS = ""

		dial = DialogUtterance(getattr(items,"act_tag"),getattr(items,"speaker"),getattr(items,"pos"),getattr(items,"text"))

		dialtext = dial.text
		dialtext = dialtext[:-1]
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
			trigrams = []
			j=0
			while(j<len(pos)):
				insidetoken = []	
				insidepos= []		
				insidetag1 = PosTag(pos[j].token,pos[j].pos)
				insidetokenstr = '[colon]' if insidetag1.token== ':' else 'BACKSLASH' if insidetag1.token=='\\' else insidetag1.token
				insidetoken.append(insidetokenstr)
				insidepos.append(insidetag1.pos)
				
				j+=1
				if(j<len(pos)):
					insidetag2 = PosTag(pos[j].token,pos[j].pos)
					insidetokenstr = '[colon]' if insidetag2.token== ':' else 'BACKSLASH' if insidetag2.token=='\\' else insidetag2.token

					insidetoken.append(insidetokenstr)
					insidepos.append(insidetag2.pos)

					j+=1
				if(j<len(pos)):
					insidetag3 = PosTag(pos[j].token,pos[j].pos)
					insidetokenstr = '[colon]' if insidetag3.token== ':' else 'BACKSLASH' if insidetag3.token=='\\' else insidetag3.token

					insidetoken.append(insidetokenstr)
					insidepos.append(insidetag3.pos)
					j+=1

				
	
				TRIPOSTAGS+="\tTRI_POS"
				for it in range(0,len(insidepos)):
					TRIPOSTAGS+="_"+insidepos[it]
				TRITOKENS+="\tTRI_TOKEN"
				for it in range(0,len(insidetoken)):

					TRITOKENS+="_"+insidetoken[it]
			j=0
			while(j<len(pos)):
				insidetoken =[]
				insidepos = []
				insidetag1 = PosTag(pos[j].token,pos[j].pos)
				insidetokenstr = '[colon]' if insidetag1.token== ':' else 'BACKSLASH' if insidetag1.token=='\\' else insidetag1.token
				insidetoken.append(insidetokenstr)
				insidepos.append(insidetag1.pos)

				j+=1
				if(j<len(pos)):
					insidetag2 = PosTag(pos[j].token,pos[j].pos)
					insidetokenstr = '[colon]' if insidetag2.token== ':' else 'BACKSLASH' if insidetag2.token=='\\' else insidetag2.token
					insidetoken.append(insidetokenstr)
					insidepos.append(insidetag2.pos)
					j+=1

				BIPOSTAGS+="\tBI_POS"
				for it in range(0,len(insidepos)):
					BIPOSTAGS+="_"+insidepos[it]
				BITOKENS+="\tBI_TOKEN"
				for it in range(0,len(insidetoken)):

					BITOKENS+="_"+insidetoken[it]

		
		mainstr+=POSTAGS+TOKENS+BIPOSTAGS+BITOKENS+TRIPOSTAGS+TRITOKENS+dialtext+"\n"
		count = count+1

outputfile = open(outputfilename,"w+")		
outputfile.write(mainstr+"\n") 

	   







		
			