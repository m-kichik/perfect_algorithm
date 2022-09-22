import math


def merge_count_split_inv(first_half: list, second_half: list) -> (list, int):
    i, j = 0, 0
    split_inv = 0
    total_len = len(first_half) + len(second_half)
    merged = []

    for _ in range(total_len):
        if len(first_half) == i:
            merged += second_half[j:]
            return merged, split_inv
        if len(second_half) == j:
            merged += first_half[i:]
            return merged, split_inv
        else:
            if first_half[i] < second_half[j]:
                merged.append(first_half[i])
                i += 1
            else:
                merged.append(second_half[j])
                j += 1
                split_inv += int(len(first_half) - i)

    return merged, split_inv


def req_count_inv(l: list) -> (list, int):
    if len(l) <= 1:
        return l, 0
    else:
        mid = int(len(l) / 2)
        sorted_first_half, left_inv = req_count_inv(l[:mid])
        sorted_second_half, right_inv = req_count_inv(l[mid:])
        sorted, split_inv = merge_count_split_inv(sorted_first_half, sorted_second_half)

        return sorted, left_inv + right_inv + split_inv


def count_inv(l: list) -> (list, int):
    sorted, inv = req_count_inv(l)

    return sorted, inv


def main():
    original = [1, 3, 5, 2, 4, 6]
    sorted = [1, 2, 3, 4, 5, 6, 7, 8]
    inverted = [8, 7, 6, 5, 4, 3, 2, 1]
    problem = [54044, 14108, 79294, 29649, 25260, 60660, 2995, 53777, 49689, 9083]

    sorted, n_inv = count_inv(problem)
    print(n_inv)


if __name__ == '__main__':
    main()
