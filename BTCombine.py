import argparse
import pandas as pd
import os

parser = argparse.ArgumentParser("CSV & Excel Combiner")
parser.add_argument("-i", "--input", help="Text file with list of input files, seperated by new lines", type=str, required=True)
parser.add_argument("-o", "--output", help="Output file name", type=str, required=True)
parser.add_argument("-t", "--type", help="Output file type(.csv, .xls, .xlsx)", type=str, default=".xlsx")
parser.add_argument("-s", "--single", help="Combine the rows into a single sheet, instead of seperate(only for excel output)", action="store_true", default=False, required=False)
parser.add_argument("-sn", "--sheetname", help="Custom sheet prefix[default: file name]", type=str, required=False)
parser.add_argument("-tr", "--transition", help="Custom sheet transition", type=str, required=False, default = "_")
args = parser.parse_args()


def readFile(file, file_extension):
    print ("exten: " + file_extension)
    if (file_extension==".csv"):
        print ("reading csv")
        return pd.read_csv(file, skip_blank_lines=False, header=None)
    elif (file_extension==".xlsx" or file_extension==".xls"):
        return pd.read_excel(file, skip_blank_lines=False, header=None)

def write(data, file, file_extension):
    if (file_extension==".csv"):
        data.to_csv(file + file_extension, sep=',', index=False, header=False)
    elif (file_extension==".xlsx" or file_extension==".xls"):
        writer = pd.ExcelWriter(file+file_extension, engine='xlsxwriter')   
        data.to_excel(writer, sheet_name = 'sheet1', index=False, header=False)
        writer.save()
        writer.close()
        
datatotal = pd.DataFrame()
f = open(args.input, "r")
for file in f:
    file = file.rstrip()
    filename, file_extension = os.path.splitext(file)
    data = readFile(file, file_extension.rstrip())
    if (args.single):
        datatotal = datatotal.append(data)
        
write(datatotal, args.output, args.type)