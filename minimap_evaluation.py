
#/usr/bin/python3
#!/usr/bin/env python3

import pandas as pd
import csv
import xlsxwriter


# with open('RevisedTranscripts.sam') as inf, open('useless.txt','w') as of1, open('ReadsCompare.sam','w') as of2:
#     outf = of1
#     for line in inf:
#         if '@PG' in line:
#             outf = of2
#             continue  # prevent output of the line with "string pattern"
#         outf.write(line)

with open('ReadsCompare.sam') as f:
    var= f.readlines()[1:]
    temp=[]
    from pandas import DataFrame
    for line in var:
        split_str=line.split("\t")
        print(split_str)
        compareColumns=(split_str[0],split_str[2])
       # print(compareColumns)
        temp.append(compareColumns)
    #Saving column 1 and column 3 in an array
    #print(temp)

#Converting array into dataframe
df=pd.DataFrame(temp)
#Naming columns
df.columns=['ref','transcript']
#print(df)

df= df['ref'].groupby(df['transcript']).unique()
# print(type(forExcel))
# forExcel.to_csv("ReadGroup.csv")
print(df)






# NO need of csv.comple
# quantify reads for each transcript
# shared 
# unique
