import math
import math


def get_primes(max_limit):
    primes = [2]
    candidate = 3
    while candidate < max_limit:
        is_prime = True
        for p in primes:
            if candidate % p == 0:
                is_prime = False
        if is_prime:
            primes.append(candidate)
        candidate += 1
    return primes


def get_divisors(x, primes = []):
    divisors = [1, x]

    if not primes:
        primes = get_primes(x)

    for p in primes:
        if p > math.sqrt(x):
            break
        p_temp = p
        while x % p_temp == 0:
            if p_temp not in divisors:
                divisors.append(p_temp)
                mirror = x/p_temp
                divisors.append(mirror)
            p_temp += p
    divisors.sort()
    return divisors


if __name__ == '__main__':
    primes = get_primes(4000)
    i = 40
    s = i * (i + 1) / 2
    s = 17907120
    divs = get_divisors(s, primes)
    max_divs = len(divs)
    while len(divs) < 100:
        i += 1
        if i % 1000 == 0:
            print i
        s = i * (i + 1) / 2
        divs = get_divisors(s, primes)
        if len(divs) > max_divs:
            max_divs = len(divs)
            print "maxdivs: ", max_divs
    print divs
    print "i: ", i
    print "s: ", s
    print "d: ", len(divs)


