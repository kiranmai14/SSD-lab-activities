import sys 
n = len(sys.argv)
if(n != 2):
    # print("Require atleast two arguments")
    exit(0)
else:
    arg = sys.argv[1]
    l = arg.split()
    l.sort(key=lambda x:float(x))
    res = []
    for i in l:
        try:
            res.append(int(i))
        except:
            res.append(float(i))
    print(res)