'''
解析和修改XML
'''
from lxml import etree

if __name__ == "__main__":
    doc = etree.parse("pred.xml", parser=etree.XMLParser())
    root = doc.getroot()
    print(root)

    root.remove(root.find("sri"))
    root.remove(root.find("cr"))

    print(root.getchildren().index(root.find("nm")))

    e = etree.Element('spam')
    e.text = "this is a test"
    root.insert(2, e)

    doc.write("newpred.xml", xml_declaration=True)