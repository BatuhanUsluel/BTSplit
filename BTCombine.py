import argparse

parser = argparse.ArgumentParser("CSV & Excel Combiner")
parser.add_argument("-i", "--input", help="Text file with list of input files, seperated by new lines", type=str, required=True)
parser.add_argument("-o", "--output", help="Output file name", type=str, required=True)
parser.add_argument("-t", "--type", help="Output file type(.csv, .xls, .xlsx)", type=str, default=".xlsx")
parser.add_argument("-s", "--single", help="Combine the rows into a single sheet, instead of seperate(only for excel output)", action="store_true", default=False, required=False)
parser.add_argument("-sn", "--sheetname", help="Custom sheet prefix[default: file name]", type=str, required=False)
parser.add_argument("-tr", "--transition", help="Custom sheet transition", type=str, required=False, default = "_")
args = parser.parse_args()