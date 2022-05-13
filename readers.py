import csv
import json
from xml.etree import cElementTree


def read_csv(input_data):
    """This function reads CSV files and formats them into dictionary 
    with the headers as keys and data cell values as values"""

    with open(input_data, newline='') as csv_data:
        csv_data_reader = csv.reader(csv_data, delimiter=',')

        csv_data_list = [row for row in csv_data_reader]
        csv_headers = csv_data_list[0]
        csv_data_list.remove(csv_headers)

        csv_matrix_trasposed = [[csv_data_list[row_index][col_index] for row_index in range(
            len(csv_data_list))] for col_index in range(len(csv_headers))]

        csv_dict_gen = {head: (row for row in csv_matrix_trasposed[index])
                        for index, head in enumerate(csv_headers)}

        return csv_dict_gen


def read_json(indput_data) -> dict:
    """This function reads JSON files and formats them into dictionary
    with the same keys for all the diferents values in the JSON."""

    with open(indput_data) as raw_data:
        json_data = json.load(raw_data)

        json_headers = [[key for key, value in row.items()]
                        for row in json_data['fields']]

        json_matrix = [
            [value for key, value in row.items()] for row in json_data['fields']]

        json_matrix_trasposed = [[json_matrix[row_index][col_index] for row_index in range(
            len(json_matrix))] for col_index in range(len(json_matrix[0]))]

        json_dict_gen = {head: (row for row in json_matrix_trasposed[index])
                         for index, head in enumerate(json_headers[0])}

        return json_dict_gen


def read_xml(input_data) -> dict:
    """This function reads xml files and formats them into dictionary 
    with the child atributes as keys and values per object as values"""
    tree = cElementTree.parse(input_data)
    root = tree.getroot()
    xml_list = []

    xml_headers = [[c.attrib['name'] for c in child] for child in root]
    xml_values_list = [[c[0].text for c in child] for child in root]
    xml_dict_gen = {head: (row for row in xml_values_list[0][index])
                    for index, head in enumerate(xml_headers[0])}
    # print("xml_headers: ", xml_headers)
    # print("xml_values_list: ", xml_values_list)
    # print("xml_dict_gen: ", xml_dict_gen)

    # for k, v in xml_dict_gen.items():
    #     print(f"k : {k} -> v: {list(v)}", v)

    # json_dict_gen = {head: (row for row in json_matrix_trasposed[index])
    # for index, head in enumerate(json_headers[0])}

    for child in root:

        xml_headers = []
        new_row = []
        for c in child:

            if c.attrib['name'] not in xml_headers:
                xml_headers.append(c.attrib['name'])

            new_row.append(c[0].text)
        xml_list.append(new_row)

    xml_by_column = [*zip(*xml_list)]
    result = {}

    for i_index, head in enumerate(xml_headers):
        result[head] = xml_by_column[i_index]

    return xml_dict_gen
