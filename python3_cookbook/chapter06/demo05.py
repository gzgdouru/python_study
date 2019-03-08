'''
将字典转换为XML
'''
from lxml import etree


def dict_to_xml(tag, d):
    elem = etree.Element(tag)
    for key, val in d.items():
        child = etree.Element(key)
        child.text = str(val)
        elem.append(child)
    return elem


if __name__ == "__main__":
    s = {'name': 'GOOG', 'shares': 100, 'price': 490.1}
    e = dict_to_xml("stock", s)
    print(etree.tostring(e))

    e.set("_id", "1")
    print(etree.tostring(e))
