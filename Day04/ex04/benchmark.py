import random
import timeit
from collections import Counter

def generator():
    spisok = [random.randint(0, 100) for i in range(10000000)]
    print(f"my function: {timeit.timeit(lambda: create_dict(spisok), number=1)}")
    print(f"Counter: {timeit.timeit(lambda: top_10(spisok), number=1)}")
    print(f"my top: {timeit.timeit(lambda: Counter(spisok), number=1)}")
    print(f"Counters top: {timeit.timeit(lambda: dict(Counter(spisok).most_common(10)), number=1)}")

def create_dict(lst):
    res = {}
    for i in lst:
        if i in res:
            res[i] += 1
        else:
            res[i] = 1
    return res
    
def top_10(lst):
    return dict(sorted(create_dict(lst).items(), key=lambda item: item[1], reverse=True)[:10])
    
if __name__ == '__main__':
    generator()