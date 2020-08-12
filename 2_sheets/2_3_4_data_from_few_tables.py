import zipfile
import xlrd
import urllib.request

url = 'https://stepik.org/media/attachments/lesson/245299/rogaikopyta.zip'
urllib.request.urlretrieve(url, 'data.zip')

zf = zipfile.ZipFile('data.zip')
filenames = zf.namelist()
staff = []
for file in filenames:
    table = zf.read(file)
    current_table_file = open('table.xlsx', 'wb')
    current_table_file.write(table)
    current_table_file.close()
    wb = xlrd.open_workbook('table.xlsx')
    sheet_names = wb.sheet_names()
    sheet = wb.sheet_by_name(sheet_names[0])
    name = sheet.row_values(1)[1]
    salary = sheet.row_values(1)[3]
    staff.append((name, salary))

staff.sort(key = lambda x: x[0])

for person in staff:
    print(person[0], int(person[1]), sep = ' ')
