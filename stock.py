class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        if isinstance(nshares, int):
            self.shares -= nshares
        else:
            raise Exception("number of shares must be int")

def read_portfolio(filename):
    import csv
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        # print(headers)
        for row in rows:
            record = Stock(row[0], int(row[1]), float(row[2]))
            portfolio.append(record)
    return portfolio

def print_portfolio(portfolio):
    print('%10s %10s %10s' % ('name', 'shares', 'price'))
    print('%10s %10s %10s' % ('----------', '----------', '----------'))
    for s in portfolio:
      print('%10s %10d %10.2f' % (s.name, s.shares, s.price))