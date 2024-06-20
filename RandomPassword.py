import random
import string

charValues = string.ascii_letters + string.digits + string.punctuation
password_len = 12

password=''.join([random.choice(charValues) for i in range(password_len)])
print("Password : ", password)