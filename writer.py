import csv

'''
# And this file just needs a little bit of configuration. This fucntion needs to write all info into .csv file that 
later can be opened in csv file
'''


def export_data(rows, filename):
    with open(filename, "a") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(rows)

