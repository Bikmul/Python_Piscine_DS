#!/usr/local/bin/python3

def data_types():
    a = 1
    b = '1'
    c = 1,1
    d = True
    e = []
    f = {}
    g = ()
    h = set()
    print(list(map(lambda x: f'{type(x).__name__}', [a, b, c, d, e, f, g, h])))

if __name__ == '__main__':
    data_types()