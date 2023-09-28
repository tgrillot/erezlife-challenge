import csv

class ParsedCsv:
    def __init__(self, f):
        with open(f, newline='') as file:
            self.data = csv.reader(file,delimiter=',',quotechar='"')
            self.parsed = []
            for row in self.data:
                self.parsed.append(row)