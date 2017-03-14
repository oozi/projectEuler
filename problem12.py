from problem12lib import *


if __name__ == '__main__':
    primes = get_primes(500)
    i = 40
    s = i * (i + 1) / 2
    divs = get_divisors(s, primes)
    max_divs = len(divs)
    while len(divs) < 500:
        i += 1
        if i % 1000 == 0:
            print(i)
        s = i * (i + 1) / 2
        divs = get_divisors(s, primes)
        if len(divs) > max_divs:
            max_divs = len(divs)
            print("max divs: ", max_divs)
    print(divs)
    print("i: ", i)
    print("s: ", s)
    print("d: ", len(divs))


