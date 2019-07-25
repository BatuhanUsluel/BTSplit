import argparse

parser = argparse.ArgumentParser("CSV Splitter")
parser.add_argument("-f", "--file", help="File Name(Required)", type=str, required=True)
parser.add_argument("-r", "--rows", help="Custom Number of rows per file[defualt: 1048576]", type=int, default=1048576, required=False)
parser.add_argument("-of", "--outputfile", help="Output file Prefix[defualt: input filename]", type=str, required=False)
parser.add_argument("-t", "--transition", help="Output file transition[defualt: _]", type=str, required=False)
args = parser.parse_args()