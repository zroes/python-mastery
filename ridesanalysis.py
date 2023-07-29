import readrides
from collections import Counter
from pprint import pprint

rows = readrides.read_rides_as_dictionaries('Data/ctabus.csv')
ride_set = {r['route'] for r in rows}
# ['route', 'date', 'daytype', 'rides']
rides_on_22_2_2_2011 = [r['rides'] for r in rows if (r['route'] == '22' and r['date'] == '02/02/2011')]

totals = Counter()
for r in rows:
    totals[r['route']] += int(r['rides'])

[r['rides'] for r in rows if r['date'][-4:] == '2001']

totals_2001 = Counter()
for r in rows:
    if r['date'][-4:] == '2001':
        totals_2001[r['route']] += int(r['rides'])

totals_2011 = Counter()
for r in rows:
    if r['date'][-4:] == '2011':
        totals_2011[r['route']] += int(r['rides'])

totals_10_year = totals_2011 - totals_2001


print(len(ride_set))
print(rides_on_22_2_2_2011)
# print(totals)
print(totals_10_year.most_common(5))