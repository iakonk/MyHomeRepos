# Redhat about memory usage: https://goo.gl/BCRZld 
# Existing checks do a lot of calculations, or use perl module, that is not installed,
# Or calculate memory usage in a wrong way (do not take into account buffers/cached)
# Axample: https://exchange.nagios.org/directory/Plugins/System-Metrics/Memory/check_mem-2Esh/details
#!/bin/bash

USAGE="`basename $0` [-w|--warning]<percent free> [-c|--critical]<percent free>"
# print usage
if [[ $# -lt 4 ]]
then
    echo ""
    echo "Wrong Syntax: `basename $0` $*"
    echo ""
    echo "Usage: $USAGE"
    echo ""
    exit 0
fi

# read input
while [[ $# -gt 0 ]]
  do
        case "$1" in
               -w|--warning)
               shift
               warning=$1
        ;;
               -c|--critical)
               shift
               critical=$1
        ;;
        esac
        shift
  done

memory_free=`free -m | awk '/cache\:/{print $4}'`
memory_total=`free -m | awk '/Mem\:/{print $2}'`
memory_used=`free -m | awk '/cache\:/{print $3}'`
percent_used=$(( $memory_used*100/$memory_total ))
percent_free=$(( $memory_free*100/$memory_total ))
physical_memused_by_process=`top -b -n1 | awk '{print int($6/1024), $1, $12}' | sort -n | egrep -v "Mem:|Swap:" | tail -5`

if [ "$percent_used" -gt "$warning" ] && [ "$percent_used" -lt  "$critical" ] ; then
    string=WARNING
    exit_code=1
fi

if [ "$percent_used" -lt "$warning" ]; then
    string=OK
    exit_code=0
fi

if [ "$percent_used" -gt "$warning" ] && [ "$percent_used" -gt  "$critical" ] ; then
    string=CRITICAL
    exit_code=2
fi
OUTPUT="; Top 5 RAM consumers(mem MB, pid, pname): "   ;
for word in $physical_memused_by_process; do
    i=`expr $i + 1`
    j=`expr $j + 1`
    if [[ $i -eq 3 ]]; then
        i=0;
         if [ $j -eq 15 ]; then
          OUTPUT="$OUTPUT `echo $word`"  ;
         else
          OUTPUT="$OUTPUT `echo $word, `" ;
         fi
    else
        if [ $(($i%3)) -eq 1 ]; then
         OUTPUT="$OUTPUT `echo $word`" ;
        else
         OUTPUT="$OUTPUT `echo $word`" ;
        fi
    fi
done

echo "$string: memory used $memory_used MB($percent_used%) out of $memory_total MB, free $memory_free MB($percent_free%) $OUTPUT|Memory usage=$memory_used$
exit $exit_code
