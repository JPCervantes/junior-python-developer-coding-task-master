import csv
from itertools import chain
from constants import RESULT_PATH


def order_list_by_length(array_list) -> list:
    """This function sort the data by the length of the lists to return
    the new list sorted by the longest element in the list."""

    max_length = len(array_list[0])
    total_length = len(array_list)
    result = []

    for index in range(0, total_length):
        if len(array_list[index]) > max_length:
            result.insert(0, array_list[index])
            max_length = len(array_list[index])
        else:
            result.append(array_list[index])

    return result


def sort_data_by_keys(input_data) -> dict:
    """This function sort the data recived by parameters 
    as a dictionary and returns the date sorted in ascending order 
    by the keys."""

    sorted_keys = []
    sorted_data = {}

    for key in input_data.keys():
        sorted_keys.append(key)
    sorted_keys = sorted(sorted_keys)

    for s_key in sorted_keys:
        sorted_data[s_key] = input_data[s_key]

    return sorted_data


def reorder_dictionary_keys_on_list(disordered_data) -> list:
    """This function takes a list of disordered dictionary data  
    and reorder their keys to an alphanumeric order."""

    ordered_dictionary_list = []

    for list in disordered_data:
        sorted_data = sort_data_by_keys(list)
        ordered_dictionary_list.append(sorted_data)

    return ordered_dictionary_list


def join_data_by_column(ordered_list) -> dict:
    """This function takes an ordered list 
    of dictionaries (key - generator) and joins the generators 
    grouping them by keys using chain method from itertools."""

    data_length = len(ordered_list)
    joined_data = {}

    for i in ordered_list[0].keys():
        joined_data[i] = " "

    for i in range(0, data_length):
        for j_index, j_value in ordered_list[i].items():
            if joined_data[j_index] and joined_data[j_index] != ' ':
                new_gen = chain(joined_data[j_index], j_value)
                joined_data[j_index] = new_gen
            else:
                joined_data[j_index] = j_value

    return joined_data


def format_data_tsv(input_data) -> dict:
    """This function takes a data set of elements in the form
    of an array of dictionaries, on this format: 
    [ { <column_name1> : <generator_object1>, ...}, 
    {...}, { <column_nameA1> : <generator_objectA1>, ...} ] 
    Returns a data formatted to be converted into TSV file."""

    order_data_by_length = order_list_by_length(input_data)
    reordered_data = reorder_dictionary_keys_on_list(order_data_by_length)
    join_data = join_data_by_column(reordered_data)

    return join_data


def convert_data_into_tsv(formated_data, headers, column_sort="D1") -> None:
    """This function converts formatted data into a TSV file 
    and sort it by default by the column D1. You can especified
    another column to sort the data"""

    comlumn_index_sort = list(headers).index(column_sort)
    formated_data.sort(key=lambda x: str(x[comlumn_index_sort]))

    with open(f'{RESULT_PATH}result_sorted_by_{column_sort}.tsv',
              'w', newline='') as output_file:

        tsv_writer = csv.writer(
            output_file,
            delimiter='\t',
            dialect=csv.excel_tab)

        tsv_writer.writerow(headers)
        for value in formated_data:
            tsv_writer.writerow(value)
