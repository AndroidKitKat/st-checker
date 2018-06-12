import lxml.etree

def parseRules(ruleFile):
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