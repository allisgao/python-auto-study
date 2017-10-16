#! python3
###########
# Failed  #
###########
# Usage:
# py SCRIPT.py NUM
#   create an multi Excel from 1 to NUM.
import openpyxl
import sys
wb = openpyxl.Workbook()
sheet = wb.get_active_sheet()
num = sys.argv[1]   # row
myStr = 'ABCDEFG' # column
for i in range(1, int(num)+1):
    # Print column-A:  A1 to A7
    sheet['A' + str(i+1)] = i
    # Print row-1: B1, C1, ..., G1
    for j in myStr:
        sheet[myStr[i:] +'1'] = i
    # Fill the body
    sheet[myStr[i+1:] + 'i+1'] = i*i
wb.save('myMulty.xlsx')
