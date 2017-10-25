import syn2place,pprint
import nltk
from nltk.corpus import wordnet as wn

nltk.data.path.append('./nltk_data')

d = syn2place.getDict();
out_syns = d.keys()
#pprint.pprint(d)

def getSyn(query):
	in_syns = wn.synsets(query,pos=wn.NOUN)
	out_syns = d.keys()
	max_similarity = -1
	res_syn = None
	for isyn in in_syns:
		loc_sim = -1
		loc_syn = None
		for osyn in out_syns:
			syn = wn.synset(osyn)
			temp = isyn.path_similarity(syn)
			if temp > loc_sim:
				loc_sim = temp
				loc_syn = osyn
		#res_syns.append(loc_syn)
		if loc_sim > max_similarity:
			max_similarity = loc_sim
			res_syn = loc_syn
	return res_syn


fin = open('test_data.txt','r')
fout = open('test_out.txt','w')

for line in fin:
	q = line.strip()
	syn = getSyn(q)
	place = " "
	if syn is not None:
		place = d[syn]
		fout.write(q + " " + place + "\n")

fin.close()
fout.close()

print("Done")



