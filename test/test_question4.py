from questions.question4 import KthPlusTwoSmallest

def test_kth_plus_two_smallest():
    kthSmallest1 = KthPlusTwoSmallest([8, 7, 6, 5, 4, 3, 2, 1], 2)
    assert kthSmallest1.add(10) == 4
    assert kthSmallest1.add(9) == 4
    assert kthSmallest1.add(0) == 3

    kthSmallest2 = KthPlusTwoSmallest([], 1)
    assert kthSmallest2.add(1) == None 
    assert kthSmallest2.add(2) == None

    nums = [i for i in range(1, 10001)]
    kthSmallest3 = KthPlusTwoSmallest(nums, 5000)
    assert kthSmallest3.add(10001) == 5002
    assert kthSmallest3.add(10002) == 5002

    kthSmallest4 = KthPlusTwoSmallest([5, 5, 5, 5, 5], 2)
    assert kthSmallest4.add(4) == 5
    assert kthSmallest4.add(6) == 5
    assert kthSmallest4.add(7) == 5

    kthSmallest5 = KthPlusTwoSmallest([1, 2, 3, 4, 5, 6, 7, 8], 1)
    assert kthSmallest5.add(0) == 2
    assert kthSmallest5.add(0) == 1
    assert kthSmallest5.add(0) == 0
    assert kthSmallest5.add(9) == 0

    kthSmallest6 = KthPlusTwoSmallest([1], 10)
    assert kthSmallest6.add(1) == None
    assert kthSmallest6.add(2) == None

    nums_large = [i for i in range(1, 1000001)]
    kthSmallest_large = KthPlusTwoSmallest(nums_large, 500000)
    assert kthSmallest_large.add(0) == 500001
    assert kthSmallest_large.add(-1) == 500000

test_kth_plus_two_smallest()
