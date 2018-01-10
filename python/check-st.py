#!/usr/bin/env python3


import re
import sys
import xml.dom.minidom
from xml.dom import minidom

# Converts a bland string to a regex
def string_to_regex(str):
    # Remove spaces
    ret =  re.sub(r"\s+", '', str)
# Here we add spaces all over
#    ret =  re.sub(r"\s+", r'\s+', str)
    ret =  re.sub(r"\.", r'\.', ret)
    ret =  re.sub(r"\(", r'\(', ret)
    ret =  re.sub(r"\)", r'\)', ret)
    ret =  re.sub(r'\“', r'\“', ret) 
    ret =  re.sub(r'\”', r'\”', ret) 
    return ret
    
def title_to_regex(title):
    ret=""
    for node in title.childNodes:
        if node.nodeType == xml.dom.Node.TEXT_NODE:
            ret= ret + string_to_regex( node.data)
        elif node.nodeType == xml.dom.Node.ELEMENT_NODE:
            # sys.stderr.write("Tagname is"+ node.tagName)
            if node.tagName == "selectables":
                delim="\[(("
                for selectable in node.getElementsByTagName("selectable"):
                    ret+= delim + title_to_regex(selectable) 
                    delim="|"
                ret=ret+")\,?)+\]"
            elif node.tagName == "assignable":
                ret=ret+".*"
            elif node.tagName == "abbr" or node.tagName == "linkref":
                ret=ret+node.getAttribute("linkend")
            elif not node.tagName == "h:strike":
                ret=ret + title_to_regex(node)
    return ret
            

def descend(root):
    ret=[]
    for node in root.childNodes:
        if node.nodeType == xml.dom.Node.ELEMENT_NODE:
            if node.tagName == "title":
                ret.append(title_to_regex(node))
#                ret.append( re.sub(r"(\\s\+)+", "\s+", title_to_regex(node) ) )
            else:
                ret.extend(descend(node))
    return ret

# Returns the text content of this node
def removeMatches(root, regexs):
    ret = ""
    for node in root.childNodes:
        if node.nodeType == xml.dom.Node.TEXT_NODE:
            ret += node.data
        elif node.nodeType == xml.dom.Node.ELEMENT_NODE:
            # Run it against our children
            content = removeMatches(node, regexs)
            for regex in regexs:
                if re.match(regex, re.sub(r"\s+", '', content)):
#                    print("Match "+content)
                    regexs.remove(regex)
            ret = ret + content
    return ret



if len(sys.argv) != 3:
    print("Usage: <check-it.py> <protection-profile> <security-target>")
    sys.exit(0)


dom = minidom.parse(sys.argv[1])
regexes = descend(dom.documentElement)


dom = minidom.parse(sys.argv[2])
print("Regexes size is " + str(len(regexes)))
removeMatches(dom, regexes)
print("Regexes size is " + str(len(regexes)))
for regex in regexes:
    print("regex: " + regex)
