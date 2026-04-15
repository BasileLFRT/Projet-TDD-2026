import csv

with open('./data/football_european_leagues/match.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')
    for row in reader:
        print(row)