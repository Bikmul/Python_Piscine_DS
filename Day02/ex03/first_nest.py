import sys

class Research:

    def __init__(self, path):
        self.path = path
        self.data = self.file_reader()
        self.calculations = self.Calculations()
        
    def file_reader(self, has_header = True):
        with open(self.path, 'r') as file:
            text = file.read()
        lines = text.split('\n')
        if has_header:
            first_line = lines[0].split(',')
            if len(first_line) != 2:
                raise Exception('Error in first string')
        r_lines = lines[1:]
        if len(r_lines) == 0:
            raise Exception('There is no data')
        for line in r_lines:
            if line != '0,1' and line != '1,0':
                raise ValueError('Error in strings')
        return [[int(x) for x in line.split(',')] for line in r_lines]
    
    class Calculations:
        def counts(self, data):
            x = [x[0] for x in data]
            y = [y[1] for y in data]
            return [sum(x), sum(y)]

        def fractions(self, counts):
            return [(counts[0] / (counts[0] + counts[1])) * 100, (counts[1] / (counts[0] + counts[1])) * 100]
            
if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise Exception('invalid number of arguments')
    else:
        print(Research(sys.argv[1]).file_reader())
        print(Research(sys.argv[1]).calculations.counts(Research(sys.argv[1]).file_reader()))
        print(Research(sys.argv[1]).calculations.fractions(Research(sys.argv[1]).calculations.counts(Research(sys.argv[1]).file_reader())))     