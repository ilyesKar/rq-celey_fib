from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import os
import time

from rq import Connection, Queue

from fib import slow_fib


def main():
    # Range of Fibonacci numbers to compute
    fib_range = range(20, 34)

    # Kick off the tasks asynchronously
    async_results = {}
    q = Queue()
    for x in fib_range:
        async_results[x] = q.enqueue(slow_fib, x)

    start_time = time.time()



if __name__ == '__main__':
    # Tell RQ what Redis connection to use
    with Connection():
        main()

