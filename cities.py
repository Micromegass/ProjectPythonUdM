import xlsxwriter

"""""
1. Open csv file
2. Read line by line and split by ; 
3. Create a list/dictionary? Maybe List dictionary with tuples [ {1 : (productId, Anzahl)} ]
4. Write a method for the headers
5. Do the same with csv file 
6. create a sum for every cities products
"""

def read_csv_file(csv_file):
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
			item[0] = int(item[0])
			format = item[0]
			city_string = 'city_number_%s.xlsx' %format

			workbook = xlsxwriter.Workbook(city_string)
			worksheet = workbook.add_worksheet()

			number_reminder.append(item[0])

			worksheet.write('A1', "idciudad")
			worksheet.write('B1', "idproducto")
			worksheet.write('C1', "cantidad")

			format1 = 2
			for item in list_with_lists[1:]:
					if item[0] == format:
						worksheet.write('A%d' %format1, item[0])
						worksheet.write('B%d' %format1, item[1])
						worksheet.write('C%d' %format1, item[2])

						format1 = format1 + 1
					else:
						pass

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


create_csv("testfile.csv")

# read_csv_file("testfile.csv")

