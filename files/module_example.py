# =============== GLOB MODULE ================= #

# import glob
#
# myfiles = glob.glob("files/*.txt")
#
# for filespath in myfiles:
#     with open(filespath ,'r') as files:
#         print(files.read())

# ================ CSV MODULE ================= #

# import csv
# with open("files/weather.csv", 'r') as file:
#     data = list(csv.reader(file))
# print(data)
#
# city = input("Enter a city: ")
# for row in data:
#     if row[0] == city:
#         print(row[1])


# ================ SHUTIL MODULE ================= #

# import shutil
# shutil.make_archive("output", "zip", "files")

# ================ WEBBROWSER MODULE ================= #

import webbrowser

user_term = input("Enter your search: ").replace(" ", "+")
webbrowser.open(f"https://google.com/search?q={user_term}")
