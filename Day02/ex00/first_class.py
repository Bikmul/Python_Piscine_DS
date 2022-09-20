#!/usr/local/bin/pytho3

class Must_read:
    try:
        with open('data.csv', 'r') as file:
            text = file.read()
            print(text)
    except Exception:
        print('no such file at dir')
        
if __name__ == '__main__':
    Must_read()