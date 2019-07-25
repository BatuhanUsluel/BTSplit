import argparse
import pandas as pd

parser = argparse.ArgumentParser("CSV Splitter")
parser.add_argument("-f", "--file", help="File Name(Required)", type=str, required=True)
parser.add_argument("-r", "--rows", help="Custom Number of rows per file[defualt: 1048576]", type=int, default=1048576, required=False)
parser.add_argument("-of", "--outputfile", help="Output file Prefix[defualt: input filename]", type=str, required=False)
parser.add_argument("-t", "--transition", help="Output file transition[defualt: _]", type=str, required=False, default = "_")
args = parser.parse_args()
print ("Output FIle:")
print (args.outputfile)

sep = '.'
file_no_extension = args.file.split(sep, 1)[0]

if (args.outputfile==None):
    args.outputfile = file_no_extension
    
i=0
chunksize = args.rows
first=True
for chunk in pd.read_csv(args.file, chunksize=chunksize):
    chunk.to_csv(args.outputfile + args.transition + str(i) + ".csv", sep=',', index=False, header=first)
    print("-----------------------------------------")
    print(chunk)
    i=i+1
    if (first):
        first=False