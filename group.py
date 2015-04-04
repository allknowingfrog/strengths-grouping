#!/usr/bin/python3
import csv

teamsCount = 2

def group(source):
    destination = {}
    outliers = {}
    for s in strengths:
        outliers[s] = {
            'high': {
                'group': '',
                'score' : 0
            },
            'low': {
                'group': '',
                'score' : 10
            }
        }

    for g in source:
        group = source[g]
        for p in group:
            people = group[p]
            for s in people:
                score = people[s]
                if score > outliers[s]['high']['score']:
                    outliers[s]['high']['score'] = score
                    outliers[s]['high']['group'] = g
                elif score < outliers[s]['low']['score']:
                    outliers[s]['low']['score'] = score
                    outliers[s]['low']['group'] = g

    for s in outliers:
        outliers[s]['spread'] = outliers[s]['high']['score'] - outliers[s]['low']['score']

people = {}
with open('strengths.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    strengths = reader.fieldnames[1:]
    for row in reader:
        people[row['Name']] = {}
        for s in strengths:
            people[row['Name']][s] = int(row[s])

groups = []
for g in people:
    person = people[g]
    group = {}
    group['people'][g] = person
    group['strengths'] = {}
    s in person:
        group['strengths'][s] = person[s]
    groups.append(group)
