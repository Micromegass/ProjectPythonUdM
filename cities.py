import xlsxwriter
from collections import defaultdict

"""""
pseudocode
1. Open csv file
2. Read line by line and split by ; 
3. Create a list/dictionary? Maybe List dictionary with tuples [ {1 : (productId, Anzahl)} ]
4. Write a method for the headers
5. Do the same with csv file 
6. create a sum for every cities products
"""


#Extract the headers from file
def headers(csv_file):
	file_csv = open(csv_file, "r")
	file = file_csv.readlines()

	list_with_lists = []

	for row in file[:1]:
		item_array = row.split(';')
		list_with_lists.append(item_array)

	return (list_with_lists)


def create_csv(csv_file):
	#Create list with lists
	file_csv = open(csv_file, "r")
	file = file_csv.readlines()

	number_reminder = []
	list_with_lists = []

	for row in file:
		item_array = row.split(';')
		list_with_lists.append(item_array)

	#loop through nested list without
	for item in list_with_lists[1:]:
		if item[0] not in number_reminder:
			format = item[0]
			city_string = 'city_number_%s.csv' %format
			city_file = open(city_string,"a")
			number_reminder.append(item[0])

			#write headers
			idc = headers("simulados.csv")

			city_file.write(idc[0][0])
			city_file.write(idc[0][1])
			city_file.write(idc[0][2])

			#Wirte the info to the file
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


def create_excel(csv_file):
	file_csv = open(csv_file, "r")
	file = file_csv.readlines()

	number_reminder = []
	list_with_lists = []

	for row in file:
		item_array = row.split(';')
		list_with_lists.append(item_array)

	# loop through nested list without
	for item in list_with_lists[1:]:

		if item[0] not in number_reminder:
			number_reminder.append(item[0])

			format = item[0]
			city_string = 'city_number_%s.xlsx' %format

			workbook = xlsxwriter.Workbook(city_string)
			worksheet = workbook.add_worksheet()
			worksheet.write('G1', 'IdProducto')
			worksheet.write('H1', 'Cantidad')

			#sum start
			integer_list = [[int(str(j)) for j in i] for i in list_with_lists[1:]]
			dct = defaultdict(list)
			for item in integer_list:
				dct[(item[0], item[1])].extend(item[2:])

			sum_format = 0
			formatx = 2

			#calculate sum
			for key, val in dct.items():
				# if the list only has 1 value turn it into an integer and write it to the file
				if len(val) == 1:
					sum = 0
					for i in val:
						int(i)
						sum = i
					if city_string == ("city_number_%s.xlsx" %key[0]) :
						worksheet.write('F%d' %formatx, key[0] )
						worksheet.write('G%d' %formatx, key[1] )
						worksheet.write('H%d' %formatx, sum)

						# prevent overwriting
						sum_format += 1
						formatx += 1

				else:
					# if the list has more than one value sum it up and write it to file
					sum = 0
					for item in val:
						sum = sum + item

					if city_string == ("city_number_%s.xlsx" %key[0]):
						worksheet.write('F%d' %formatx, key[0])
						worksheet.write('G%d' %formatx, key[1])
						worksheet.write('H%d' %formatx, sum)

						# prevent overwriting
						sum_format += 1
						formatx += 1
						sum_format += 1

			# call headers method to and write it on top
			idc = headers("simulados.csv")

			worksheet.write('A1', idc[0][0])
			worksheet.write('B1', idc[0][1])
			worksheet.write('C1', idc[0][2])

			# Write the info to the file
			format1 = 2
			for item in list_with_lists[1:]:
				if item[0] == format:
					worksheet.write('A%d' %format1, item[0])
					worksheet.write('B%d' %format1, item[1])
					worksheet.write('C%d' %format1, item[2])
					#prevent overwrite
					format1 = format1 + 1
				else:
					pass

			workbook.close()
		else:
			number_reminder.append(item[0])


def sum(csv_file):
	file_csv = open(csv_file, "r")
	file = file_csv.readlines()

	list_with_lists = []

	for row in file:
		item_array = row.split(';')
		list_with_lists.append(item_array)


	integer_list = [[int(str(j)) for j in i] for i in list_with_lists[1:]]

	dct = defaultdict(list)
	for item in integer_list:
		dct[(item[0], item[1])].extend(item[2:])

	sum_format = 0

	for key, val in dct.items():
		# if the list only has 1 value turn it into an integer and write it to the file
		if len(val) == 1:
			for i in val:
				int(i)
				sum = i
			# prevent overwriting
			sum_format += 1


		else:
			# if the list has more than one value sum it up and write it to file
			sum = 0
			for item in val:
				sum = sum + item
			sum_format += 1


## Call both methods
def main_method(file):
	create_excel(file)
	create_csv(file)


if __name__ == "__main__":
	main_method('simulados.csv')





