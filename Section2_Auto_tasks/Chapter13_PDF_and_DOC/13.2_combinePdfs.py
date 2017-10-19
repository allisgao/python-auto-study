#! python3
# combinePdfs.py - Combines all the current working directory into
# a single PDF.

import os, PyPDF2

# Get all the PDF filenames.
pdfFiles = []
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)
pdfFiles.sort(key=str.lower)
pdfWrite = PyPDF2.PdfFileWriter()

# Loop through all the PDF files.
for filename in pdfFiles:
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    # Loop through all the pages (except the first) and add them.
    for pageNum in range(1, pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWrite.addPage(pageObj)
# Save theresulting PDF to a file.
pdfOutput = open('allminutes_gjz.pdf', 'wb')
pdfWrite.write(pdfOutput)
pdfOutput.close()

