import json

dict1={"k":"toronto","B":"VanCouver","c":"yemen"}

data1=json.dumps(dict1)

print(type(data1))

with open("output.json","w") as file:

    a=file.write(data1)

with open("output.json","r") as file:   

    b=file.read()

    data2=json.loads(b)

    print(type(data2))

    print(dict1)