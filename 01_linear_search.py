def linear_search(n: int, v: int):
    list = []
    [list.append(i) for i in range(n + 1)]
    flag: bool = False
    for i in range(len(list)):
        if list[i] == v:
            flag = True
    print(flag)


if __name__ == '__main__':
    linear_search(10, 5)
