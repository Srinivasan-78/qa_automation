#!/bin/bash
filename=$1
while read line; do
# reading each line
#sed -n $line | bash
./$line
done < $filename
