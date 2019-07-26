import argparse
import pandas as pd
import os
import xlsxwriter


def readFile(file, chunksize, extension):
    print (extension)
    if (extension==".csv"):
        return pd.read_csv(args.file, chunksize=chunksize, skip_blank_lines=False, header=None)
    elif (extension==".xlsx" or extension==".xls"):
        excel_file = pd.read_excel(args.file, skip_blank_lines=False, header=None)
        return [excel_file[i:i+chunksize] for i in range(0,excel_file.shape[0],chunksize)]
    else:
        return None
        
def writeFile(chunk, outputFileName, transition, i, extension):
    if (extension==".csv"):
        chunk.to_csv(outputFileName+ transition + str(i) + extension, sep=',', index=False, header=False)
    elif (extension==".xlsx" or extension==".xls"):
        writer = pd.ExcelWriter(outputFileName+ transition + str(i) + extension, engine='xlsxwriter')
        chunk.to_excel(writer, sheet_name = 'sheet1', index=False, header=False)
        writer.save()
    else:
        return None
parser = argparse.ArgumentParser("CSV Splitter")
parser.add_argument("-f", "--file", help="File Name(Required)", type=str, required=True)
parser.add_argument("-r", "--rows", help="Custom Number of rows per file[defualt: 1048576]", type=int, default=1048576, required=False)
parser.add_argument("-of", "--outputfile", help="Output file Prefix[defualt: input filename]", type=str, required=False)
parser.add_argument("-t", "--transition", help="Output file transition[defualt: _]", type=str, required=False, default = "_")
args = parser.parse_args()

filename, file_extension = os.path.splitext(args.file)

if (args.outputfile==None):
    args.outputfile = filename
    
i=0
chunksize = args.rows
for chunk in readFile(args.file,args.rows,file_extension):
    chunk.fillna("")
    writeFile(chunk, args.outputfile, args.transition, i, file_extension)
    print("-----------------------------------------")
    print(chunk)
    i=i+1