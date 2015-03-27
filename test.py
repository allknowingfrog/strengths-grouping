#!/usr/bin/python3
import csv

teamsCount = 2

scores = {}
with open('strengths.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        scores[row['Name']] = {}
        scores[row['Name']]['strengths'] = {}
        scores[row['Name']]['strengths']['a'] = int(row['A'])
        scores[row['Name']]['strengths']['b'] = int(row['B'])
        scores[row['Name']]['strengths']['c'] = int(row['C'])

for user in scores:
    total = 0
    strengths = scores[user]['strengths']
    for s in strengths:
        total += strengths[s]
    scores[user]['total'] = total

for user in scores:
    print(user, scores[user]['total'])

teams = []
for i in range(0, teamsCount):
    teams.append([])

