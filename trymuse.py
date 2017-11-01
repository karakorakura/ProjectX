from datamuse import datamuse

api = datamuse.Datamuse()
pencil_syn=api.words(ml="pencil")
#print(pencil_syn)
#for x in pencil_syn:
#	print(x[u'word']+" ")

file=open("test_data.txt","r")
# fileWords=open("wordsDataSet.txt","w")
fileSentences = open("sentencesDataSet2.txt","w")

for line in file:
	line = line.strip()
	tagword=line.rsplit(' ',1)
	word1 = tagword[0].strip()
	tag_syn=api.words(ml=word1)
	sentence1=""
	for x in tag_syn:
		sentence1 += x[u'word'].encode('ascii','ignore') + " ";
		# fileWords.write("__label__"+tagword[1]+" , "+x[u'word'].encode('ascii','ignore')+"\n")
	# fileWords.write("__label__"+tagword[1]+" , "+word1+"\n")
	fileSentences.write(""+tagword[1]+", "+word1+" "+sentence1+"\n")
	# 	writefile.write("__label__"+tagword[1]+" , "+x[u'word'].encode('ascii','ignore')+"\n")


fileSentences.close()
file.close()
