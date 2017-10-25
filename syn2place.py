def getDict():
	syn2place = {}
	with open('map.txt','r') as f:
		for line in f:
			line = line.strip()
			syn,place = line.split(' ',1)
			syn2place[syn] = place
	return syn2place

if __name__ == "__main__":
	main()