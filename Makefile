default:
#	cd ~/work/pp/st-checker && xsltproc -o OsRules.xsl xsl/RuleGenerator.xsl ../operatingsystem/input/operatingsystem.xml && xsltproc OsRules.xsl GoodExample.xml
#	~/saxon-wrapper/bin/saxon-xslt GoodExample.xml OsRules.xsl
#	python3 python/check-st.py ~/Documents/operatingsystem/input/operatingsystem.xml examples/GoodExample.xml
#	python3 python/pp-to-worksheet.py ~/Documents/operatingsystem/input/operatingsystem.xml > /tmp/Abc.html && firefox /tmp/Abc.html 
#	python3 python/get-input.py ~/Downloads/operatingsystem.pdf