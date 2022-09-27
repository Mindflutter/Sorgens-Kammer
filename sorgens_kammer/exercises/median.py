def find_median_sorted_arrays(nums1, nums2) -> float:
    nums1.extend(nums2)
    nums1.sort()

    nums_len = len(nums1)
    if nums_len % 2 == 0:
        median = (nums1[nums_len // 2 - 1] + nums1[nums_len // 2]) / 2
    else:
        median = nums1[nums_len // 2]
    return median


print(find_median_sorted_arrays([1, 3], [2]))
