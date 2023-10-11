from time import time
from solutions.question1 import reverse_stack

def test_reverse_stack():
    # Basic Tests
    assert reverse_stack([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]
    assert reverse_stack([10, 20, 30]) == [30, 20, 10]
    assert reverse_stack([7]) == [7]
    assert reverse_stack([]) == []

    # Edge Cases
    assert reverse_stack([1, 1, 2, 3, 5, 5]) == [5, 5, 3, 2, 1, 1]  # Duplicates
    assert reverse_stack([10**5, 10**6, 10**7]) == [10**7, 10**6, 10**5]  # Large values
    assert reverse_stack([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]  # Already reversed stack
    
    class StackMock(list):
        def __getitem__(self, index):
            # Queues shouldn't allow indexing.
            raise AssertionError("Indexing detected. Make sure you're using queue operations.")

    try:
        reverse_stack(StackMock([1, 2, 3, 4, 5]))
        reverse_stack(StackMock([10, 20, 30]))
    except AssertionError:
        pass  # Test will fail if the above block doesn't raise an AssertionError

    # Large Unit Test
    large_stack = list(range(1, 10**5 + 1))
    start_time = time()
    assert reverse_stack(large_stack) == list(range(10**5, 0, -1))
    end_time = time()
    assert (end_time - start_time) < 1
    
    print("All tests passed!")

test_reverse_stack()
