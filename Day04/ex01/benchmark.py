import timeit

def main():
    emails = ["john@gmail.com", "james@gmail.com", "alice@yahoo.com", "anna@live.com", "philipp@gmail.com"] * 5
    i = 10000
    print("it is better to use a map")
    print(f'{timeit.timeit(lambda: second_method(emails), number = i)} vs {timeit.timeit(lambda: first_method(emails), number = i)} vs {timeit.timeit(lambda: third_method(emails), number = i)}')

def first_method(emails):
    r = []
    for i in emails:
        if i.endswith("@gmail.com"):
            r.append(i)
    return(r)
        
def second_method(emails):
    return[i for i in emails if i.endswith("@gmail.com")]

def third_method(emails):
    return list(map(lambda x: x if x.endswith("@gmail.com") else None, emails))
    
if __name__ == '__main__':
    main()