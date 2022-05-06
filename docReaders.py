import csv
import enum
import json
from xml.etree import cElementTree


def read_csv(inputData):
    with open(inputData, newline='') as CSVdata:
        CSVdataReader = csv.reader(CSVdata, delimiter=',')

        CSVdataList = []
        for row in CSVdataReader:
            CSVdataList.append(row)
        CSVheaders = CSVdataList[0]
        CSVdataList.remove(CSVheaders)

        CSVbyCol = [*zip(*CSVdataList)]
        result = {}

        for i_index, head in enumerate(CSVheaders):
            result[head] = CSVbyCol[i_index]

        return result


def read_json(indputData):

    with open(indputData) as rawData:
        JSONdata = json.load(rawData)

        JSONdataList = []
        JSONheaders = []

        for row in JSONdata['fields']:
            rowList = []

            for key, value in row.items():
                if key not in JSONheaders:
                    JSONheaders.append(key)
                rowList.append(value)

            JSONdataList.append(rowList)

        JSONbyCol = [*zip(*JSONdataList)]
        result = {}

        for i_index, head in enumerate(JSONheaders):
            result[head] = JSONbyCol[i_index]

        return result


def read_xml(inputData):

    tree = cElementTree.parse(inputData)
    root = tree.getroot()

    XMLlist = []

    for child in root:
        XMLheaders = []
        newRow = []
        for c in child:
            if c.attrib['name'] not in XMLheaders:
                XMLheaders.append(c.attrib['name'])
            newRow.append(c[0].text)
        XMLlist.append(newRow)

    XMLbyCol = [*zip(*XMLlist)]
    result = {}

    for i_index, head in enumerate(XMLheaders):
        result[head] = XMLbyCol[i_index]

    return result
