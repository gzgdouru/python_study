#写xml文件
import openpyxl
import json
import xml.etree.ElementTree as ET
from myXml import prettyXml

if __name__ == "__main__":
    wb = openpyxl.load_workbook("numbers.xlsx")
    sheet = wb.active
    data = []

    for row in sheet.rows:
        tmpList = []
        [tmpList.append(cell.value) for cell in row]
        data.append(tmpList)

    strdata = json.dumps(data, indent=2, ensure_ascii=False)
    notes = "\n<--\n\t数字信息\n-->\n"

    rootNode = ET.Element("root")
    numbersNode = ET.Element("numbers")
    numbersNode.text = notes + strdata
    rootNode.extend((numbersNode,))
    prettyXml(rootNode)

    tree = ET.ElementTree(rootNode)
    tree.write("numbers.xml", encoding="utf-8")
