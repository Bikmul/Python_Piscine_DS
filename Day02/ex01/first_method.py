
from lib2to3.pgen2.grammar import opmap_raw


class Research:
    
    def file_reader(self):
            with open('data.csv', 'r') as file:
                return file.read()
        
if __name__ == '__main__':
    try:
        print(Research().file_reader())
    except Exception:
        print("can't read file")  