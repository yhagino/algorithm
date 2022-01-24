def recursive_sum(n: int):
    if n == 0:
        return 0
    return n + recursive_sum(n - 1)


def recursive_gcd(m: int, n: int):
    if n == 0:
        return m
    return recursive_gcd(n, m % n)


if __name__ == '__main__':
    print(recursive_gcd(105, 15))