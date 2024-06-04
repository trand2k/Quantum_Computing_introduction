import time

def lcg_random(seed, a=1664525, c=1013904223, m=2**32):
    """
    Linear Congruential Generator (LCG) for generating pseudo-random numbers.
    """
    while True:
        seed = (a * seed + c) % m
        yield seed

def generate_random_list(n: int):
    """
    Generates a list of 2n unique random positive integers, each using a maximum of n bits,
    and another random positive integer k using n bits.
    """
    max_value = 2 ** n - 1  # Maximum value using n bits
    unique_numbers = set()
    seed = int(time.time() * 1000) % 2**32
    lcg = lcg_random(seed)
    
    # Generate 2n unique numbers
    while len(unique_numbers) < 2 * n:
        random_number = next(lcg) % max_value + 1
        unique_numbers.add(random_number)
    
    list_n = list(unique_numbers)
    
    # Generate a random k
    k = next(lcg) % max_value + 1
    
    return k, list_n

def search_k(k: int, list_n: list[int]):
    """
    Checks if k exists in the list_n.
    Returns (True, n_steps) if k exists, and (False, n_steps) otherwise,
    where n_steps is the number of steps needed.
    """
    n_steps = 0
    for num in list_n:
        n_steps += 1
        if num == k:
            return True, n_steps
    return False, n_steps

def less_than_k(k: int, list_n: list[int]):
    """
    Finds all integers less than k in the list_n.
    Returns (list_nk, n_steps), where list_nk contains all numbers in list_n that are less than k,
    and n_steps is the number of steps needed.
    """
    list_nk = []
    n_steps = 0
    for num in list_n:
        n_steps += 1
        if num < k:
            list_nk.append(num)
    return list_nk, n_steps

# Example usage
n = 3
k, list_n = generate_random_list(n)
k_exist = search_k(k, list_n)
list_nk = less_than_k(k, list_n)

print(f"Generated k: {k}")
print(f"Generated list: {list_n}")
print(f"Does k exist in the list?: {k_exist}")
print(f"Numbers in the list less than k: {list_nk}")
