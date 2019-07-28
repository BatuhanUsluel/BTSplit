# Spreadsheet(CSV & Excel) Splitter

BTSplit
------
Can split .csv, .xlsx and .xls files into multiple smaller files or seperate sheets in excel.

  * Input number of rows per file
  * Input output file prefix
  * Input output files transition charecter
  * Input output type(Can convert from one type to another)
  * Split into multiple sheets in excel
  * Adjusts formula row references when diving into excel sheets
  
        usage: CSV & Excel Splitter [-h] -f FILE [-r ROWS] [-of OUTPUTFILE] [-t TRANSITION]
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
BTCombine
------
Can combine a list of excel and csv files, either adding up the rows consecutively or into diffrent sheets in excel.
  * List input files in a text file
  * Can input a combination of csv and excel files
  * Can output as an excel or csv
  * When outputting as an excel, it can place each file in its own sheets using the filenames or a custom prefix & counter
  
          usage: CSV & Excel Combiner [-h] -i INPUT -o OUTPUT [-t TYPE] [-s]
                                    [-sn SHEETNAME] [-tr TRANSITION]

        optional arguments:
          -h, --help            show this help message and exit
          -i INPUT, --input INPUT
                                Text file with list of input files, seperated by new
                                lines
          -o OUTPUT, --output OUTPUT
                                Output file name
          -t TYPE, --type TYPE  Output file type(.csv, .xls, .xlsx)
          -s, --single          Combine the rows into a single sheet, instead of
                                seperate(only for excel output)
          -sn SHEETNAME, --sheetname SHEETNAME
                                Custom sheet prefix[default: file name]
          -tr TRANSITION, --transition TRANSITION
                                Custom sheet transition
