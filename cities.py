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

def create_excel(csv_file):
	#Open file in read modus and read line by line
	file_csv = open(csv_file, "r")
	file = file_csv.readlines()
	#create empty lists
	number_reminder = []
	list_with_lists = []
	#create list of lists
	for row in file[1:]:
		item_array = row.split(';')
		list_with_lists.append(item_array)
	#loop through list of lists and create archives
	for item in list_with_lists:
		#remove duplicates
		if item[0] not in number_reminder:
			item[0] = int(item[0])
			#format is now the city id without duplicates
			format = item[0]
			#create the archives with xls writer
			city_string = 'city_number_%s.xlsx' %format
			workbook = xlsxwriter.Workbook(city_string)
			worksheet = workbook.add_worksheet()

			number_reminder.append(item[0])
			#call headers method to and write it on top
			idc = headers("simulados.csv")

			worksheet.write('A1', idc[0][0])
			worksheet.write('B1', idc[0][1])
			worksheet.write('C1', idc[0][2])

			#initialize total_sum and set format to prevent overwriting
			total_sum = 0
			format1 = 2
			#loop through nested list
			for item in list_with_lists:
					if (item[0] == format):
						#convert list to integers
						integer_list = [[int(str(j)) for j in i] for i in list_with_lists]
						#calculate total sum for items
						total_sum = total_sum + int(item[2])
						#write id and sum
						worksheet.write('A%d' %format1, item[0])
						worksheet.write('B%d' %format1, item[1])
						worksheet.write('C%d' %format1, item[2])
						worksheet.write('F5', total_sum)
						#prevent overwrite
						format1 = format1 + 1
						#create a dictionary with tuple and list and group duplicates in list  {(6, 1): [25, 23], (6, 6): [5, 7]}
						dct = defaultdict(list)
						for item in integer_list:
							dct[(item[0], item[1])].extend(item[2:])


						sum_format = 5
						headings_format = 4

						worksheet.write('D%s' %headings_format, 'Id-Prod:')
						worksheet.write('E%s' %headings_format, 'Cantidad')
						worksheet.write('F%s' %headings_format, 'Total-Sum')

						#loop through dictionary
						for key, val in dct.items():
							#if id of city is the first key of dictionary
							if (format == key[0]):
								#if the list only has 1 value turn it into an integer and write it to the file
								if len(val) == 1:
									for i in val:
										int(i)
										sum = i
										worksheet.write('D%s' %sum_format, key[1])
										worksheet.write('E%s' %sum_format, sum)
									#prevent overwriting
									sum_format += 1
								else:
									#if the list has more than one value sum it up and write it to file
									sum = 0
									for item in val:
										sum = sum + item
										worksheet.write('D%s' % sum_format, key[1])
										worksheet.write('E%s' % sum_format, sum)
									sum_format += 1

					else:
						pass
			# close file
			workbook.close()

		else:
			number_reminder.append(item[0])


# Create the CSV file
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

#Extract the headers from file
def headers(csv_file):
	file_csv = open(csv_file, "r")
	file = file_csv.readlines()

	list_with_lists = []

	for row in file[:1]:
		item_array = row.split(';')
		list_with_lists.append(item_array)

	return (list_with_lists)

## Call both methods
def main_method(file):
	create_excel(file)
	create_csv(file)


main_method("simulados.csv")

#helper function
# def sum(file):
# 	file_csv = open(file, "r")
# 	file = file_csv.readlines()
#
# 	list_with_lists = []
#
# 	for row in file[1:]:
# 		item_array = row.split(';')
# 		list_with_lists.append(item_array)
#
# 	integer_list = [[int(str(j)) for j in i] for i in list_with_lists]
#
# 	print(integer_list)
# 	dct = defaultdict(list)
# 	for item in integer_list:
# 		dct[(item[0], item[1])].extend(item[2:])
#
#
# 	print(dct)
#
# 	sum = 0
#
# 	for key, val in dct.items():
# 		if len(val) == 1:
# 			sum = val
# 			print(key, sum)
# 		else:
# 			for item in val:
# 				sum = sum + item
# 			print(key, sum)
#
