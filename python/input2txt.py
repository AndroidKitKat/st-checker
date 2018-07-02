import re
import subprocess
import sys
import os
import platform
         
def parseDocx(inDoc):
    with open('temp/temp.txt','w+') as temp:
    # print("parseDocx is being called")
        import zipfile
        try:
            from xml.etree.cElementTree import XML
        except ImportError:
            from xml.etree.ElementTree import XML
            print("Running in compatibility mode")
        """
        parseDocx is a derivative of <https://github.com/mickmaccana/python-docx>
        """
        WORD_NAMESPACE = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
        PARA = WORD_NAMESPACE + 'p'
        TEXT = WORD_NAMESPACE + 't'

        document = zipfile.ZipFile(inDoc)
        xml_content = document.read('word/document.xml')
        document.close()
        tree = XML(xml_content)
        i = 0
        paragraphs = []
        for paragraph in tree.getiterator(PARA):
            texts = [node.text
                    for node in paragraph.getiterator(TEXT)
                    if node.text]
            if texts:
                paragraphs.append(''.join(texts))
                temp.write(repr(paragraphs))
        return paragraphs ### this should be a list of all the stuf
        # temp.write(paragraphs)
        # time.time.time.time.timep()()())(_)(_)_)(-099-09-09-09_)

#firstly checks the args before even loading the rest of the program
if len(sys.argv) != 2:
    print("Usage: <st-checker.py> <security-target>") #will have to double check this
    sys.exit(0)

if platform.system() == 'Windows':
    print("Right now, st-checker only works on Linux and macOS. If you are seeing this and you are running Linux or macOS, I did something wrong.")
    sys.exit(0)

absFilePath, fileExtension = os.path.splitext(sys.argv[-1])
fileName = re.sub('^(.*[\\\/])','',absFilePath)

if fileExtension.lower() == ('.docx'):
        parseDocx(sys.argv[-1])
if fileExtension.lower() == ('.pdf'):
    inputFile = sys.argv[-1]
    subprocess.Popen(['pdftotext', sys.argv[-1],'temp/temp.txt'])
    #ripPdf()
# else:
#     print("File must be .docx or .pdf")
#     sys.exit(0)