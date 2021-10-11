#!/bin/bash
ls -l| awk '{print (substr($1,7,1)),$NF}' | grep "^x" | awk '{print $nf}'
