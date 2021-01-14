import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "123456789"
symbol = ",./[]{}()_-*#$%@&"

secure = lower + upper + number + symbol
length = 16
password = "".join(random.sample(secure, length))
print("Secure password: " + password)
