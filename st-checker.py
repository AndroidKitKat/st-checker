"""
This is not the main python program for st-checker

This is a fork and continuation of www.github.com/commoncriteria/st-checker

st-checker is a WIP and gives no warranty

If you'd like to report a problem, please file an issue on either this repository or the main repo, and someone will try to correct that issue asap
"""

import sys
import re
import subprocess
import os
import platform
import time

currTime = time.strftime("%Y-%m-%d %H:%M:%S")

try:
    import lxml.etree as etree
except ImportError:
    print("Failed to import the proper ElementTree libraries needed. Please install \'lxml\' from pip.")
    sys.exit(0)

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
def makeSchema():
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
        root = etree.Element('PP_Rules')#, nsmap={None: "http://relaxng.org/ns/structure/1.0"}) 
        xmlRules = etree.SubElement(root, 'Present_Rules')
        xmlRules.text = str(presentRules)
        xmlMissing = etree.SubElement(root, 'Missing_Rules')
        xmlMissing.text = str(missingRules)
        test.write((etree.tostring(root, pretty_print=True)))
makeSchema()