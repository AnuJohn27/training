# Accounting script

# A script to take balance & transaction file names ( including full paths ) 
# generated in test_data.py as command line inputs. It also validates them to 
# check whether they exist, are readable & are not empty. A tally checking report
# is generated which consists of the following fields:- 'Month', 'Opening', 'Closing',
# 'Total Credits', 'Total Debits'. Data for this monthly analyzing report is generated 
# using the specified input files. This data is checked to hold this equation: 
# monthly opening + monthly credits - monthly debits = monthly closing

import sys
import csv
import re
import os
import argparse

def validate():

    """
    Given a balance file & a transaction file as arguments in command-line. They are validated
    in terms of existence, readability & nullability.

    """

    balance_file = sys.argv[1]
    transaction_file = sys.argv[2]

    size1 = os.path.getsize(balance_file)
    size2 = os.path.getsize(transaction_file)

    if os.path.exists(balance_file) and os.access(balance_file, os.R_OK) and size1 != 0:
        print("Balance file exists, is readable & not empty")
    if os.path.exists(transaction_file) and os.access(transaction_file, os.R_OK) and size2 != 0:
        print("Transaction file exists, is readable & not empty") 
    return balance_file, transaction_file 

def tally_check():

    """
    Generates tally checking report file. Monthly openings & closings are generated from
    balance_file. Total credits & debits are generated from transaction_file.
    
    """
    balance_file, transaction_file = validate()

    # Read from balance_file

    file1 = open(balance_file , 'r')
    csvreader1 = csv.reader(file1)
    header = next(csvreader1)
    balance_rows = []
    for row in csvreader1:
        balance_rows.append(row)

    # Read from transaction_file
     
    file = open(transaction_file , 'r')
    csvreader2 = csv.reader(file)
    transaction_rows = []
    for row in csvreader2:
        transaction_rows.append(row)

    # Tally checking report file

    with open('tally_checking_report.csv', mode='w') as csv_file:
        fieldnames = ['Month', 'Opening', 'Closing', 'Total Credits', 'Total Debits']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        opening_amout=balance_rows[0][2]
        for month in range(1,13):
            month_only=str(month).zfill(2)
            total_credits = 0.0
            total_debits = 0.0
            for row in balance_rows:
                if month_only in re.findall(r'2020(\d\d)\d\d', row[0]): # Check if corresponding month number is matching the pattern of month in balance_file
                    closing_amount=row[3]
            for row in transaction_rows:
                if month_only in re.findall(r'2020(\d\d)\d\d', row[0]): # Check if corresponding month number is matching the pattern of month in transaction_file
                    if float(row[2]) > 0: # Check if amount is a credit value
                        total_credits = round(total_credits + float(row[2]),2)
                        # print(total_credits)
                    else:
                        total_debits =  round(total_debits + float(row[2]),2)
                        # print(total_debits)
            writer.writerow({'Month': month, 'Opening': opening_amout, 'Closing': closing_amount, 'Total Credits': total_credits, 'Total Debits': -(total_debits)})
            opening_amout = closing_amount

def validate_tally():

    """
    Check whether monthly total tallies are correct.

    """

    file = open('tally_checking_report.csv' , 'r')
    csvreader = csv.reader(file)
    header = next(csvreader)
    rows = []
    for row in csvreader:
        # rows.append(row)
    # for data in rows:
        lhs = round(float(row[1]) + float(row[3]) - float(row[4]), 2)
        rhs = float(row[2])
        print(lhs, rhs)
        if lhs==rhs: # Check if monthly opening + monthly credits - monthly debits = monthly closing
            print("Validated")
        else:
            print("Error in tally checking report")
            

tally_check()
validate_tally()