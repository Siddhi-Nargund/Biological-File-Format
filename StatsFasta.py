#/usr/bin/python3
#!/usr/bin/env python3

import argparse
import re
import os
import gzip
import shutil

parser = argparse.ArgumentParser(description='Enter File name with location')
parser.add_argument('--file', type=str,dest="filepaths")
parser.add_argument('--output',type=str,dest="outputFileName")
args = parser.parse_args()

#splitting name and extension of the file
name, extension= os.path.splitext(args.filepaths)

fileToOpen = args.filepaths
outputFileName = args.outputFileName

#If extension isn't in fasta file format or in gunzipped, it would exit giving an error
if extension not in ['.gz', '.fa']:
    print("Invalid file format")
    exit()

#if file is in .gz format, it would open it in fasta file format
if extension=='.gz':
    with gzip.open(fileToOpen, 'rb') as faFileGz:
        with open(name, 'wb') as faFile:
            shutil.copyfileobj(faFileGz, faFile )
    fileToOpen=name

with open(fileToOpen, 'r') as faFile:
        fastaFile = faFile.read()

#regex to extract "Read_ID"    
readIDString= "read_id=[0-9]*"
#searching gor regex in the file
temp = re.findall(readIDString,fastaFile)
readIDDict = {}
readIDArray = []
for i in range(0,len(temp)):
    readIDDict['Read_ID'] = temp[i]
    readIDArray.append(readIDDict)
    readIDDict = {}
#print(readIDArray)

print("Number of sequences are: "+str(len(readIDArray)))

#regex to extract length of reads
lenString= "length=[0-9]*"

#searching gor regex in the file
flag= re.findall(lenString,fastaFile)
lenDict = {}
lenArray = []
for i in range(0,len(flag)):
    lenDict = flag[i]
    lenArray.append(lenDict)
    lenDict = {}
# print(lenArray)

#Accessing number after '=' in 'lenght=nn'
lenArray = [i.split('=')[1] for i in lenArray] 
#print(lenArray)

for i in range(0, len(lenArray)): 
    lenArray[i] = int(lenArray[i]) 
# print(len(lenArray))

#counting lengths of all the reads
total= sum(lenArray)
print("Number of residues are :", total)

#writing the output in output file
with open(outputFileName, 'w') as f:
    f.write("Number of sequences are: "+str(len(readIDArray)))
    f.write("\nNumber of residues are :" +str(total))
    