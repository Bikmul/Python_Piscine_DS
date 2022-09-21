import timeit

def main():
    emails = ["john@gmail.com", "james@gmail.com", "alice@yahoo.com", "anna@live.com", "philipp@gmail.com"] * 5
    print("it is better to use a list comprehension")
    print(f'{timeit.timeit(lambda: second_method(emails), number = 9000000)} vs  {timeit.timeit(lambda: first_method(emails), number = 9000000)}')

def first_method(emails):
    r = []
    for i in emails:
        if i.endswith("@gmail.com"):
            r.append(i)
    return(r)
        
def second_method(emails):
    return[i for i in emails if i.endswith("@gmail.com")]
    
if __name__ == '__main__':
    main()
