def print_table(records, fields):
    print(" ".join("%10s" % field for field in fields))
    print(("-" * 10 + " ") * len(fields))
    for record in records:
      print(" ".join("%10s" % getattr(record, field) for field in fields))
