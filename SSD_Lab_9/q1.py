import sys
import re
n = len(sys.argv)
if(n != 2):
    exit(0)
else:
    # print(n)
    arg = sys.argv[1]
    if(arg == ""):
        # print("Input is empty")
        exit(0)
    else:
        i = 0
        first = ""
        while(re.match("[^A-Z]", arg[i])):
            first = first+arg[i]
            i = i+1
        arg = arg[i:]
        splittedWords = re.findall('[A-Z][^A-Z]*', arg)
        for i in range(0, len(splittedWords)):
            splittedWords[i] = splittedWords[i].lower()
        x = ' '.join(splittedWords)
        x = first + " "+x
        print(x)
