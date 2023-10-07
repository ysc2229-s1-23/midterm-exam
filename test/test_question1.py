from questions.question1 import fibonacci
import time

def test_fibonacci():
    # Basic tests
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13

    # Large input test
    start_time = time.time()
    # This doesn't check for a correct value but ensures the function returns in a timely manner
    fib_result = fibonacci(100000)
    end_time = time.time()
    assert (end_time - start_time) < 2  # function should return within 2 seconds for O(n) complexity
    
    print("All tests passed!")

test_fibonacci()
