import random


def linear_search(n: int, v: int):
    list = []
    [list.append(i) for i in range(n + 1)]
    flag: bool = False
    for i in list:
        if list[i] == v:
            flag = True
    return flag


def linear_search_min(n: int):
    list = [random.randint(1, 100) for i in range(n)]
    print(list)
    min_val = 100
    for i in list:
        if i < min_val:
            min_val = i
    return min_val


if __name__ == '__main__':
    linear_search(10, 11)
