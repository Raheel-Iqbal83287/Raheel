#Make a Marks Sheet.

phy = int(input("Enter Physics marks : "))

mat = int(input("Enter Mathematics marks : "))

che = int(input("Enter Chemistry marks : "))

bio = int(input("Enter Biology marks : "))

eng = int(input("Enter English marks : "))

tot = phy + mat + che + bio + eng

per = int(tot / 500 * 100)

print(f"\nPercentage : {per}")
print(f"\nTotal Marks : {tot}")


if per>=80:
    #print(f"\nPercentage : {per}")
    print("Grade : A+")
elif per>=70 and per<=79:
    #print(f"\nPercentage : {per}")
    print("Grade : A")
elif per>=60 and per<=69:
    #print(f"\nPercentage : {per}")
    print("Grade : B")
elif per>=50 and per<=59:
    #print(f"\nPercentage : {per}")
    print("Grade : C")
else:
    #print(f"\nPercentage : {per}")
    print("Fail")    

