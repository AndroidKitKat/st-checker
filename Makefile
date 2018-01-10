default:
#	cd ~/work/pp/st-checker && xsltproc -o OsRules.xsl xsl/RuleGenerator.xsl ../operatingsystem/input/operatingsystem.xml && xsltproc OsRules.xsl GoodExample.xml
	~/saxon-wrapper/bin/saxon-xslt GoodExample.xml OsRules.xsl
