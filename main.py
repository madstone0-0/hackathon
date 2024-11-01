from time import time_ns


def rng(limit):
    return time_ns() % limit
