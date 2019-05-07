import xlsxwriter

"""""
1. Open csv file
2. Read line by line and split by ; 
3. Create a list/dictionary? Maybe List dictionary with tuples [ {1 : (productId, Anzahl)} ]
4. Write a method for the headers

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

			i = 0
			while True:
				try:
					if list_with_lists[i][0] == format:
						worksheet.write('A1', list_with_lists[i][1])
						worksheet.write('A2', list_with_lists[i][2])
						i += 1
					else:
						i += 1


				except IndexError:
					break

			workbook.close()
		else:
			number_reminder.append(item[0])



read_csv_file("testfile.csv")


# listA = [[1,2,3,4,5,6,6], [1,3,5,8,6], [5,6,7,9]]
#
# i = 0
# while True:
#     try:
#         print(listA[i][0])
#         i += 1
#
#     except IndexError:
#         break


#
# workbook = xlsxwriter.Workbook('cities.xlsx')
# worksheet = workbook.add_worksheet()
#
# worksheet.write('A1', 'Hello world')
#
# workbook.close()