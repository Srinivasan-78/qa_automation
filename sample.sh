#!/bin/bash
filename=$1
while read line; do
# reading each line
./$line
done < $filename
