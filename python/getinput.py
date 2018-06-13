import os
import sys
import re
import fileparse

if len(sys.argv) != 2:
    print("Usage: <get-input.py> <input.file>")
    sys.exit(0)

absFilePath, fileExtension = os.path.splitext(sys.argv[-1])
fileName = re.sub('^(.*[\\\/])','',absFilePath)

#checks file extension
if fileExtension.lower() == ('.docx'):
    fileparse.docxparse(sys.argv[-1], 'output/rippedWord.txt')
elif fileExtension.lower() == ('.pdf'):
    fileparse.pdfparse(sys.argv[-1],'output/rippedpdf.txt')
else:
    print("File must be .docx or .pdf")
    sys.exit(0)