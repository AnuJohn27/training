import requests
import json
import csv

def get_address(listt):
    string = ''
    for l in listt:
        string = string + str(l) + ',\n'
    return string

def main():
    header = []
    d = {}
    with requests.get('https://fakerapi.it/api/v1/persons') as url:
      contents = url.json()
    data_part = contents.get('data')
    header = list(data_part[0].keys())
    data_list = []
    for data in data_part:
        listt = list(data['address'].values())
        address = get_address(listt)
        data['address'] = address
        data_list.append(data)
    with open('person_details1.csv', 'w', encoding='UTF8', newline='') as f:
      writer = csv.DictWriter(f, fieldnames=header)
      writer.writeheader()
      writer.writerows(data_list)

      
if __name__ == '__main__':
  main()

    
