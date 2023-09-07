class Stock:
    types = (str, int, float)
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
    
    @classmethod
    def from_row(cls, row):
        values = [func(val) for func, val in zip(cls.types, row)]
        return cls(*values)

    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        if isinstance(nshares, int):
            self.shares -= nshares
        else:
            raise Exception("number of shares must be int")

from decimal import Decimal
class DStock(Stock):
    types = (str, int, Decimal)

def read_portfolio(filename, cls):
    import csv
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        # print(headers)
        for row in rows:
            # Original
            # record = Stock(row[0], int(row[1]), float(row[2]))

            # Improved
            record = cls.from_row(row)
            portfolio.append(record)
    return portfolio

def print_portfolio(portfolio):
    print('%10s %10s %10s' % ('name', 'shares', 'price'))
    print('%10s %10s %10s' % ('----------', '----------', '----------'))
    for s in portfolio:
      print('%10s %10d %10.2f' % (s.name, s.shares, s.price))