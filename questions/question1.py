"""
Problem: Calculate the nth Fibonacci Number

Description:
The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones, typically starting with 0 and 1. The sequence starts as: 0, 1, 1, 2, 3, 5, 8, 13, and so on.

Your task is to create a function that, given a non-negative integer `n`, returns the nth number in the Fibonacci sequence.

Function Signature:
def fibonacci(n: int) -> int:

Inputs:
- n (int): A non-negative integer representing the position in the Fibonacci sequence. (0 ≤ n ≤ 10^5)

Returns:
- int: The nth number in the Fibonacci sequence.

Examples:

1. 
Input: 
n = 5
Output: 
5
Explanation:
The sequence starts as 0, 1, 1, 2, 3, 5. The 5th number is 5.

2. 
Input: 
n = 7
Output: 
13
Explanation:
The sequence starts as 0, 1, 1, 2, 3, 5, 8, 13. The 7th number is 13.

3. 
Input:
n = 0
Output:
0
Explanation:
The sequence starts with 0.

Notes:
- Do not use any recursive methods as they can lead to exponential time complexities.
- Iteratively calculate the Fibonacci numbers for efficient computation.
- The Fibonacci sequence is defined as:
    - F(0) = 0
    - F(1) = 1
    - F(n) = F(n-1) + F(n-2) for n > 1

Tags:
- Math
- Iteration
"""

def fibonacci(n):
    return 0


