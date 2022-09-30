import numpy as np
import time
from matplotlib import pyplot as plt
import random
# random.seed(42)
import sys
sys.setrecursionlimit(2500)


def choose_pivot_first(x: list, l: int, r: int):
    return l


def choose_pivot_last(x: list, l: int, r: int):
    return r - 1


def choose_pivot_random(x: list, l: int, r: int):
    return random.randint(l, r - 1)


def swap(x_1, x_2):
    return x_2, x_1


def choose_pivot_median(x: list, l: int, r: int):
    if r - l == 2:
        return l if x[l] < x[r - 1] else r - 1
    else:
        x_1, x_2, x_3 = (x[l], l), (x[int((r - l) / 2)], int((r - l) / 2)), (x[r - 1], r - 1)
        if x_1[0] >= x_2[0]:
            x_1, x_2 = swap(x_1, x_2)
        if x_1[0] >= x_3[0]:
            x1, x_3 = swap(x_1, x_3)
        if x_2[0] >= x_3[0]:
            x_2, x_3 = swap(x_2, x_3)
        return x_2[1]


def partition(x: list, l: int, r: int):
    p = x[l]
    i = l + 1
    for j in range(l + 1, r, 1):
        if x[j] < p:
            x[j], x[i] = swap(x[j], x[i])
            i += 1
    x[l], x[i - 1] = swap(x[l], x[i - 1])
    return i - 1


def rec_quick_sort(x: list, l: int, r: int, choose_pivot):
    if l >= r:
        return
    i = choose_pivot(x, l, r)
    x[l], x[i] = swap(x[l], x[i])
    j = partition(x, l, r)

    rec_quick_sort(x, l, j, choose_pivot)
    rec_quick_sort(x, j + 1, r, choose_pivot)


def quick_sort(x: list, choose_pivot):
    rec_quick_sort(x, 0, len(x), choose_pivot)


def main():
    lens = np.arange(50, 1550, 50)
    keys = ['first', 'last', 'random', 'median']
    pivots = {
        'first': choose_pivot_first,
        'last': choose_pivot_last,
        'random': choose_pivot_random,
        'median': choose_pivot_median
    }
    times = {
        'first': [],
        'last': [],
        'random': [],
        'median': []
    }

    for l in lens:
        print(f'work with {int(l)}-element list...')
        x = np.arange(l)
        random.shuffle(x)
        for k in keys:
            y = x.copy()
            start_time = time.time()
            quick_sort(y, choose_pivot=pivots[k])
            exec_time = time.time() - start_time
            times[k].append(exec_time)

    plt.title('time dependence for different pivots [shuffled arrays]')
    plt.xlabel('n elements')
    plt.ylabel('time, s')
    plt.xscale('log')
    for k in keys:
        plt.plot(lens, times[k], label=k)
        plt.legend()
    plt.savefig('qs_vis_shuffled')


if __name__ == '__main__':
    main()
