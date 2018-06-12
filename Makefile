default:
	cd ~/Projects/st-checker && xsltproc -o OsRules.xsl xsl/RuleGenerator.xsl ~/Documents/operatingsystem/input/operatingsystem.xml && xsltproc OsRules.xsl examples/GoodExample.xml
	python3 python/get-input.py ~/Projects/st-checker/input/st_vid10851-st.pdf
#	~/saxon-wrapper/bin/saxon-xslt GoodExample.xml OsRules.xsl
	python3 python/check-st.py ~/Documents/operatingsystem/input/operatingsystem.xml output/rippedpdf.txt
	python3 python/pp-to-worksheet.py ~/Documents/operatingsystem/input/operatingsystem.xml > /tmp/Abc.html && firefox /tmp/Abc.html 
	