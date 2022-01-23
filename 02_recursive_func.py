def recursive_func_sum(n: int):
    if n == 0:
        return 0
    return n + recursive_func_sum(n - 1)


if __name__ == '__main__':
    print(recursive_func_sum(10))