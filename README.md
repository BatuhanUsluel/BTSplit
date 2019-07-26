# Spreadsheet(CSV & Excel) Splitter
Can split .csv, .xlsx and .xls files into multiple smaller files or seperate sheets in excel.

Features:
  * Input number of rows per file
  * Input output file prefix
  * Input output files transition charecter
  * Input output type(Can convert from one type to another)
  * Split into multiple sheets in excel
  * Adjusts formula row references when diving into excel sheets
  
        usage: CSV Splitter [-h] -f FILE [-r ROWS] [-of OUTPUTFILE] [-t TRANSITION]
                    [-ot OUTPUTTYPE] [-s SEPERATE] [-aj ADJUSTFORMULAS]

        optional arguments:
            -h, --help            show this help message and exit
            -f FILE, --file FILE  File Name(Required)
            -r ROWS, --rows ROWS  Custom Number of rows per file[defualt: 1048576]
            -of OUTPUTFILE, --outputfile OUTPUTFILE
                  Output file Prefix[defualt: input filename]
            -t TRANSITION, --transition TRANSITION
                  Output file transition[defualt: _]
            -ot OUTPUTTYPE, --outputtype OUTPUTTYPE
                  Output file type(.csv, .xls, .xlsx)[defualt: input
                  type]
            -s SEPERATE, --seperate SEPERATE
                  Have seperate files(True, False)[defualt: False]
            -aj ADJUSTFORMULAS, --adjustformulas ADJUSTFORMULAS
                  Adjusts formulas in excel sheets, very computationally
                  expensive(True, False)[defualt: False]