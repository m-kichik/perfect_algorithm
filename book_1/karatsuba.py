import math


def preproc_karatsuba(n: int, m:int):
    n = [int(d) for d in str(n)]
    m = [int(d) for d in str(m)]
    req_len = 2 ** math.ceil(math.log2(max(len(n), len(m))))
    n_pref = [0 for _ in range(req_len - len(n))]
    m_pref = [0 for _ in range(req_len - len(m))]
    n = n_pref + n
    m = m_pref + m

    return n, m


def rec_karatsuba(n: list, m: list):
    if len(n) == len(m) == 1:
        return n[0] * m[0]
    else:
        mid_ind = int(len(n) / 2)
        a, b = n[:mid_ind], n[mid_ind:]
        c, d = m[:mid_ind], m[mid_ind:]

        n_a = int(''.join(map(str, a)))
        n_b = int(''.join(map(str, b)))
        n_c = int(''.join(map(str, c)))
        n_d = int(''.join(map(str, d)))

        n_p = n_a + n_b
        n_q = n_c + n_d

        p, q = preproc_karatsuba(n_p, n_q)

        ac = rec_karatsuba(a, c)
        bd = rec_karatsuba(b, d)
        pq = rec_karatsuba(p, q)

        adbc = pq - ac - bd

        return int(10 ** len(n) * ac + 10 ** (len(n) / 2) * adbc + bd)


def karatsuba(n: int, m: int) -> int:
    n, m = preproc_karatsuba(n, m)

    return rec_karatsuba(n, m)


def main():
    n = 1230942
    m = 984321
    nm = karatsuba(n, m)
    print(n * m)
    print(nm)


if __name__ == '__main__':
    main()
