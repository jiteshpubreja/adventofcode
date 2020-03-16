from hashlib import md5

iinput = "bgvyzdsv"

i = 0

temp = iinput + str(i)

while md5(temp.encode("ascii")).hexdigest()[:6] != "000000":
    i += 1
    temp = iinput + str(i)

print(i)