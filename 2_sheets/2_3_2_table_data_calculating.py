import math
import xlrd
import urllib.request

url = 'https://stepik.org/media/attachments/lesson/245290/trekking2.xlsx'
urllib.request.urlretrieve(url, 'trekking2.xlsx')

wb = xlrd.open_workbook('trekking2.xlsx')
sheet_names = wb.sheet_names()

data_sheet = wb.sheet_by_name(sheet_names[0])
grocery_list = wb.sheet_by_name(sheet_names[1])
DATA_ELEMENTS_COUNT = 38
LIST_ELEMENTS_COUNT = 13

characteristics = data_sheet.row_values(0)[1:]
products = {
    head :
        {   element : tail[j]
            if tail[j] != ''
            else 0
            for j, element in enumerate(characteristics)
        }
    for head, *tail in (data_sheet.row_values(i) for i in range(1, DATA_ELEMENTS_COUNT))
}

products_list = [{'name': grocery_list.row_values(i)[0], 'weight': grocery_list.row_values(i)[1]}
    for i in range(1, LIST_ELEMENTS_COUNT)]
data = {characteristics[j]: 0 for j in range(len(characteristics))}


def add_product(prod):
    name = prod['name']
    weight = prod['weight']
    for char in characteristics:
        data[char] += weight * products[name][char] / 100


for product in products_list : add_product(product)
print(*list(map(math.floor, data.values())))
