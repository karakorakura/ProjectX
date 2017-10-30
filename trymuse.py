from datamuse import datamuse

api = datamuse.Datamuse()
pencil_syn=api.words(ml="pencil")
#print(pencil_syn)
#for x in pencil_syn:
#	print(x[u'word']+" ")

file=open("test_data.txt","r")
writefile=open("tag.txt","w")

for line in file:
	line = line.strip()
	tagword=line.split()
	tag_syn=api.words(ml=tagword[0])
	for x in tag_syn:
		writefile.write(x[u'word'].encode('ascii','ignore')+"__label__"+tagword[1]+"\n")

writefile.close()
file.close()
