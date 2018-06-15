"""
This is the main python program for st-checker

This is a fork and continuation of www.github.com/commoncriteria/st-checker

st-checker is a WIP and gives no warranty

If you'd like to report a problem, please file an issue on either this repository or the main repo, and someone will try to correct that issue asap
"""

import sys
import re
import os
import subprocess
import platform
try:
    import lxml.etree
except ImportError:
    raise ImportError('st-checker.py will not work without lxml installed. Install lxml and try again.')

if not os.path.exists('congfig.json'):
    print("Run config.py before running st-checker.py")
    sys.exit(0)

#firstly checks the args before even loading the rest of the program
if len(sys.argv) != 2:
    print("Usage: <st-checker.py> <protection-profile>") #will have to double check this
    sys.exit(0)

if platform.system() == 'Windows':
    print("Right now, st-checker only works on Linux and macOS. If you are seeing this and you are running Linux or macOS, I did something wrong.  ")
    sys.exit(0)

#gets input file and makes sure its valid
def getInput(inputFile):
    absFilePath, fileExtension = os.path.splitext(sys.argv[-1])
    fileName = re.sub('^(.*[\\\/])','',absFilePath)

    if fileExtension.lower() == ('.docx'):
        return parseDocx(sys.argv[-1])
        #fileparse.docxparse(sys.argv[-1], 'output/rippedWord.txt')
        #print("doc")
    elif fileExtension.lower() == ('.pdf'):
        #fileparse.pdfparse(sys.argv[-1],'output/rippedpdf.txt')
        return parsePdf(sys.argv[-1])
        #print("pdf")
    else:
        print("File must be .docx or .pdf")
        sys.exit(0)
    
def parseDocx(inDoc):
    print("parseDocx is being called")
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
    return paragraphs ### this should be a list of all the stuff        

def parsePdf(inPdf):
    print("parsePdf is being called")
    subprocess.Popen(['pdftotext', sys.argv[-1],'temp/temp.txt'])
    rippedpdf = []
    with open('temp/temp.txt') as temp:
        for line in temp:
            #line = line.strip('\n')
            rippedpdf.append(line.strip('\n'))
    return [item for item in rippedpdf if item]


#def findRulesTemplate():

def generateRuleSheet():
    subprocess.Popen(['xsltproc', '-o', 'rules/OsRules.xsl', 'xsl/RuleGenerator.xsl', '~/Documents/operatingsystem/input/operatingsystem.xml'])

def getRulesFromSheet(ruleFile):
	with open(ruleFile) as ruleSheet:
			xml = lxml.etree.fromstring(ruleSheet.read())
			badRules = xml.xpath('.//axsl:when/@test', namespaces=xml.nsmap)
			goodRules = []
			for item in badRules:
				item = repr(item)
				item = item.replace('//*[@id=\'','')
				item = item.replace('\']','')
				item = item.strip('\"')
				goodRules.append(item)
	return(goodRules)
userInput = getInput(sys.argv[-1])

if not os.path.exists('rules/OsRules.xsl'):
    generateRuleSheet()


#rulesList = getRulesFromSheet(file)