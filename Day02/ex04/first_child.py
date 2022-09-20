import sys
from random import randint

class Research:

    def __init__(self, path):
        self.path = path
        self.calc = self.Calculations(self.file_reader())
        self.anal = self.Analytics(self.file_reader())
        
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
        
        def __init__(self, data):
            self.data = data
        
        def counts(self):
            x = [x[0] for x in self.data]
            y = [y[1] for y in self.data]
            return [sum(x), sum(y)]

        def fractions(self, counts):
            return [(counts[0] / (counts[0] + counts[1])) * 100, (counts[1] / (counts[0] + counts[1])) * 100]
    
    class Analytics(Calculations):
        
 
        
        def predict_random(self, num):
            dct = {0 : [0,1], 1 : [1,0]}
            return [dct[randint(0,1)] for x in range(num)]
    
        def predict_last(self):
            return self.data[-1]
            
            
if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise Exception('invalid number of arguments')
    else:
        print(Research(sys.argv[1]).file_reader())
        print(Research(sys.argv[1]).calc.counts())
        print(Research(sys.argv[1]).calc.fractions(Research(sys.argv[1]).calc.counts()))
        print(Research(sys.argv[1]).anal.predict_random(3))
        print(Research(sys.argv[1]).anal.predict_last())
