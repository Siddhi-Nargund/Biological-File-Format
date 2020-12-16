#!/usr/bin/python3
#!/usr/bin/env python3

def isValidSequence(seq):
	check_array = ['A','T','G','C']
	for i in seq:
		if i not in check_array:
			return False
	return True
#To check if Sequence consists of only A,T,G,C

def inputSequence():
	seq = str(raw_input("Please Enter Your Sequence: "))
	print(seq)
	return seq
#To input sequence from the user

def reverseSequence(seq):
	revString = seq[::-1]
	#print(revString)
	return revString
#To reverse the sequence

def findComplement(seq):
	complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
	return ''.join([complement[base] for base in seq[:]])
#To find complement of the sequence

#First Drive
seq = inputSequence()
#print(seq)
tmp = isValidSequence(seq)
while tmp:
	#print(seq)
	#rev = reverseSequence(seq)
	compl = findComplement(seq)
	#print(compl)
	rev = reverseSequence(compl)
	#print("Reverse Complement: ")
	print(rev)
	seq = inputSequence()
	tmp = isValidSequence(seq)
