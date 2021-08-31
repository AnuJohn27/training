#! /bin/csh -f
# reverse.csh
set num=$1
if ($#argv < 1) then
  echo Usage: 'Number'
  exit(1)
endif
set $rev=0
if (-e $num) then
  while ($num > 0) 
    $r = $num/10
    $rev = ($rev*10)+$r
    $num = $num%10
echo $rev
else
  echo Please enter a number. 
endif  
