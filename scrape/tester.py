import NYT_API

mydata = []
NYT_API.get_data("condition+of+anonymity", mydata)

print(len(mydata))

print("***"*10)

print(mydata[0])

print("==="*20)

for item in mydata:
    print(item["web_url"], item["body"])
    print("__"*10)
