#写xml文件
import openpyxl
import xml.etree.ElementTree as ET
from myXml import prettyXml
import json

if __name__ == "__main__":
    wb = openpyxl.load_workbook("student.xlsx")
    sheet = wb.active

    data = {}
    for row in sheet.rows:
        tmpList = []
        [tmpList.append(row[i].value) for i in range(1, len(row))]
        data[row[0].value] = tmpList

    strdata = json.dumps(data, indent=2, ensure_ascii=False)
    notes = "\n <!--\n\t\t学生信息表\n\t\t'id':[名字, 数学, 语文, 英文]\n--> \n"

    rootNode = ET.Element("root")
    studentNode = ET.Element("student")
    studentNode.text = notes + strdata
    rootNode.extend((studentNode,))
    prettyXml(rootNode)

    tree = ET.ElementTree(rootNode)
    tree.write("student.xml", encoding="utf-8", xml_declaration=True, method="xml")

    tree = ET.ElementTree(file="student.xml")
    root = tree.getroot()
    for child in root:
        print(child.tag, child.attrib, child.text)