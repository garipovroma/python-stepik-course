import xlrd
import urllib.request
import statistics

url = 'https://stepik.org/media/attachments/lesson/245267/salaries.xlsx'
urllib.request.urlretrieve(url, 'salaries.xlsx')

wb = xlrd.open_workbook('salaries.xlsx')
sheet_names = wb.sheet_names()
sh = wb.sheet_by_name(sheet_names[0])
DATA_ELEMENTS_COUNT = 9
PROFESSIONS_COUNT = 8

cities = [(sh.row_values(i)[0], sh.row_values(i)[1:]) for i in range(1, DATA_ELEMENTS_COUNT)]
sorted_by_median_value_cities = list(cities)
sorted_by_median_value_cities.sort(key = lambda x: statistics.median(x[1]), reverse=True)

professions = [(sh.col_values(i)[0], sh.col_values(i)[1:]) for i in range(1, PROFESSIONS_COUNT)]
sorted_by_average_value_professions = list(professions)
sorted_by_average_value_professions.sort(key = lambda x: statistics.mean(x[1]), reverse=True)

print(sorted_by_median_value_cities[0][0], sorted_by_average_value_professions[0][0])
