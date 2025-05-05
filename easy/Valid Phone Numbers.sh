#!/bin/bash

re='^(\([0-9]{3}\) [0-9]{3}-[0-9]{4}|[0-9]{3}-[0-9]{3}-[0-9]{4})$'


while IFS= read -r line; do
    if [[ $line =~ $re ]]; then
        echo "$line"
    fi
   
done < file.txt
