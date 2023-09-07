import csv
from collections.abc import Sequence


def read_csv_as_dicts(filename, fields):
    arr = []
    with open(filename) as f:
      rows = csv.reader(f)
      headers = next(rows)
        # print(headers)
      for row in rows:
          item = {
            name: func(val) for name, func, val in zip(headers, types, row)
          }
          arr.append(item)
      return arr


# mostly adapted from readrides.py
from collections.abc import Sequence
class DataCollection(Sequence):
    def __init__(self, headers):
        for col_name in headers:
            #  Same as self.col_name = []
            setattr(self, col_name, [])
        self.headers = headers

    def __len__(self):
        # Same as len(self.((self.headers[0])))
        return len(getattr(self, self.headers[0]))

    def __getitem__(self, index):
        if isinstance(index, slice):
            # new_self = self.__class__(self.headers)
            # Same thing ^
            new_self = getattr(self, self.headers)
            for col_name in self.headers:
                setattr(new_self, col_name, getattr(self, col_name)[index])
            return new_self

        data = {col_name:getattr(self, col_name)[index] for col_name in self.headers}
        return data

    def append(self, d):
        for col_name in self.headers:
            getattr(self, col_name).append(d[col_name])

def read_csv_as_columns(filename, types):
    d = {}
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        headers = next(rows)
        data = DataCollection(headers)
        for row in rows:
            record = {name:func(value) for name, func, value in zip(headers, types, row)}
            data.append(record)
        return data