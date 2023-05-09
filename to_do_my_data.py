import csv

filename = 'data/charles_town_2022.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Print Headers
    for index, column_headers in enumerate(header_row):
        print(index, column_headers)