import sys
import csv
import random,uuid
import argparse
from datetime import date, timedelta


##  workdays of particular year
def workdays(year):

  days = []
  sdate = date(int(year), 1, 2)   
  edate = date(int(year), 12, 30)   

  delta = edate - sdate       

  for i in range(delta.days + 1):
    day = sdate + timedelta(days=i)
    if day.isoweekday() not in (6,7):
      new = str(day).replace('-','')
      days.append(new)

  return days


## transaction file generation
def transaction(year):

  days = workdays(year)
  new_days = []
  num = 150
  while  ( num !=0):
    new_days.append(random.choice(days))
    num -= 1

  
  with open('transaction.csv', mode='w') as csv_file:
    fieldnames = ['Date', 'currency', 'Amount', 'Description', 'Ref#']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    n=250
    writer.writeheader()
    
    while (n != 0):
      writer.writerow({'Date': random.choice(new_days), 'currency': 'INR', 'Amount': round(random.uniform(-100,100),2), 'Description': 'wire out invoice ', 'Ref#':uuid.uuid4().hex[:8]})
      n-=1
      
## balance file generation
def balance(year):
  new_sorted = []
  file = open("transaction.csv")
  csvreader = csv.reader(file)
  header = next(csvreader)
  rows = []
  for row in csvreader:
      rows.append(row)
# print(rows)
  date_sorted=sorted(rows,key=lambda x:x[0])
# print(date_sorted)

  days = workdays(year)
  accounts = ['current','savings','salary','fixed deposite','NRI']
  
  with open('balance.csv', mode='w') as csv_file:
    fieldnames = ['Date', 'Account', 'Opening', 'Closing', 'Ref#']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    opening_amout=0
    closing_amount=0
    for day in days:
      total=0
      for row in date_sorted:
        if day == row[0]:
          total = float(row[2]) +float(total)
      closing_amount = round(total+float(opening_amout),2)

      writer.writerow({'Date': day, 'Account': random.choice(accounts), 'Opening':opening_amout , 'Closing':closing_amount , 'Ref#': uuid.uuid4().hex[:8]})
      opening_amout = closing_amount
      

parser = argparse.ArgumentParser()
parser.add_argument("-y", "--year", type=int, help="Details of the specified year")
args = parser.parse_args()
transaction(args.year)
balance(args.year)