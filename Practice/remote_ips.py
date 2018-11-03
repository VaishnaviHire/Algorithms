import json
from pprint import pprint

fin = []
with open('results-20180830-144706.json') as f:
    for row in f:
        a = row.split(':')
        print a[1].split('"')[1]
        fin.append(a[1].split('"')[1])


print fin

