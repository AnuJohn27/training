#! /bin/bash
if [ $# -lt 1 ] ; then
  echo Usage: Directory
  exit 1
fi
if [ $1 ] ; then
  cd $1
  ls | awk '{ print $0".new" ; }'
fi
