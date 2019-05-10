import xlsxwriter
from collections import defaultdict

"""""
1. Open csv file
2. Read line by line and split by ; 
3. Create a list/dictionary? Maybe List dictionary with tuples [ {1 : (productId, Anzahl)} ]
4. Write a method for the headers
5. Do the same with csv file 
6. create a sum for every cities products
"""

def create_excel(csv_file):
	file_csv = open(csv_file, "r")
	file = file_csv.readlines()

	number_reminder = []
	list_with_lists = []

	for row in file[1:]:
		item_array = row.split(';')
		list_with_lists.append(item_array)

	print(list_with_lists)

	integer_list = [[int(str(j)) for j in i] for i in list_with_lists]
	print(integer_list)


	for item in list_with_lists:
		if item[0] not in number_reminder:
			item[0] = int(item[0])
			format = item[0]
			city_string = 'city_number_%s.xlsx' %format

			workbook = xlsxwriter.Workbook(city_string)
			worksheet = workbook.add_worksheet()

			number_reminder.append(item[0])

			idc = headers("simulados.csv")

			worksheet.write('A1', idc[0][0])
			worksheet.write('B1', idc[0][1])
			worksheet.write('C1', idc[0][2])

			total_sum = 0
			format1 = 2

			sum_list = []
			for item in list_with_lists:
					sum_list.append(item[0])
					sum_list.append(item[1])
					sum_list.append(item[2])


					if (item[0] == format):

						integer_list = [[int(str(j)) for j in i] for i in list_with_lists]

						total_sum = total_sum + int(item[2])

						worksheet.write('A%d' %format1, item[0])
						worksheet.write('B%d' %format1, item[1])
						worksheet.write('C%d' %format1, item[2])

						worksheet.write('F5', total_sum)
						format1 = format1 + 1

						dct = defaultdict(list)
						for item in integer_list:
							dct[(item[0], item[1])].extend(item[2:])

						print(dct)

						sum_format = 5
						worksheet.write('D4', 'Id-Prod:')
						worksheet.write('E4', 'Cantidad')
						worksheet.write('F4', 'Total-Sum')

						for key, val in dct.items():
							if format in key and format != key[1]:
								if len(val) == 1:
									for i in val:
										int(i)
										sum = i
										worksheet.write('D%s' %sum_format, key[1])
										worksheet.write('E%s' %sum_format, i)
										worksheet.write('E%s' %sum_format, i)
									sum_format += 1
								else:
									sum = 0
									for item in val:
										sum = sum + item
										worksheet.write('D%s' % sum_format, key[1])
										worksheet.write('E%s' % sum_format, sum)
									sum_format += 1

							else:
								pass
					else:
						pass

			print(sum_list)
			workbook.close()

		else:
			number_reminder.append(item[0])


def create_csv(csv_file):
	file_csv = open(csv_file, "r")
	file = file_csv.readlines()

	number_reminder = []
	list_with_lists = []

	for row in file:
		item_array = row.split(';')
		list_with_lists.append(item_array)

	print(list_with_lists)

	for item in list_with_lists[1:]:

		if item[0] not in number_reminder:
			format = item[0]
			city_string = 'city_number_%s.csv' %format

			city_file = open(city_string,"a")

			number_reminder.append(item[0])

			city_file.write("idciudad;")
			city_file.write("idproducto;")
			city_file.write("cantidad\n")


			for item in list_with_lists[1:]:
				if item[0] == format:
					city_file.write(item[0] + ';')
					city_file.write(item[1] + ';')
					city_file.write(item[2])

				else:
					pass

			city_file.close()
		else:
			number_reminder.append(item[0])


def headers(csv_file):
	file_csv = open(csv_file, "r")
	file = file_csv.readlines()

	list_with_lists = []

	for row in file[:1]:
		item_array = row.split(';')
		list_with_lists.append(item_array)

	return (list_with_lists)



def sum(file):
	file_csv = open(file, "r")
	file = file_csv.readlines()

	list_with_lists = []

	for row in file[1:]:
		item_array = row.split(';')
		list_with_lists.append(item_array)

	integer_list = [[int(str(j)) for j in i] for i in list_with_lists]

	dct = defaultdict(list)
	for item in integer_list:
		dct[(item[0], item[1])].extend(item[2:])


	print(dct)

	sum = 0

	for key, val in dct.items():
		if len(val) == 1:
			sum = val
			print(key, sum)
		else:
			for item in val:
				sum = sum + item
			print(key, sum)



create_excel("testfile.csv")


# print(sum_list)
# create_csv("testfile.csv")
# sum("testfile.csv")
