'''
增量式解析大型XML文件
'''
from lxml import etree


def incremental_parse_xml(file, path):
    path_parts = path.split('/')
    doc = etree.iterparse(file, ('start', 'end'))
    tag_stack = []
    for event, elem in doc:
        if event == "start":
            tag_stack.append(elem.tag)
        elif event == "end":
            if tag_stack == path_parts:
                yield elem
            tag_stack.pop()


if __name__ == "__main__":
    for item in incremental_parse_xml("data.xml", "rss/item/item"):
        print(item)
        for child in item:
            print(child.tag, child.text)
