import argparse 
import gzip 
import os  

def fastqOperation(fq):
    lineCount = 0
    completeCount = 0
    for line in fq:
        lineCount += 1
    # computeLines = []
    #Starting with second line and skipping by 3 lines
    for i in range(1,lineCount,4):
        #print(i)
        currLine = fq[i]
        currLine = currLine.rstrip()
        currLine = currLine.decode("utf-8")
        # print(currLine)
        completeCount += len(currLine)
        # computeLines.append(currLine)
    print("Total number of Residues are : " +str(completeCount))
    readCount = 0
    for i in range(0,lineCount,4):
        #print(i)
        read = fq[i]
        read = read.rstrip()
        read = read.decode("utf-8")
        # print(read)
        readCount += 1
        # computeLines.append(currLine)
    print("Total number of reads are : "+str(readCount))

def fastaOperation(fa):
    total_residues = 0
    seq_count = 0
    for line in fa:         
        if line.startswith(b'>'):             
            seq_count += 1         
        else:             
            total_residues += len(line)      
    print("\nTotal sequences found: {0}".format(seq_count));     
    print("Total residues found : {0}\n\n".format(total_residues));    

def main(): 
    parser = argparse.ArgumentParser( description='Basic sequence statistics reporter for FASTA files')     
    ## output file to be written     
    parser.add_argument('-i', '--input_file', type=str, required=True, help='Path to an input file to be read' )     
    args = parser.parse_args()  

    #Checking the extension of file if compressed
    if args.input_file.endswith('gz') or args.input_file.endswith('bz'):         
        fh = gzip.open( args.input_file, 'rb').readlines()        
        is_compressed = True     
        for line in fh:
            if is_compressed:          
                line = line.decode()                        
            line = line.rstrip()
        tempLine = fh.pop(0)
        tempLine = tempLine.decode('UTF-8')
        #print(tempLine)
        #Checking if compressed file is in fasta or fastq file format
        if '>' in tempLine:
            fastaOperation(fh)
        elif '@' in tempLine:
            fastqOperation(fh)
        
    elif args.input_file.endswith('fastq'):         
        fq = open( args.input_file, 'rb' ).readlines()        
        is_compressed = False    
        fastqOperation(fq) #Calling module if file in fastq format and passing the file as argument
    elif args.input_file.endswith('fasta'): 
        fa = open( args.input_file, 'rb').readlines() 
        is_compressed= False
        fastaOperation(fa) #Calling module if file in fasta format and passing the file as argument
  
if __name__ == '__main__':     
    main()