#!/usr/bin/python3
import csv

teamsCount = 2

people = {}
with open('strengths.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        people[row['Name']] = {}
        people[row['Name']]['a'] = int(row['A'])
        people[row['Name']]['b'] = int(row['B'])
        people[row['Name']]['c'] = int(row['C'])

outliers = {
    'a': {
        'high': {
            'person': '',
            'score' : 0
        },
        'low': {
            'person': '',
            'score' : 10
        }
    },
    'b': {
        'high': {
            'person': '',
            'score' : 0
        },
        'low': {
            'person': '',
            'score' : 10
        }
    },
    'c': {
        'high': {
            'person': '',
            'score' : 0
        },
        'low': {
            'person': '',
            'score' : 10
        }
    }
}
for p in people:
    for s in people[p]:
        score = people[p][s]
        if score > outliers[s]['high']['score']:
            outliers[s]['high']['score'] = score
            outliers[s]['high']['person'] = p
        elif score < outliers[s]['low']['score']:
            outliers[s]['low']['score'] = score
            outliers[s]['low']['person'] = p

for s in outliers:
    print(
        s, 
        outliers[s]['high']['person'], 
        outliers[s]['high']['score'], 
        outliers[s]['low']['person'], 
        outliers[s]['low']['score']
    )

teams = []
for i in range(0, teamsCount):
    teams.append([])

