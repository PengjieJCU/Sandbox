name = input ("enter user name")

while len(name) <= 0:
    print("name is blank, enter again")
    name = input("enter name")
print(name [::2])

for i in range(0,len(name),2):
    print(name(i),odd="")
