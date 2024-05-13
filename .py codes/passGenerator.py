# Working
import random

strings = 'abcdefghijklmnopqrstuvwxyz@#$*&'
str_len = int(input("enter the range  "))

paswrd = ""
password = ""
for i in range(0, str_len):
    paswrd = random.choice(strings)
    password = password + paswrd
print(password)