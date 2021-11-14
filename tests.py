from main import Solution


def test_1():
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    assert Solution().search(nums, target) == 4


def test_2():
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 3
    assert Solution().search(nums, target) == -1


def test_3():
    nums = [1]
    target = 0
    assert Solution().search(nums, target) == -1


def test_4():
    nums = [4, 5, 6, 7, 0, 1, 2, 3]
    target = 0
    assert Solution().search(nums, target) == 4


def test_5():
    nums = [1, 3]
    target = 0
    assert Solution().search(nums, target) == -1


def test_6():
    nums = [1, 3]
    target = 3
    assert Solution().search(nums, target) == 1


def test_7():
    nums = [1, 3, 5]
    target = 5
    assert Solution().search(nums, target) == 2


def test_8():
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 1
    assert Solution().search(nums, target) == 5


def test_9():
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 5
    assert Solution().search(nums, target) == 1


def test_10():
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 6
    assert Solution().search(nums, target) == 2


def test_11():
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 7
    assert Solution().search(nums, target) == 3
