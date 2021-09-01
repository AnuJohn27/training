#! /bin/bash 
num=$1
if [ $# -lt 1 ] ; then
  echo Usage: Number
  exit 1
fi
r=0
rev=0
while [ $num -gt 0 ] ; do 
    r=`expr $num % 10`
    rev=`expr $rev \* 10 + $r`
    num=`expr $num / 10`
  done
echo $rev

