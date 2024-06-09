
import random

upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_case = upper_case.lower()
numbers = "1234567890"
symbols = "!@#$%^&*()?+-*/\|"

join_all_character = upper_case + lower_case + numbers + symbols

length = int(input("Enter the desired length for your password: "))

password = ''.join(random.sample(join_all_character,length))

print("And your generated password is :" ,password)
