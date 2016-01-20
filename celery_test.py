from celery import Celery
import requests
import time
import sys, os
from fib import *

app = Celery('celery_test', broker='redis://localhost:6379/0')


@app.task
def fetch_url(url):
    resp = requests.get(url)
    print(resp.status_code)


def func(urls):
    for url in urls:
        fetch_url.delay(url)
@task
def slow_fib_c(n):
    if n <= 1:
        return 1
    else:
        return slow_fib(n - 1) + slow_fib(n - 2)


def fib_compute(n,m):
    for i in range(n,m):
        slow_fib_c.delay(i)


if __name__ == "__main__":
    #func(["http://google.com", "https://amazon.in", "https://facebook.com", "https://twitter.com", "https://alexa.com"])
    fib_compute(1,100)
