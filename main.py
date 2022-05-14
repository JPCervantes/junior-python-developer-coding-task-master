from readers import read_csv, read_json, read_xml
from tsv_formatter import format_data_tsv, convert_data_into_tsv
from itertools import zip_longest
from constants import DATA_PATH


data1 = read_csv(f'{DATA_PATH}csv_data_1.csv')
data2 = read_csv(f'{DATA_PATH}csv_data_2.csv')
data3 = read_json(f'{DATA_PATH}json_data.json')
data4 = read_xml(f'{DATA_PATH}xml_data.xml')

data_inputs = [data1, data2, data3, data4]
formated_data = format_data_tsv(data_inputs)
headers = formated_data.keys()
formated_data = list(zip_longest(*list(formated_data.values())))

convert_data_into_tsv(formated_data, headers, "M9")
