try:
	import lxml.etree
except ImportError:
	raise ImportError('this will not work without lxml installed. Please install lxml in a virtual python environment using `pip install lxml')
##needs improvement, but returns a lidt with the os rules
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