#!/bin/bash
POSSIBLE_USERS=`cat /etc/passwd | cut -d":" -f 1`
for user in $POSSIBLE_USERS; do
   echo $(find $1 -user $user -exec du -scb {} \; | awk -v var="$user" '{sum+=$1}END{print var, " disk usage, MB: ", sum/1024/1024}')
done
echo '------------------------------------'
echo Used by users not in /etc/passwd: && echo $(find $1 -nouser -exec du -scb {} \; | awk '{sum+=$1}END{print sum/1024/1024}')
