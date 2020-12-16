#!/usr/bin/python3
#!/usr/bin/env python3
import re
import argparse

parser = argparse.ArgumentParser(description='Enter File location and Class Code')
parser.add_argument('--file', type=str,dest="filepaths")
parser.add_argument('--class_code',type=str,dest="searchSymbol")
parser.add_argument('--output',type=str,dest="outputFileName")
args = parser.parse_args()

fileToOpen = args.filepaths
symbolToSearch = args.searchSymbol
outputFileName = args.outputFileName

f= open(fileToOpen, "r")
lines = f.readlines()
regexString = '[=,c,k,m,n,j,e,o,s,x,i,y,p,r,u]\s*[q1]'
regexList = []
counter = 1
for i in lines:
    # print(i)
    counter += 1
    # print(counter)
    temp = re.findall(regexString,i)
    # temp = temp[0].split("\\")
    print(temp[0])
    regexList.append(temp[0])

symbolList = []
tempCount = 1
for index in range(len(regexList)):
    tempCount += 1
    print(regexList[index][0].strip())
    symbolList.append(regexList[index][0].strip())
resultList = []
# print(symbolList)

for index in range(len(symbolList)):
    if symbolList[index] is symbolToSearch:
        # print("Currently at")
        print(index+1)
    
        resultList.append(index+1)
# print(resultList)
contentToWrite = []
counts = 1 
for i in range(len(lines)):
    counts += 1
    # print(counts)
    if counts in resultList:
        print(lines[i+1])
        contentToWrite.append(lines[i+1])

print("Symbol Counter: "+str(tempCount))
print("File Counter: "+str(counter))

print("Final!!")
print(contentToWrite)
newFile = open(outputFileName, "w")
for current in contentToWrite:
    newFile.write(current+'\n')

newFile.close()
f.close()