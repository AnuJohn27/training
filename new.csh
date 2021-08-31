#! /bin/csh -f
set dir=$1
if (-e dir) then
  awk BEGIN {foreach FILE in dir {echo $FILE+'.new' ;} done}
endif 
