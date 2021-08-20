import os
import sys


def folder_files(folder_name, folder_del=''):
    result = ''
    
    for root, folders, files in os.walk(folder_name):
      print(root,folders,files)
      for name in files:
          result += folder_del + '--' + name + '\n'
          # print(result)
      return result
      for folder in folders:
          folder_del += '--'
          return folder_files(folder, folder_del)
      
          
    """
    filenames = os.listdir(folder_name)
    # print(type(filenames))
    result = '--' + '\n--'.join(filenames)
    for filename in filenames:
    
        for root, folders, files in (os.walk(filename)):
          if folders:
            folder_name = folders
            folder_files(folder_name)
    
        try:
          extract = os.listdir(filename)
          folder_files(filename)
        except:
          continue
    """
    return result

def main():
    folder_name = sys.argv[1]
    print(folder_name)
    get_details = folder_files(folder_name)
    print(get_details)

if __name__ == '__main__':
  main()
    

    
    
