import argparse
import pandas as pd
import os
import xlsxwriter
from openpyxl import load_workbook
import re

def readFile(file, chunksize, extension, outputtype):
    print (extension)
    if (extension==".csv"):
        return pd.read_csv(args.file, chunksize=chunksize, skip_blank_lines=False, header=None)
    elif (extension==".xlsx" or extension==".xls"):
        if (outputtype==".csv"):
            excel_file = pd.read_excel(args.file, skip_blank_lines=False, header=None)
        elif(outputtype==".xlsx" or outputtype==".xls"):
            wb = load_workbook(filename = args.file)
            sheet_names = wb.get_sheet_names()
            name = sheet_names[0]
            sheet_ranges = wb[name]
            excel_file = pd.DataFrame(sheet_ranges.values)
        return [excel_file[i:i+chunksize] for i in range(0,excel_file.shape[0],chunksize)]
    else:
        return None

def adjustNumber(match):
    global i
    global chunksize
    #print(i)
    match = match.group()
    return str(int(match)-(i*chunksize))
    
def helper(a):
    if (str(a)[:1]!="="):
        return a
    pattern = '(?<=[A-Z]).\d{1,7}(?=(?:[^"]*"[^"]*")*[^"]*$)'
    r2 = re.sub(pattern, adjustNumber, str(a))
    return r2
        
def writeFile(chunk, outputFileName, transition, i, extension, seperate, adjustformulas):
    if (extension==".csv"):
        chunk.to_csv(outputFileName+ transition + str(i) + extension, sep=',', index=False, header=False)
    elif (extension==".xlsx" or extension==".xls"):
        if (seperate==False):
            if (adjustformulas):
                chunk = chunk.applymap(helper) 
            global writer
            if (writer==None):
                writer = pd.ExcelWriter("split_" + outputFileName + extension, engine='xlsxwriter')   
            chunk.to_excel(writer, sheet_name = 'sheet' + str(i), index=False, header=False)
        else:
            writer = pd.ExcelWriter(outputFileName+ transition + str(i) + extension, engine='xlsxwriter')
            chunk.to_excel(writer, sheet_name = 'sheet1', index=False, header=False)
            writer.save()
            writer.close()
    else:
        return None

parser = argparse.ArgumentParser("CSV Splitter")
parser.add_argument("-f", "--file", help="File Name(Required)", type=str, required=True)
parser.add_argument("-r", "--rows", help="Custom Number of rows per file[defualt: 1048576]", type=int, default=1048576, required=False)
parser.add_argument("-of", "--outputfile", help="Output file Prefix[defualt: input filename]", type=str, required=False)
parser.add_argument("-t", "--transition", help="Output file transition[defualt: _]", type=str, required=False, default = "_")
parser.add_argument("-ot", "--outputtype", help="Output file type(.csv, .xls, .xlsx)[defualt: input type]", type=str, required=False)
parser.add_argument("-s", "--seperate", help="Have seperate files(True, False)[defualt: False]", type=str, required=False, default = False)
parser.add_argument("-aj", "--adjustformulas", help="Adjusts formulas in excel sheets, very computationally expensive(True, False)[defualt: False]", type=str, required=False, default = False)
args = parser.parse_args()

filename, file_extension = os.path.splitext(args.file)

if (args.outputfile==None):
    args.outputfile = filename
   
if (args.outputtype==None):
    args.outputtype = file_extension

i=0
chunksize = args.rows
writer = None
for chunk in readFile(args.file,args.rows,file_extension, args.outputtype):
    #print(list(chunk.columns))
    chunk.fillna("")
    writeFile(chunk, args.outputfile, args.transition, i, args.outputtype, args.seperate, args.adjustformulas)
    #print("-----------------------------------------")
    #print(chunk)
    i=i+1
    
if (writer!=None):
    writer.save()
    writer.close()
    
#Project ToDo:
#Add support for formulas in rows following Z(AA,AB) - Regex
#Formulas seperated in different sheets can referance each other
#Optimize, test what takes time

