#!/Users/victor.tobi/.pyenv/shims/python

from datetime import datetime

def myfunction(my_user_data):
    age = datetime.now().year - int(my_user_data)
    return age

date = input("Enter the year you were born? ")
user_age = myfunction(date)
print(user_age)