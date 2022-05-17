from decimal import Decimal
import time
import sys
from functools import wraps

sys.setrecursionlimit(10**5)

def measure_func(func):
    @wraps(func)
    def _inner(*args):
        start = time.perf_counter()
        res = func(*args)
        end = time.perf_counter()
        print("{}() time = {:.10f}".format(
            func.__name__, Decimal(end-start)))
        return res
    return _inner

@measure_func
def fact(n):
    def _fact(n):
        if n == 0:
            return 1
        return n * _fact(n-1)
    return _fact(n)
print(fact(50))

@measure_func
def fibo(n):
    def _fibo(n):
        if n <= 1:
            return n
        return _fibo(n-1) + _fibo(n - 2)
    return _fibo(n)
print(fibo(33))

@measure_func
def fibo_memo(n):
    memo = [0]*(n+1)
    def _fibo_memo(n):
        if n <= 1:
            return n
        if memo[n] != 0:
            return memo[n]
        memo[n] = _fibo_memo(n-1) + _fibo_memo(n - 2)
        return memo[n]
    return _fibo_memo(n)
print(fibo_memo(33))
