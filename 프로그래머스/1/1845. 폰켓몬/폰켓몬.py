def solution(nums):
    nums_dict = dict()
    num_count = 0

    for num in nums:

        if num in nums_dict:
            nums_dict[num] += 1
        else:
            nums_dict[num] = 1
            num_count += 1

    return min(num_count, len(nums) / 2)