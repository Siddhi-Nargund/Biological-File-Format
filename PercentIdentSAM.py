#!/usr/bin/python3
#!/usr/bin/env python3
import argparse
import re
import csv

parser = argparse.ArgumentParser(description='Enter File location')
parser.add_argument('-i', type=str,dest="filepaths")
parser.add_argument('-o',type=str,dest="outputFileName")
args = parser.parse_args()

fileToOpen = args.filepaths
outputFileName = args.outputFileName

#f= open(fileToOpen, "rb")
#f= open("Lactobacillus_crispatus_Aligned.sam", "rb")
#samFile= f.readlines()

with open(fileToOpen, 'rb') as f:
    lines = [x.decode('utf8').strip() for x in f.readlines()]

md_string= "MD:Z:[0-9,A-Z,^]*"
matchedArray = []
unmatchedArray = []
percentIdentityArray = []
nameArray = []
positionArray = []
for line in lines:
    split_str=line.split("\t")
    #print(split_str)
    if len(split_str) < 13:
        continue
    else:
        name= split_str[0]
        nameArray.append(name)
        
        #print(name, location)
        split_str2=split_str[11:]
        for st in split_str2:
            temp = re.findall(md_string,st)
            #print(temp)
            if len(temp) > 0:
                matched = 0
                unmatched = 0
                # print(name, location, temp)
                temp = temp[0].split('MD:Z:')[1]
                # print(temp)
                tempData = re.findall('[0-9]*',temp)
                tempData[:] = [x for x in tempData if x]
                # print(tempData)
                for a in tempData:
                    matched += int(a)
                matchedArray.append(matched)
                tempUnmatchedData = re.findall("['A','T','G','C']", temp)
                # print(tempUnmatchedData)
                unmatched += len(tempUnmatchedData)
                unmatchedArray.append(unmatched)
                location= split_str[3]
                positionArray.append(location)
# print(unmatchedArray)
# print(matchedArray)

for i in range(len(matchedArray)):
    percentIdentity = 100 * (matchedArray[i] / (matchedArray[i] + unmatchedArray[i]))
    # print(percentIdentity)
    percentIdentityArray.append(percentIdentity)
# print(percentIdentityArray)

resultArray = []   
for i in range(len(matchedArray)):
    t = []
    t.append(nameArray[i])
    t.append(positionArray[i])
    t.append(percentIdentityArray[i])
    resultArray.append(t)
fields = ['Name', 'Position', 'PercentIdentity'] 
with open(outputFileName+'.csv', "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(fields)
    writer.writerows(resultArray)
