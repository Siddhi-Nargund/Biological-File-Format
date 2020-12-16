#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--source_gff', type=str,dest="source")
parser.add_argument('--type', type=str,dest="type")
parser.add_argument('--attribute', type=str,dest="attribute")
parser.add_argument('--value', type=str,dest="value")
args = parser.parse_args()

#filename= '/home/jorvis1/Saccharomyces_cerevisiae_S288C.annotation.gff'

filename=args.source
type=args.type
attribute=args.attribute
value=args.value
#type="gene"
#attribute="ID"
#value="YAR003W"
seq=None
fasta= ""
temp=False

for line in open(filename):
	if line.startswith("#"):
		continue
	elif line.startswith(">"):
		line=line.strip("\n").strip("\r")
		if temp== True:
			temp= False
			break
		if ">" + seq == line:
			temp= True 
	else:
		line=line.strip("\n").strip("\r")
		#ignoring \n and \r
		if temp== True:
			fasta+=str(line)
			continue	
		flag=line.split("\t")
		#splitting by tab
		#print(flag)
		#exit(0)
		if len(flag)<9:
			continue
		#print(line)
		type2=flag[2]
		#seq=flag[0]
		column=flag[8]
		column=column.split(";")
		#splitting column 9 
		#print(column)
		#exit(0)
		if type2 != type:
			continue
		
		for x in column:
			if x== str(attribute)+ "=" + str(value):
				#comparing attribute in column9
				print(flag[3], flag[4], flag[6])
				seq=flag[0]
				start=flag[3]
				stop=flag[4]
				strand=flag[6]

			

#print(">" + str(type)+":"+str(attribute)+":"+str(value))
print(fasta[int(start):int(stop)])
newFasta = fasta[int(start):int(stop)]
		
#print(len(fasta))
