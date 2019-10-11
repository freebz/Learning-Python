# XML 분석 도구

# <books>
#     <date>1995~2013</date>
#     <title>Learning Python</title>
#     <title>Programming Python</title>
#     <title>Python Pocket Reference</title>
#     <publisher>O'Reilly Media</publisher>
# </books>

# Learning Python
# Programming Python
# Python Picket Reference


# patternparse.py 파일

import re
text = open('mybooks.xml').read()
found = re.findall('<title>(.*)</title>', text)
for title in found: print(title)


# domparse.py 파일

from xml.dom.minidom import parse, Node
xmltree = parse('mybooks.xml')
for node1 in xmltree.getElementsByTagName('title'):
    for node2 in node1.childNodes:
        if node2.nodeType == Node.TEXT_NODE:
            print(node2.data)


# saxparse.py 파일

import xml.sax.handler

class BookHandler(xml.sax.handler.ContentHandler):
    def __init__(self):
        self.inTitle = False
    def startElement(self, name, attributes):
        if name == 'title':
            self.inTitle = True
    def characters(self, data):
        if self.inTitle:
            print(data)
    def endElement(self, name):
        if name == 'title':
            self.inTitle = False

import xml.sax
parser = xml.sax.make_parser()
handler = BookHandler()
parser.setContentHandler(handler)
parser.parse('mybooks.xml')


# etreeparse.py 파일

from xml.etree.ElementTree import parse
tree = parse('mybooks.xml')
for E in tree.findall('title'):
    print(E.text)


# py -2
# Learning Python
# Programming Python
# Python Pocket Reference

# py -3
# Learning Python
# Programming Python
# Python Pocket Reference


# py -3
from xml.dom.minidom import parse, Node
xmltree = parse('mybooks.xml')
for node in xmltree.getElementsByTagName('title'):
    for node2 in node.childNodes:
        if node2.nodeType == Node.TEXT_NODE:
            node2.data

# 'Learning Python'
# 'Programming Python'
# 'Python Pocket Reference'

# py -2
# ...동일한 코드...

# u'Learning Python'
# u'Programming Python'
# u'Python Pocket Reference'
