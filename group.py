#!/usr/bin/python3
import csv

teamsCount = 2

def group(source):
    global strengths

    destination = {}
    outliers = {}
    for s in strengths:
        outliers[s] = {
            'high': {'group': '', 'score' : 0},
            'low': {'group': '', 'score' : 10}
        }

    for g in range(len(source)):
        strengths = source[g]['strengths']
        for s in strengths:
            score = strengths[s]
            if score > outliers[s]['high']['score']:
                outliers[s]['high']['score'] = score
                outliers[s]['high']['group'] = g
            elif score < outliers[s]['low']['score']:
                outliers[s]['low']['score'] = score
                outliers[s]['low']['group'] = g

    max_spread = 0
    max_spread_strength = ''
    for s in outliers:
        spread = outliers[s]['high']['score'] - outliers[s]['low']['score']
        outliers[s]['spread'] = spread
        if spread > max_spread:
            max_spread = spread
            max_spread_strength = s

    print(max_spread, max_spread_strength)
    print(outliers)

people = {}
with open('strengths.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    strengths = reader.fieldnames[1:]
    for row in reader:
        people[row['Name']] = {}
        for s in strengths:
            people[row['Name']][s] = int(row[s])

groups = []
for p in people:
    person = people[p]
    unit = {}
    unit['people'] = {p:person}
    unit['strengths'] = {}
    for s in person:
        unit['strengths'][s] = person[s]
    groups.append(unit)

group(groups)
