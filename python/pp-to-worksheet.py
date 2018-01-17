#!/usr/bin/env python3

from io import StringIO 
import re
import sys
import xml.dom.minidom
from xml.dom import minidom
from xml.sax.saxutils import escape


def node_to_text(node):
    ret=""
    if node.nodeType == xml.dom.Node.TEXT_NODE:
        ret += escape(node.data)
    elif node.nodeType == xml.dom.Node.ELEMENT_NODE:
        # sys.stderr.write("Tagname is"+ node.tagName)
        if node.tagName == "selectables":
            sels=[]
            contentCtr=0
            ret+="<span class='selectables'>"
            for child in node.childNodes: # Hopefully only seletable
                if child.nodeType == xml.dom.Node.ELEMENT_NODE and child.tagName == "selectable":
                    contents = title_to_form(child)
                    contentCtr+=len(contents)
                    chk = "<input type='checkbox'"
                    if child.getAttribute("exclusive") == "yes":
                        chk += " onclick='chooseMe(this)'"
                    chk +=">"+ contents+"</input>\n"
                    sels.append(chk)
            if contentCtr < 50:
                for sel in sels:
                    ret+= sel
            else:
                ret+="<ul>\n"
                for sel in sels:
                    ret+= "<li>"+sel+"</li>\n"
                ret+="</ul>\n"
            ret+="</span>"
        elif node.tagName == "assignable":
            ret += "<textarea rows='1' placeholder='"
            ret += ' '.join(title_to_form(node).split())
            ret +="'></textarea>"
                
        elif node.tagName == "abbr" or node.tagName == "linkref":
            ret += node.getAttribute("linkend")
        elif node.tagName == "h:strike":
            pass
        elif ":" in node.tagName:
            tag = re.sub(r'.*:', '', node.tagName)
            ret += "<"+tag
            attrs = node.attributes
            for aa in range(0,attrs.length) :
                attr =attrs.item(aa)
                ret+=" " + attr.name + "='" + escape(attr.value) +"'"
            ret += ">"
            ret += title_to_form(node)
            ret += "</"+tag+">"
    return ret

def title_to_form(title):
    ret=""
    for node in title.childNodes:
        ret+=node_to_text(node)
    return ret
            

def descend(root):
    ret=""
    for node in root.childNodes:
        if node.nodeType == xml.dom.Node.ELEMENT_NODE:
            if node.tagName == "section":
                idAttr=node.getAttribute("id")
                if "SFRs" == idAttr or "SARs" == idAttr:
                    ret+="<h2>"+node.getAttribute("title")+"</h2>\n"
            elif node.tagName == "f-component" or node.tagName == "a-component":
                ret+="<h3>"+node.getAttribute("name")+"</h3>\n"
            elif node.tagName == "title":
                ret+="<div data-id='" + node.parentNode.getAttribute('id') + "'>"
                ret+=title_to_form(node)
                ret+="</div>\n"
                
            ret+=descend(node)
    return ret




if len(sys.argv) != 2:
    print("Usage: <check-it.py> <protection-profile>")
    sys.exit(0)

# Parse the PP
root = minidom.parse(sys.argv[1]).documentElement
form =  "<html xmlns:h='http://www.w3.org/1999/xhtml'>\n   <head>"
form += "<meta charset='utf-8'></meta><title>"+root.getAttribute("name")+"</title>"
form += """
       <style type="text/css">
:disabled{
   color : #DDDDDD;
}
       </style>
       <script type='text/javascript'>

function generateReport(){
    report = "<abc/>";
    initiateDownload('Report.xml', report);
}

function initiateDownload(filename, data) {
    var blob = new Blob([data], {type: 'text/xml'});
    if(window.navigator.msSaveOrOpenBlob) {
        window.navigator.msSaveBlob(blob, filename);
    }
    else{
        var elem = window.document.createElement('a');
        elem.href = window.URL.createObjectURL(blob);
        elem.download = filename;        
        document.body.appendChild(elem);
        elem.click();        
        document.body.removeChild(elem);
    }
}

function chooseMe(sel){
   var common = sel.parentNode;
   while( common.tagName != "SPAN" ){
      common = common.parentNode;
   }
   toggleFirstCheckboxExcept(common, sel);
}

function toggleFirstCheckboxExcept(root, exc){
   if (root == exc) return;
   if (root.getAttribute("type") == "checkbox"){
      root.disabled=exc.checked;
      return;
   }
   var children = root.children;
   var aa;
   for (aa=0; aa!=children.length; aa++){
      toggleFirstCheckboxExcept(children[aa], exc);
   }
}

       </script>
   </head>
   <body>
"""

form +=  "      <h1>Worksheet for the " + root.getAttribute("name") + "</h1>"

form += descend(root)
form += """
      <br/>
      <button type="button" onclick="generateReport()">Generate Report</button>

   </body>
</html>
"""

print(form)
