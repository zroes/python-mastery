
def portfolio_cost(filename):
  with open(filename, 'r') as file:
    total = 0
    for line in file:
      l = line.split()
      try:
        total += int(l[1]) * float(l[2])
      except ValueError as e:
        print('Couldn\'t parse', line[:-1])
        print('Reason:', e, '\n')
    
  return total

if __name__ == '__main__':
  print(portfolio_cost('Data/portfolio.dat'))