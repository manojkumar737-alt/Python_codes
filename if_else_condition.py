import sys
age = int(sys.argv[1])
name = sys.argv[2]
if (age >= 18):
    print(name,"valide voter for voting")
elif(age <=18):
    print(f"{name} not valide for voting")
else:
    print("not nter valide parametor for age")
