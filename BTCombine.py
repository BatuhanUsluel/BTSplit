import argparse
import pandas as pd
import os
from openpyxl import load_workbook
import glob

parser = argparse.ArgumentParser("CSV & Excel Combiner")
parser.add_argument('-f','--filter', nargs='+', help='File filters using wildcards to select input files (Ex: *.csv)', required=False)
parser.add_argument("-i", "--input", help="Text file with list of input files, seperated by new lines", type=str, required=False)
parser.add_argument("-o", "--output", help="Output file name", type=str, required=True)
parser.add_argument("-t", "--type", help="Output file type(.csv, .xls, .xlsx)[Default: .xlsx]", type=str, default=".xlsx")
parser.add_argument("-s", "--single", help="Combine the rows into a single sheet, instead of seperate(only for excel output)[Default: False]", action="store_true", default=False, required=False)
parser.add_argument("-sn", "--sheetname", help="Custom sheet prefix[Default: file name]", type=str, required=False)
parser.add_argument("-tr", "--transition", help="Custom sheet transition[Default: None]", type=str, required=False, default = "")
parser.add_argument("-fv", "--formulavalue", help="When enabled gets excel formula values instead of formulas", action="store_true", required=False, default = False)
args = parser.parse_args()

print("Filter: " + str(args.filter))
def readFile(file, file_extension, formulavalue):
    if (file_extension==".csv"):
        return pd.read_csv(file, skip_blank_lines=False, header=None)
    elif (file_extension==".xlsx" or file_extension==".xls"):
        if formulavalue:
            return pd.read_excel(file, skip_blank_lines=False, header=None)
        else:
            wb = load_workbook(filename = file)
            sheet_names = wb.get_sheet_names()
            name = sheet_names[0]
            sheet_ranges = wb[name]
            excel_file = pd.DataFrame(sheet_ranges.values)
            return excel_file

def write(data, file, file_extension, i, sheetname, transition, filename):
    if (file_extension==".csv"):
        data.to_csv(file + file_extension, sep=',', index=False, header=False)
    elif (file_extension==".xlsx" or file_extension==".xls"):
        global writer
        if writer == None:
            writer = pd.ExcelWriter(file+file_extension, engine='xlsxwriter')
        name=""
        if (sheetname==None):
            name = filename
        else:
            name = sheetname + transition + str(i)
        data.to_excel(writer, sheet_name = name, index=False, header=False)
    
if (not (args.type == ".csv" or args.type == ".xls" or args.type == ".xlsx")):
    print ("Output type " + args.type + " invalid. Valid output types are: .csv, .xls, .xlsx")
    print ("Quitting")
    quit()
    
writer = None
i=1
datatotal = pd.DataFrame()
f = None

lookedfiles = []
for filter in args.filter:
    files = glob.glob(filter)
    for file in files:
        print (file)
        file = file.rstrip()
        filename, file_extension = os.path.splitext(file)
        data = readFile(file, file_extension.rstrip(), args.formulavalue)
        if (args.single or args.type==".csv"):
            datatotal = datatotal.append(data)
        else:
            write(data, args.output, args.type, i, args.sheetname, args.transition, filename)
            i=i+1
        lookedfiles.append(file)
        
if (args.input==None and args.filter == None):
    print ("You gave no way to select input files. Please either use -i or -f. Use -h for more help & information")
    print ("Quitting")
    quit()
    
if (args.input!=None):
    try:
        f = open(args.input, "r")
    except FileNotFoundError:
        print ("Input file " + args.input + " not found, quitting")
        quit()
    for file in f:
        if (file not in lookedfiles):
            file = file.rstrip()
            filename, file_extension = os.path.splitext(file)
            data = readFile(file, file_extension.rstrip(), args.formulavalue)
            if (args.single or args.type==".csv"):
                datatotal = datatotal.append(data)
            else:
                write(data, args.output, args.type, i, args.sheetname, args.transition, filename)
                i=i+1
            
if (args.single or args.type==".csv"):
    write(datatotal, args.output, args.type, i, args.sheetname, args.transition, "")

if (writer!=None):
    writer.save()
    writer.close()