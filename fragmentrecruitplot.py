import matplotlib.pyplot as plt 
import argparse
import csv
import matplotlib as mpl
import numpy as np

parser = argparse.ArgumentParser(description='Enter File location')
parser.add_argument('-i',type=str,dest="InputFileName")
args = parser.parse_args()

fileToOpen = args.InputFileName 

with open(fileToOpen, 'rb') as f:
    f= ["Lactobacillus_crispatus.csv"]#, "Lactobacillus_iners.csv","Atopobium_vaginae.csv", "Staphylococcus_epidermidis.csv", "Mycoplasma_homini.csv", "Lactobacillus_jensenii.csv","Lactobacillus_gasseri.csv", "Gardnerella_vaginalis.csv"]
    for file in f:
        position= []
        percenIdentity= []
        with open(file) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for i,row in enumerate(csv_reader):
                if i==0: # or i > 10000:
                    continue
                position.append(int(row[1]))
                percenIdentity.append(float(row[2]))
            #position = np.array(position)
            #position = position/position.max()
            plt.scatter(position, percenIdentity, s=0.1, label = file)

#print(len(position))
lg= plt.legend( prop={'size': 6}, markerscale= 9)
plt.xlabel('Position')
plt.ylabel('Percent Identity')
plt.ticklabel_format(axis="x", style="plain")
mpl.rcParams['agg.path.chunksize'] = 1000 * len(position)

#plt.savefig("fig.png")
plt.show()