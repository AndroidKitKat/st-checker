import os
import subprocess
import sys

try:
    import lxml.etree as etree
except ImportError:
    print("Failed to import the proper ElementTree libraries needed. Install \'lxml\' from pip.")
    sys.exit(0)

def newGenerateRuleSheet():
    if not os.path.exists('../rules/OsRules.xsl'):
        subprocess.Popen(['curl','-soc','../rules/OsRules.xsl','https://github.com/AndroidKitKat/st-checker/releases/download/whyDoINeedThis/OsRules.xsl'])
    return getRulesFromSheet('../rules/OsRules.xsl')


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
    with open('../temp/temp.txt',) as pprofile, open('../temp/line.txt','w+') as liner, open('../temp/itemize.txt','w+') as itemize, open('temp/out.xml','wb') as test:
        for line in pprofile:
            lineNum = lineNum + 1
            for item in rulesheet:
                if item.lower() in line.lower():
                    presentRules.append(item)
                    liner.write(line)
                    itemize.write(item+'\n')
        presentRules = list(set(presentRules))
        missingRules = [x for x in rulesheet if x not in presentRules]
        root = etree.Element('PP_Rules')
        xmlRules = etree.SubElement(root, 'Present_Rules')
        xmlRules.text = str(presentRules)
        xmlMissing = etree.SubElement(root, 'Missing_Rules')
        xmlMissing.text = str(missingRules)
        test.write((etree.tostring(root, pretty_print=True)))