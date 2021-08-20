import os
import sys


def folder_files(folder_name, folder_del='', root_dir='.'):
    list_dir = os.listdir(root_dir+'/'+folder_name)
    # print(list_dir)
    if folder_name is not None:
      print(folder_del + folder_name)
    for name in list_dir:
        if os.path.isdir(root_dir + '/' + folder_name + '/' + name):
            folder_files(name, folder_del + '--', root_dir + '/' + folder_name)
        elif name is not None:
            print(folder_del + '--' + name)
  # ./basic/solution      
            
    

def main():
    folder_name = sys.argv[1]
    get_details = folder_files(folder_name)

if __name__ == '__main__':
  main()
