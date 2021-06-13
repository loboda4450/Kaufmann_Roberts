cache = {}


def q(n, v, a, t):
    if n < 0 or n > v:
        return 0
    elif n == 0:
        return 1
    elif f'{n}{v}{a}{t}' in cache:
        return cache[f'{n}{v}{a}{t}']
    else:
        value = (sum(a[i] * t[i] * q(n - t[i], v, a, t) for i in range(0, len(a))) / n)
        cache[f'{n}{v}{a}{t}'] = value
        return value


def p(n, v, a, t):
    return q(n, v, a, t) / sum(q(n, v, a, t) for n in range(0, v + 1))


def e(i, v, a, t):
    return sum(p(n, v, a, t) for n in range((v - t[i] + 1), v + 1))


def main():
    m = 3
    v = 100
    a = [15, 4.28571429, 2.72727272]
    c = [2, 7, 11]

    print(f'm: {m}, v: {v}, a: {a}, c: {c}')

    for n in range(0, v + 1):
        print(f'q({n}) = {q(n, v, a, c)}, p({n}) = {p(n, v, a, c)}')

    for i in range(0, m):
        print(f'E{i + 1} = {e(i, v, a, c)}')

    print('\n')


if __name__ == "__main__":
    main()
