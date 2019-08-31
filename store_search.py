import re
import string
from app_dictionary import database

#Can be removed if needed to save data
database.clearAll()
status = True
file = open('sample.txt', 'r').readlines()
for z in file:
    res = re.sub('[' + string.punctuation + ']', '', z).split()
    for i in res:
        database.insert(i)

while(status):
    output = input("Enter word to search: ")
    if len(database.search(output)) != 0:
        print('Success! Word is present in the Database')
    else:
        print('Failure! Word not present')
    option = input("\nEnter 1 to search again, or 2 to exit: ")
    if option == "1":
        status = True
    elif option == "2":
        status = False
    else:
        print("Wrong input! Exiting program...")
        status = False