from __future__ import (absolute_import, division, print_function, unicode_literals)
from celery import task


def slow_fib(n):
    if n <= 1:
        return 1
    else:
        return slow_fib(n - 1) + slow_fib(n - 2)


@task
def slow_fib_c(n):
    if n <= 1:
        return 1
    else:
        return slow_fib(n - 1) + slow_fib(n - 2)


def fib_compute(n,m):
    for i in range(n,m):
        slow_fib_c.delay(i)
