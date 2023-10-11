from typing import List

def find_second_next_letter(letters, key):
    n = len(letters)

    start, end = 0, n - 1
    while start <= end:
        mid = start + (end - start) // 2
        if key < letters[mid]:
            end = mid - 1
        else:  # key >= letters[mid]:
            start = mid + 1

    # After the next letter, get the second next letter by incrementing the index
    return letters[(start + 1) % n]

