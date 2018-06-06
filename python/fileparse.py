import subprocess
try:
    from xml.etree.cElementTree import XML
except ImportError:
    from xml.etree.ElementTree import XML
import zipfile
import re


"""
Module that extract text from MS XML Word document (.docx).
(Inspired by python-docx <https://github.com/mikemaccana/python-docx>)
"""

WORD_NAMESPACE = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
PARA = WORD_NAMESPACE + 'p'
TEXT = WORD_NAMESPACE + 't'



#both in and outs are file paths for all functions

def docxparse(inDocx,outDocx):
    with open(outDocx, "w+") as outDocx:

    #Take the path of a docx file as argument, return the text in unicode.

        document = zipfile.ZipFile(inDocx)
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
        outDocx.write('\n'.join(paragraphs))

#fairly simple pre-built tool that generates txt from PDF
def pdfparse(inPdf,outPdf):
    with open(inPdf) as inPdf, open(outPdf, "w+") as outPdf:
        pdfPath = inPdf.name
        outPdfPath = outPdf.name
        subprocess.Popen(['pdftotext', pdfPath, outPdfPath])