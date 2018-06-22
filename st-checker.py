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
import json
import time

currTime = time.strftime("%Y-%m-%d %H:%M:%S")

try:
    import lxml.etree as etree
except ImportError:
    print("Failed to import the proper ElementTree libraries needed. Install \'lxml\' from pip.")
    sys.exit(0)
# deprecated
# with open('config.json') as configFile:  
#     data = json.load(configFile)
#     configData = (data['os_path'] + data['found'])


# if not os.path.exists('config.json'):
#     print("Run config.py before running st-checker.py")
#     sys.exit(0)

#firstly checks the args before even loading the rest of the program
if len(sys.argv) != 2:
    print("Usage: <st-checker.py> <security-target>") #will have to double check this
    sys.exit(0)

if platform.system() == 'Windows':
    print("Right now, st-checker only works on Linux and macOS. If you are seeing this and you are running Linux or macOS, I did something wrong.")
    sys.exit(0)

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

def parsePdf(inPdf):
    # print("parsePdf is being called")
    subprocess.Popen(['pdftotext', sys.argv[-1],'temp/temp.txt'])
    rippedpdf = []
    with open('temp/temp.txt') as temp:
        for line in temp:
            #line = line.strip('\n')
            rippedpdf.append(line.strip('\n'))
    return [item for item in rippedpdf if item]

# def generateRuleSheet():
#     if configData[1] == '1':
#         subprocess.Popen(['xsltproc', '-o', 'rules/OsRules.xsl', 'xsl/RuleGenerator.xsl', configData[0] + 'input/operatingsystem.xml'])
#     elif configData[1] == '0':
#         print('balls')
#     return getRulesFromSheet('rules/OsRules.xsl')

def newGenerateRuleSheet():
    if not os.path.exists('rules/OsRules.xsl'):
        subprocess.Popen(['curl','-soc','rules/OsRules.xsl','https://github.com/AndroidKitKat/st-checker/releases/download/whyDoINeedThis/OsRules.xsl'])
    return getRulesFromSheet('rules/OsRules.xsl')


def getRulesFromSheet(ruleFile):
	with open(ruleFile) as ruleSheet:
			xml = etree.fromstring(ruleSheet.read())
			badRules = xml.xpath('.//axsl:when/@test', namespaces=xml.nsmap)
			goodRules = []
			for item in badRules:
				item = repr(item)
				item = item.replace('//*[@id=\'','')
				item = item.replace('\']','')
				item = item.strip('\"')
				goodRules.append(item)
	return goodRules

#this is broken and i dont know why
def checkST(ruleList):
    with open('temp/temp.txt') as pprofile, open('output/'+currTime+'-output.txt', "w+") as output:
        count = 0
        match = 0
        #print(ruleList)
        for item in ruleList:
            for line in pprofile:
                if item.lower() in line.lower():
                    #print(pprofile.readline())
                    #print(item)
                    output.write('PP has '+item+'\n')
                    #print("balls")
                    #print('Missing '+ item)
                else:
                    output.write('PP is missing '+item+'\n')
                    count = count + 1
        print('Security Target is missing ', str(((count / len(ruleList))) * 100) ,'% of the Protection Profile')

#this fscking works and I don't know why
def test():
    presentRules = []
    missingRules = []
    lineNum = 1
    rulesheet = newGenerateRuleSheet()
    with open('temp/temp.txt') as pprofile, open('temp/fark1.txt','w+') as poop, open('temp/poop1.txt','w+') as fark:
        for line in pprofile:
            lineNum = lineNum + 1
            for item in rulesheet:
                if item.lower() in line.lower():
                    presentRules.append(item)
                    poop.write(line)
                    fark.write(item+'\n')
    presentRules = list(set(presentRules))
    missingRules = [x for x in rulesheet if x not in presentRules]

    root = etree.Element('PP_Rules')
    xmlRules = etree.SubElement(root, 'Present_Rules')
    xmlMissing = etree.SubElement(root, 'Missing_Rules')
    # for item in presentRules:
    #     xmlRules.append(etree.Element(item))
    # for item in missingRules:
    #     xmlMissing.append(etree.Element(item))
    root.write(sys.stdout, pretty_print=True)
        

def cleanOutput(clearOutput, clearTemp):
    import shutil
    if clearOutput == 0:
        shutil.rmtree('output/')
        os.makedirs('output/')
    if clearTemp == 0:
        shutil.rmtree('temp/')
        os.makedirs('temp/')

def main():    
    document = getInput(sys.argv[-1])
    rulesheet = newGenerateRuleSheet()
    checkST(rulesheet)
    cleanOutput(1,1)

test()