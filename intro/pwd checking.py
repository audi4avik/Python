password = "abc123"

for i in range (3):
    j = 2
    pwd = input("Enter the password: ")
    if (pwd == password):
        print("welcome to the python")
    else:
        print("wrong password, chances left", j-i)

print ("chances exhausted")