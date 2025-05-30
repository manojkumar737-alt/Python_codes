import sys
number = int(sys.argv[1])
rem = number % 2
if(rem == 0):
    print(number, " is EVEN number")
else:
    print(number, "is ODD number")
#need to pass number in command line example - script.py 6