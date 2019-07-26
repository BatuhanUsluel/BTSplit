import argparse
import pandas as pd
import os

parser = argparse.ArgumentParser("CSV Splitter")
parser.add_argument("-f", "--file", help="File Name(Required)", type=str, required=True)
parser.add_argument("-r", "--rows", help="Custom Number of rows per file[defualt: 1048576]", type=int, default=1048576, required=False)
parser.add_argument("-of", "--outputfile", help="Output file Prefix[defualt: input filename]", type=str, required=False)
parser.add_argument("-t", "--transition", help="Output file transition[defualt: _]", type=str, required=False, default = "_")
args = parser.parse_args()
print ("Output FIle:")
print (args.outputfile)

filename, file_extension = os.path.splitext(args.file)

if (args.outputfile==None):
    args.outputfile = filename
    
i=0
chunksize = args.rows
for chunk in pd.read_csv(args.file, chunksize=chunksize, skip_blank_lines=False, header=None):
    chunk.fillna("")
    chunk.to_csv(args.outputfile + args.transition + str(i) + file_extension, sep=',', index=False, header=False)
    print("-----------------------------------------")
    print(chunk)
    i=i+1