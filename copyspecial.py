#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import subprocess

"""Copy Special exercise
"""

def get_special_paths(direc):
  list_path = []
  filenames = os.listdir(direc)
  for filename in filenames:
    match = re.search(r'__\w+__', filename)
    if match:
      result = match.group()
      list_path.append(os.path.abspath(os.path.join(direc, filename)))
  return list_path

def copy_to(paths, direct):
  if not os.path.exists(direct):
    os.mkdir(direct)
  for path in paths:
    filename = os.path.basename(paths)
    new_path = os.path.join(direct, filename)
    return shutil.copy(path, new_path)

def zip_to(paths, zippath):
  command = 'zip -j ' + zippath + ' '.join(paths)
  print("Command I'm going to do:" + command)
  (status, output) = commands.getstatusoutput(command)
  if status:
    sys.stderr.write(output)
    sys.exit(1)  
  
  
# Write functions and modify main() to call them


def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print("usage: [--todir dir][--tozip zipfile] dir [dir ...]");
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print("error: must specify one or more dirs")
    sys.exit(1)

  # +++your code here+++
  direc = args[0]
  manipulated = get_special_paths(direc)
  special_paths = '\n '.join(manipulated)
  print(special_paths)

  if todir:
    copy_to(special_paths, todir)
  else:
    if tozip:
      zip_to(special_paths, tozip)
    
    
  # Call your functions
  
if __name__ == "__main__":
  main()
