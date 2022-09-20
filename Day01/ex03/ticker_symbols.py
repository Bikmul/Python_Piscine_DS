#!/usr/local/bin/python3

from curses import keyname
import sys

def ticker_symbols(name):
    COMPANIES = {
        'Apple': 'AAPL',
        'Microsoft': 'MSFT',
        'Netflix': 'NFLX',
        'Tesla': 'TSLA',
        'Nokia': 'NOK'
    }
    STOCKS = {
        'AAPL': 287.73,
        'MSFT': 173.79,
        'NFLX': 416.90,
        'TSLA': 724.88,
        'NOK': 3.37
    }
    if name in COMPANIES.values():
        for key in COMPANIES.items():
            if key[1] == name:
                print(key[0], STOCKS[name])
    else:
        print('Unknown ticker')

if __name__ == '__main__':
    if len(sys.argv) == 2:
        ticker_symbols(sys.argv[1].upper())