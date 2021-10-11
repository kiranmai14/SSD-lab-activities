#!/bin/bash
if [ "$#" -ne 3 ]; then
    echo "You must enter exactly 3 command line arguments"
else
[ "$1" -eq "$1" ] 2>/dev/null && echo -n || echo "$1 : not a number" && flag=1 && exit 1
[ "$2" -eq "$2" ] 2>/dev/null && echo -n || echo "$1 : not a number" && flag=1 && exit 1
[ "$3" -eq "$3" ] 2>/dev/null && echo -n || echo "$1 : not a number" && flag=1 && exit 1
[ $flag -eq 0 ] 2>/dev/null && c=$(echo "$1+$2-$3" | bc)
echo $c
fi
