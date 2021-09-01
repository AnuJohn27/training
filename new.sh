#! /bin/bash
if [ $# -lt 1 ] ; then
  echo Usage: Directory
  exit 1
fi
if [ $1 ] ; then
  cd $1
  ls | awk -F "." '{print $1".new"}'
fi
