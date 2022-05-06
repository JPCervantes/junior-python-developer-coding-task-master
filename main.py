from docReaders import read_csv, read_json, read_xml
from TSVformatter import TSVformatter, TSVconverter, TSVconverterSortBy
from constants import DATA_PATH


data1 = read_csv(f'{DATA_PATH}csv_data_1.csv')
data2 = read_csv(f'{DATA_PATH}csv_data_2.csv')
data3 = read_json(f'{DATA_PATH}json_data.json')
data4 = read_xml(f'{DATA_PATH}xml_data.xml')

dataSource = [data1, data2, data3, data4]

formatedData = TSVformatter(dataSource)

headers = formatedData.keys()

formatedData = list(zip(*list(formatedData.values())))

TSVconverter(formatedData, headers)
TSVconverterSortBy(formatedData, headers, 'D3')
