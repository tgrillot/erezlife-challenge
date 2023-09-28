from parse_csv import ParsedCsv
from shape import Shape

def main():
    input_file = input('Enter the path to the CSV file. [test.csv]\n')
    if input_file == '':
        input_file = 'test.csv'
    data = ParsedCsv(input_file)
    for row in data.parsed:
        item = Shape(row)
        print(item.output)

if __name__ == "__main__":
    main()