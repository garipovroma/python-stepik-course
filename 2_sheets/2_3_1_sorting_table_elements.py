import xlrd
import urllib.request

url = 'https://stepik.org/media/attachments/lesson/245290/trekking1.xlsx'
urllib.request.urlretrieve(url, 'trekking1.xlsx')

wb = xlrd.open_workbook('trekking1.xlsx')
sheet_names = wb.sheet_names()
sh = wb.sheet_by_name(sheet_names[0])
DATA_ELEMENTS_COUNT = 38

products = [{'name' : sh.row_values(i)[0], 'characteristics' : sh.row_values(i)[1:]} for i in range(1, DATA_ELEMENTS_COUNT)]
for product in products:
    product_characteristics = product['characteristics']
    product_characteristics = [element if element != '' else 0 for element in product_characteristics]

sorted_by_calorific_value_products = products.copy()
sorted_by_calorific_value_products.sort(key = lambda x: (-x['characteristics'][0], x['name']))
print(*[i['name'] for i in sorted_by_calorific_value_products], sep = '\n')
