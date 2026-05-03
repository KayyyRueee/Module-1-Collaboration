with open("today.txt" , "r") as file:
    today_string = file.read()

print(today_string)

from datetime import datetime

date_object = datetime.strptime(today_string.strip(), "%B %d, %Y")
print(date_object)