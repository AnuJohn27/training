#! /bin/bash
if [ $# -lt 1 ] ; then
	echo Usage: Directory
	exit 1
else
        find $1 | awk 'END { print NR-1 }'
fi
