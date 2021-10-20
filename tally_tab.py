import csv

def tally_tab():
    file = open('tally_checking_report.csv' , 'r')
    csvreader = csv.reader(file)
    header = next(csvreader)
    tab_file = open('tab_file.txt', 'w')
    heading = 'Month   Opening    Closing    Credits    Debits' + '\n'
    tab_file.write(heading)
    for row in csvreader:
        tally_tab_separated = "     ".join(row) + '\n'
        tab_file.write(tally_tab_separated)

tally_tab()
