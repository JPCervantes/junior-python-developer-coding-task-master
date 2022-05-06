import csv
from operator import delitem
import constants

VOID_FILL = constants.VOID_FILL


def check_biggest_data(dataList):
    arrayLen = len(dataList)

    if arrayLen == 0:
        return 0

    biggestData = len(dataList[0])

    for index in range(0, arrayLen):
        if len(dataList[index]) > biggestData:
            result = dataList[index]

    return result


def order_list_by_len(arrayList):

    max_len = len(arrayList[0])
    total_len = len(arrayList)
    result = []

    for index in range(0, total_len):
        if len(arrayList[index]) > max_len:
            result.insert(0, arrayList[index])
            max_len = len(arrayList[index])
        else:
            result.append(arrayList[index])
    return result


def sortData(dataList):

    sortedData = {}
    sortedKeys = []

    for key in dataList.keys():
        sortedKeys.append(key)
    sortedKeys = sorted(sortedKeys)

    for sKey in sortedKeys:
        sortedData[sKey] = dataList[sKey]

    return sortedData


def reorder_elements_on_list(disorderedData):
    '''This function takes a list of disorderedData 
    and reorder their keys to an alphanumeric order'''

    orderedElementsList = []
    for list in disorderedData:

        sData = sortData(list)
        orderedElementsList.append(sData)

    return orderedElementsList


def join_data(orderedList):
    '''This function allows to concatenate the data 
    passed like a orderedList of elements'''

    dataLen = len(orderedList)

    finalData = {}
    for i in orderedList[0].keys():
        finalData[i] = " "

    for i in range(0, dataLen):
        for j_index, j_value in orderedList[i].items():
            if finalData[j_index] and finalData[j_index] != ' ':
                finalData[j_index] += j_value
            else:
                finalData[j_index] = j_value
    return finalData


def add_void_data(formatedData, VOID_FILL):
    '''This functions allows to add void data to formated data,
    fills voids with a constant character'''

    longestColumn = 0
    for key, value in formatedData.items():
        cLenght = len(value)
        if cLenght > longestColumn:
            longestColumn = len(value)

    for key, value in formatedData.items():
        cLenght = len(value)
        if cLenght < longestColumn:
            diff = longestColumn - cLenght
            formatedData[key] += (VOID_FILL,)*diff

    return formatedData


def verify_items(unverifiedData):

    verifiedData = {}

    for key, value in unverifiedData.items():
        cList = list(value)
        newList = []
        for item in cList:
            if type(item) == str and item.isnumeric():
                item = int(item)
            newList.append(item)

        verifiedData[key] = tuple(newList)

    return verifiedData


def TSVformatter(initialData):
    '''This function takes a data set of elements in the form
    of an array of dictionaries, on this format: 
    [ { <column_name1> : (<e1>, <e2>, ..., <eN>), ...}
    , {...}, { <column_name1> : (<e1>, ...)} ] 
    Returns a TSV formatted data with headers and no voids inside.'''

    orderedByLenData = order_list_by_len(initialData)

    reOrderedData = reorder_elements_on_list(orderedByLenData)

    joinData = join_data(reOrderedData)

    unverifiedData = add_void_data(joinData, VOID_FILL)

    finalData = verify_items(unverifiedData)

    return finalData


def TSVconverter(TSVformatedData, headers):
    '''This function recive formated data and headers to convert
    the data into a tsv file'''

    with open('results/basic_resultJP.tsv', 'w', newline='') as outputFile:
        tsvwriter = csv.writer(
            outputFile, delimiter='\t', dialect=csv.excel_tab)

        tsvwriter.writerow(headers)
        for value in TSVformatedData:
            tsvwriter.writerow(value)


def TSVconverterSortBy(TSVformatedData, headers, columnSort):
    '''This function converts formatted data into a TSV file and sort it by an specified columnSort.'''

    comlumnIndexSort = list(headers).index(columnSort)
    TSVformatedData.sort(key=lambda x: str(x[comlumnIndexSort]))

    with open(f'results/resultjp_SortedBy{columnSort}.tsv', 'w', newline='') as outputFile:
        tsvwriter = csv.writer(
            outputFile, delimiter='\t', dialect=csv.excel_tab)

        tsvwriter.writerow(headers)
        for value in TSVformatedData:
            tsvwriter.writerow(value)
