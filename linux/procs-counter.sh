#!/usr/bin/bash
for i in `ps -A -o comm= --sort=+comm | uniq`; 
do 
    if (( `ps -C $i --no-headers | wc -l` > 10 )); then 
        echo `hostname` $i `ps -C $i --no-headers | wc -l` ;
    fi
done

