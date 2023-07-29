import csv

def read_rides_as_tuples(filename):
    '''
    Read the bus ride data as a list of tuples
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = (route, date, daytype, rides)
            records.append(record)
    return records

def read_rides_as_dictionaries(file):
    records = RideData()
    with open(file) as f:
        rows = csv.reader(f)
        headers = next(rows)
        print(headers)
        for r in rows:
            d = {
                'route': r[0],
                'date': r[1],
                'daytype': r[2],
                'rides': int(r[3])
            }
            records.append(d)
    return records

class Row:
    __slots__ = ('route', 'date', 'daytype', 'rides')
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides
# Row = namedtuple('Row',('route','date','daytype','rides'))

from collections.abc import Sequence

class RideData(Sequence):
    def __init__(self):
        self.routes = []      # Columns
        self.dates = []
        self.daytypes = []
        self.numrides = []

    def __len__(self):
        return len(self.routes)

    def __getitem__(self, index):
        if isinstance(index, slice):
            print(index)
            index = slice(0, index.stop, index.step) if index.start is None else index
            index = slice(index.start, len(self.routes), index.step) if index.stop is None else index
            index = slice(index.start, index.stop, 1) if index.step is None else index
            return [{ 'route': self.routes[i],
                'date': self.dates[i],
                'daytype': self.daytypes[i],
                'rides': self.numrides[i] }
                for i in range(index.start, index.stop, index.step)]
        return { 'route': self.routes[index],
                'date': self.dates[index],
                'daytype': self.daytypes[index],
                'rides': self.numrides[index] }

    def append(self, d):
        self.routes.append(d['route'])
        self.dates.append(d['date'])
        self.daytypes.append(d['daytype'])
        self.numrides.append(d['rides'])


def read_rides_as_class(file):
    records = []
    with open(file) as f:
        rows = csv.reader(f)
        headers = next(f)
        for r in rows:
            item = Row(r[0], r[1], r[2], int(r[3]))
            records.append(item)
    return records


'''
Read the bus ride data into 4 lists, representing columns
'''
def read_rides_as_columns(filename):
    routes = []
    dates = []
    daytypes = []
    numrides = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            routes.append(row[0])
            dates.append(row[1])
            daytypes.append(row[2])
            numrides.append(int(row[3]))
    return dict(routes=routes, dates=dates, daytypes=daytypes, numrides=numrides)


if __name__ == '__main__':
    import tracemalloc
    tracemalloc.start()
    rows = read_rides_as_dictionaries('Data/ctabus.csv')
    print('Memory Use: Current %d, Peak %d' % tracemalloc.get_traced_memory())