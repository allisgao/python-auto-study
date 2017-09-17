#! python3
# 9.4_renameDates.py - Rename filenames with American MM-DD-YYYY date format
# to Europen DD-MM-YYYY.

import shutil, os, re

# Create a regex that matches files with the American date format.
datePattern = re.compile(r"""^(.*?)  # all test before the date
    ((0|1)?\d)-      # 1 or 2 digits for the month
    ((0|1|2|3)?\d)-  # 1 or 2 digits for the day
    ((19|20)\d\d)    # 4 digits for the year —— 本示例仅作演示，查看19XX和2XXX年
    (.*?)$           # all the text after the date
    """,re.VERBOSE)

# Loop over the files in the working directory
for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)

    # Skip files without a date.
    if mo == None:
        continue

    # Get the different parts of the filename.
    # 此处有个难点，正则表达式的分组
    beforePart = mo.group(1)
    monthPart  = mo.group(2)
    dayPart    = mo.group(4)
    yearPart   = mo.group(6)
    afterPart  = mo.group(8)

    # Form the European-style filename.
    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

    #  Get the full, absolute file paths.
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)

    # Rename the files.
    print('Renaming "%s" to "%s" ... ' % (amerFilename,euroFilename))




















