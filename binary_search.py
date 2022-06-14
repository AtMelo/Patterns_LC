def search(nums, target):
    start_i = 0
    end_i = len(nums) - 1
    while start_i <= end_i:
        mean_i = (end_i + start_i) // 2
        if nums[mean_i] == target:
            return mean_i
        if nums[mean_i] < target:
            start_i = mean_i + 1
        else:
            end_i = mean_i - 1
    return -1


def test_search():
    assert search([-1, 0, 3, 5, 9, 12], 9) == 4
    assert search([-1, 0, 3, 5, 9, 12], 0) == 1
    assert search([-1, 0, 3, 5, 9, 12], 2) == -1
