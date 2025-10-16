from base64 import b64decode

flag_1 = b64decode("ZmxhZ3t3NDF0XzF0c19hbGxfYjE=")
print(flag_1)

num = 664813035583918006462745898431981286737635929725

from math import log
print(log(num, 256)) #256 --> 2^8 --> uso il logaritmo per capire il numero di   da 
flag_2 = (num).to_bytes(20, 'big') #--> esce circa 20 --> uso quello

print(flag_1 + flag_2)