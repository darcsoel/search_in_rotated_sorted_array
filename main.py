from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        first = 0
        last = len(nums) - 1

        while True:
            divider = round((first + last) / 2)
            cur = nums[divider]
            first_el = nums[first]
            last_el = nums[last]

            if first_el == target:
                return first
            elif last_el == target:
                return last

            if last - first < 2 and target not in (first_el, last_el):
                return -1

            if abs(first_el - cur) > abs(last_el - cur):
                if target < cur:
                    last = divider
                elif target < last_el:
                    first = divider
                else:
                    last = divider
            else:
                if target > cur:
                    first = divider
                elif target > first_el:
                    last = divider
                else:
                    first = divider
