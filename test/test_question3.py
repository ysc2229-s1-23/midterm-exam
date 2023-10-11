from solutions.question3 import find_second_next_letter  # Assuming you named the function like this

from random import choice, seed
from string import ascii_lowercase
from time import time

def test_find_second_next_letter():
    assert find_second_next_letter(['a', 'c', 'f', 'h'], 'f') == 'a'
    assert find_second_next_letter(['a', 'c', 'f', 'h'], 'b') == 'f'
    assert find_second_next_letter(['a', 'c', 'f', 'h'], 'm') == 'c'
    assert find_second_next_letter(['a', 'c', 'f', 'h'], 'h') == 'c'
    assert find_second_next_letter(['a', 'b', 'c', 'd', 'e'], 'e') == 'b'


def brute_force_second_next_letter(letters, key):
    found_next = False
    for letter in letters:
        if letter > key and not found_next:
            found_next = True
            continue
        if found_next and letter > key:
            return letter
    if found_next:
        return letters[0]
    return letters[1]  

def test_efficient_vs_brute_force():
    seed(42)  # to make it reproducible

    large_letters = sorted([choice(ascii_lowercase) for _ in range(10000)])
    large_key = choice(ascii_lowercase)
    
    # Time the optimized solution
    start_time_efficient = time()
    result_efficient = find_second_next_letter(large_letters, large_key)
    end_time_efficient = time()
    duration_efficient = end_time_efficient - start_time_efficient

    # Time the brute force solution
    start_time_brute = time()
    result_brute = brute_force_second_next_letter(large_letters, large_key)
    end_time_brute = time()
    duration_brute = end_time_brute - start_time_brute

    # Ensure results match
    assert result_efficient == result_brute

    # Ensure the optimized solution is faster
    assert duration_efficient < duration_brute

    print(f"Optimized solution took: {duration_efficient:.6f} seconds")
    print(f"Brute force solution took: {duration_brute:.6f} seconds")
