#写xml文件
import openpyxl
import json
import xml.etree.ElementTree as ET
from myXml import prettyXml

if __name__ == "__main__":
    wb = openpyxl.load_workbook("city.xlsx")
    sheet = wb.active
    data = {}

    for row in sheet.rows:
        data[row[0].value] = row[1].value

    strdata = json.dumps(data, indent=2, ensure_ascii=False)
    notes = "\n<--\n\t城市信息\n-->\n"

    rootNode = ET.Element("root")
    cityNode = ET.Element("city")
    cityNode.text = notes + strdata
    rootNode.extend((cityNode,))
    prettyXml(rootNode)

    tree = ET.ElementTree(rootNode)
    tree.write("city.xml", encoding="utf-8")