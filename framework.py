from validation import *
validate()

RECORDS_FILE_NAME = 'bank.dat'
MENU_FILE_NAME = 'menu.cfg'
FIELDS_FILE_NAME = 'fields.cfg'
FIELDS_TYPE_FILE_NAME = 'fields_type.cfg'
domain_keyword = "Account"

def create():
	record = {}
	for field_index in range(0, len(field_names)):
		record[field_names[field_index]] = input("Enter %s: "%field_names[field_index])
		if(fields_type[field_names[field_index]] == "integer"):
			record[field_names[field_index]] = int(record[field_names[field_index]])
		if(fields_type[field_names[field_index]] == "float"):
			record[field_names[field_index]] = float(record[field_names[field_index]])
	records.append(record)
	print("%s created successfully."%domine_keyword)
	save()

def show():
	for record in range(0, len(records)):
		display(record)

def update():
	search = input("Enter %s: "%field_names[0])
	for record_index in range(0, len(records)):
		record = records[record_index]
		if(record[field_names[0]] == search):
			for field_index in range(0, len(field_names)):
				if(fields_type[field_names[field_index]] == "float"):
					record[field_names[field_index]] = float(input("Enter %s to update: "%(field_names[len(field_names) - 1])))
					save()
					break

def delete():
	search = input("Enter %s to update: "%field_names[0])
	for record_index in range(0, len(records)):
		record = records[record_index]
		if(record[field_names[0]] == search):
			del records[record_index]
			save()
			break;

def search():
	search = input("Enter %s to search: "%field_names[0])
	for record_index in range(0, len(records)):
		record = records[record_index]
		if(record[field_names[0]] == search):
			record = record_index
			display(record)

def display(record_index):
	record = records[record_index]
	for field_index in range(0, len(field_names)):
		print("%s:"%field_names[field_index], record[field_names[field_index]])

def save():
	with open(RECORDS_FILE_NAME, 'w') as file:
		file.write("%s" %records)

try:
	with open(RECORDS_FILE_NAME) as file:
		records = eval(file.read())
except IOError:
	print("Error: File does not exist.")
	# message = "Can't find file {0}.".format(RECORDS_FILE_NAME)
	# print(message)
		
with open(FIELDS_FILE_NAME) as file:
	field_names = eval(file.read())

with open(MENU_FILE_NAME) as file:
	menu = file.read()

with open(FIELDS_TYPE_FILE_NAME) as file:
	fields_type = eval(file.read())

while True:
	print(menu)
	functions = [create, show, update, delete, search, exit]
	try:
		choice = int(input())
		functions[choice - 1]()
	except ValueError:
		print("Enter a valid input!")
	except IndexError:
		print("Enter a valid choice!")