import timeit
import sys

def main():
    emails = ["john@gmail.com", "james@gmail.com", "alice@yahoo.com", "anna@live.com", "philipp@gmail.com"] * 5
    i = (int)(sys.argv[2])
    if (sys.argv[1]) == "loop":
        print(f'{timeit.timeit(lambda: loop_method(emails), number = i)}')
    elif (sys.argv[1]) == "comprehension":
        print(f'{timeit.timeit(lambda: comprehension_method(emails), number = i)}')
    elif (sys.argv[1]) == "map":
        print(f'{timeit.timeit(lambda: map_method(emails), number = i)}')
    elif (sys.argv[1]) == "filter":
        print(f'{timeit.timeit(lambda:fiter_method(emails), number = i)}')

def loop_method(emails):
    r = []
    for i in emails:
        if i.endswith("@gmail.com"):
            r.append(i)
    return(r)
        
def comprehension_method(emails):
    return[i for i in emails if i.endswith("@gmail.com")]

def map_method(emails):
    return list(map(lambda x: x if x.endswith("@gmail.com") else None, emails))

def fiter_method(emails):
    return list(filter(lambda i: i.endswith("@gmail.com"), emails))
    
if __name__ == '__main__':
    if len(sys.argv) == 3:
        main()