import sys 
n = len(sys.argv)
if(n != 2):
    # print("Require atleast two arguments")
    exit(0)
else:
    arg = sys.argv[1]
    if(arg == ""):
        print(True)
    else:
        num = int(arg,2)
        x = str(num)
        reverseNum = x[::-1]
        if(reverseNum == x):
            print(True)
        else:
            print(False)