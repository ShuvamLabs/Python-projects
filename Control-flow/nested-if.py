age = int(input("Enter your age: "))
print("Do you have license?")
s=input()
if age >= 18:
    if s == "Yes" or s == "yes" or s == "YES":
        print("You can drive.")
    else:
        print("Get a driving license first.")
else:
    print("You are underage.")