"""
This is not the main python program for st-checker

This is a fork and continuation of www.github.com/commoncriteria/st-checker

st-checker is a WIP and gives no warranty

If you'd like to report a problem, please file an issue on either this repository or the main repo, and someone will try to correct that issue asap
"""
import sys
import re
import os
import subprocess
import platform
import time

currTime = time.strftime("%Y-%m-%d %H:%M:%S")

try:
    import lxml.etree as etree
except ImportError:
    print("Failed to import the proper ElementTree libraries needed. Please install \'lxml\' from pip.")
    sys.exit(0)

# def parseDocx(inDoc):
#     with open('temp/temp.txt','w+') as temp:
#     # print("parseDocx is being called")
#         import zipfile
#         try:
#             from xml.etree.cElementTree import XML
#         except ImportError:
#             from xml.etree.ElementTree import XML
#             print("Running in compatibility mode")
#         """
#         parseDocx is a derivative of <https://github.com/mickmaccana/python-docx>
#         """
#         WORD_NAMESPACE = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
#         PARA = WORD_NAMESPACE + 'p'
#         TEXT = WORD_NAMESPACE + 't'

#         document = zipfile.ZipFile(inDoc)
#         xml_content = document.read('word/document.xml')
#         document.close()
#         tree = XML(xml_content)
#         i = 0
#         paragraphs = []
#         for paragraph in tree.getiterator(PARA):
#             texts = [node.text
#                     for node in paragraph.getiterator(TEXT)
#                     if node.text]
#             if texts:
#                 paragraphs.append(''.join(texts))
#                 temp.write(repr(paragraphs))
#         return paragraphs ### this should be a list of all the stuf
#         # temp.write(paragraphs)

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

#this fscking works and I don't know why
def test():
    presentRules = []
    missingRules = []
    lineNum = 1
    rulesheet = newGenerateRuleSheet()
    with open('temp/temp.txt',) as pprofile, open('temp/line.txt','w+') as liner, open('temp/itemize.txt','w+') as itemize, open('output/'+currTime+'.xml','wb') as test:
        for line in pprofile:
            lineNum = lineNum + 1
            for item in rulesheet:
                if item.lower() in line.lower():
                    presentRules.append(item)
                    liner.write(line)
                    itemize.write(item+'\n')
        presentRules = list(set(presentRules))
        presentRules.sort()
        missingRules = [x for x in rulesheet if x not in presentRules]
        missingRules.sort()
        print(len(presentRules),' present rules')
        print(len(missingRules),' missing rules')
        root = etree.Element('PP_Rules')
        xmlRules = etree.SubElement(root, 'Present_Rules')
        xmlRules.text = str(presentRules)
        xmlMissing = etree.SubElement(root, 'Missing_Rules')
        xmlMissing.text = str(missingRules)
        test.write((etree.tostring(root, pretty_print=True)))


# deprecated
# with open('config.json') as configFile:
#     data = json.load(configFile)
#     configData = (data['os_path'] + data['found'])


# if not os.path.exists('config.json'):
#     print("Run config.py before running st-checker.py")
#     sys.exit(0)

#firstly checks the args before even loading the rest of the program
# if len(sys.argv) != 2:
#     print("Usage: <st-checker.py> <security-target>") #will have to double check this
#     sys.exit(0)

# if platform.system() == 'Windows':
#     print("Right now, st-checker only works on Linux and macOS. If you are seeing this and you are running Linux or macOS, I did something wrong.")
#     sys.exit(0)

# absFilePath, fileExtension = os.path.splitext(sys.argv[-1])
# fileName = re.sub('^(.*[\\\/])','',absFilePath)

# if fileExtension.lower() == ('.docx'):
#     parseDocx(sys.argv[-1])
# #     #fileparse.docxparse(sys.argv[-1], 'output/rippedWord.txt')
# #     #print("doc")
# if fileExtension.lower() == ('.pdf'):
#     inputFile = sys.argv[-1]
#     #subprocess.Popen(['pdftotext', inputFile,'temp/temp.txt'])
# #    os.system('pdftotext', sys.argv[-1],'temp/temp.txt')
# #     ripPdf()
# #     #print("pdf")
# # else:
# #     print("File must be .docx or .pdf")
# #     sys.exit(0)

test()