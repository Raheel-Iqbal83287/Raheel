#Assignment 2

country = input("Enter your country : ")

if(country == "Pakistan"):
    age = int(input("Enter your age : "))
    if(age >= 18):
        print("Congratulations! You can cast vote")
    else:
        print("You cannot vote right now. Please come to cast vote after " + str(int(18)-age) + " years.")
else:
    print("You are not Pakistani! you cannot cast vote.")

