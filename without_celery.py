import requests
import time
from fib import *
def func(urls):
    start = time.time()
    for url in urls:
        resp = requests.get(url)
        print(resp.status_code)
    print("It took", time.time() - start, "seconds")

if __name__ == "__main__":
    start = time.time()
    for i in range(20,34):
        slow_fib(i)
    print("It took", time.time() - start, "seconds")