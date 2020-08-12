import math
import xlrd
import urllib.request

url = 'https://stepik.org/media/attachments/lesson/245290/trekking3.xlsx'
urllib.request.urlretrieve(url, 'trekking3.xlsx')

wb = xlrd.open_workbook('trekking3.xlsx')
sheet_names = wb.sheet_names()

data_sheet = wb.sheet_by_name(sheet_names[0])
grocery_list = wb.sheet_by_name(sheet_names[1])
DATA_ELEMENTS_COUNT = 38
LIST_ELEMENTS_COUNT = 100

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

products_list = [
    {'day': int(grocery_list.row_values(i)[0]),
     'name': grocery_list.row_values(i)[1],
     'weight': grocery_list.row_values(i)[2]
     } for i in range(1, LIST_ELEMENTS_COUNT)]

MAX_DAY_NUMBER = max([int(prod['day']) for prod in products_list])
data = [{characteristics[j]: 0 for j in range(len(characteristics))} for i in range(MAX_DAY_NUMBER)]

def add_product(prod):
    name = prod['name']
    weight = prod['weight']
    day = prod['day'] - 1
    for char in characteristics:
        data[day][char] += weight * products[name][char] / 100

for product in products_list :
    add_product(product)

for day in range(MAX_DAY_NUMBER):
    print(*list(map(math.floor, data[day].values())))
