from hashlib import md5

iinput = "bgvyzdsv"

i = 0

temp = iinput + str(i)

while md5(temp.encode("ascii")).hexdigest()[:5] != "00000":
    i += 1
    temp = iinput + str(i)

print(i)