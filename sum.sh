#! /bin/bash
# sum of numbers in a file
if [ $# -lt 1 ] ; then
  echo Usage: File name
  exit 1
fi
if [ $1 ] ; then
  cat $1 | awk 'BEGIN {sum = 0} {sum=sum+$1} END {print sum}'
fi
