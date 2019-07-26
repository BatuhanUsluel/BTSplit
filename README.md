# Spreadsheet(CSV & Excel) Splitter
Can split .csv, .xlsx and .xls files into many smaller files based on the given row count. Main development purpose was to split large files into the excel row limit of 1048576.

usage: CSV Splitter [-h] -f FILE [-r ROWS] [-of OUTPUTFILE] [-t TRANSITION]

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  File Name(Required)
  -r ROWS, --rows ROWS  Custom Number of rows per file[defualt: 1048576]
  -of OUTPUTFILE, --outputfile OUTPUTFILE
                        Output file Prefix[defualt: input filename]
  -t TRANSITION, --transition TRANSITION
                        Output file transition[defualt: _]