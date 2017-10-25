import nltk
from nltk.corpus import wordnet as wn

nltk.data.path.append('./nltk_data')

result = open('output.txt','w')

with open('places.txt') as places:
	for place in places:
		place = place.strip()
		result.write(place + '\n')
		syns = wn.synsets(place)
		for syn in syns:
			result.write('\t %s\n' % syn)
		#result.write('\n')

result.close()
print("Done")