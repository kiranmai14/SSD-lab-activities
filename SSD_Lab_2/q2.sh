#!/bin/bash
grep -w "is" $1
wc -l $1 > x1
read x y < x1
let x=x/2
let x=x+5
head -n $x $1|tail -10
awk '{print $3,$5}' $1

