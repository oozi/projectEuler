import math


def get_primes(max_limit: int) -> list:
    if not isinstance(max_limit, int):
        raise TypeError()
    if max_limit <= 0:
        raise ValueError()
    if max_limit == 1:
        return []
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


def get_divisors(x, primes=None):
    if not isinstance(x, int) and x % 1 != 0:
        raise TypeError()

    if x <= 0:
        raise ValueError()

    divisors = [1]
    if x!= 1:
        divisors.append(x)

    if not primes:
        primes = get_primes(x)

    for p in primes:
        if p > math.sqrt(x):
            break
        p_temp = p
        while p_temp < math.sqrt(x):
            if x % p_temp == 0 and p_temp not in divisors:
                divisors.append(p_temp)
                mirror = int(x/p_temp)
                divisors.append(mirror)
            p_temp += p

    divisors.sort()

    return divisors
