import random
import numpy
file=open("wordsDataSet.txt","r").readlines()
# print file
random.shuffle(file);
testfile=open("TestData1.txt","w")
trainfile=open("TrainData1.txt","w")

# CNT=1900
CNT = len(file)


lcnt=0;
for line in file:
    if lcnt < 0.7*CNT:
        line = line
        trainfile.write(line)
    else :
        l1 = line.strip()
        l1 = line.split(' , ')
        l1 = l1[1]
        # l1=l1+"\n"
        testfile.write(l1)
    lcnt+=1

testfile.close()
trainfile.close()
# file.close()
