# URL = input("Please enter a URL:\n")
URL = "http://www.example.com?p1=10&p2=20&p3=30"
Host = URL.split("//")[1].split('?')[0]

items1 = URL.split("://")
print(items1)
items2 = items1[1].split('?')
print(items2)

host = items2[0]

items3 = items2[1].split('&')
print(items3)

print("Host is " + host)
for i in range(items2[1].count('=')):
    items4 = items3[i].split("=")
    print("Name is " + items4[0] + ", value is " + items4[1])
