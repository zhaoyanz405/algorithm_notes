"""
荷兰国旗问题

给定无序数组和一个数字x，要求经过算法可以得到一个新数组，满足：
- 与x相等的数字排列在一起
- 比x小的数字排列在左侧
- 比x大的数字排列在右侧
"""

from sort import SortCheckAble


class Solution(SortCheckAble):

    def sort(self, arr, target):
        left = -1
        right = len(arr)

        idx = 0
        while right > idx:
            if arr[idx] < target:
                arr[idx], arr[left + 1] = arr[left + 1], arr[idx]

                left += 1
                idx += 1

            elif arr[idx] == target:
                idx += 1

            elif arr[idx] > target:
                arr[idx], arr[right - 1] = arr[right - 1], arr[idx]
                right -= 1

    def check(self, data: list, target):
        flag = -1  # -1 -> 0 -> 1 flag只可以由小变大，不可以由大变小
        for item in data:
            if item < target:
                if flag > -1:
                    raise

            if item == target:
                if flag > 0:
                    raise

                flag = 0

            if item > target:
                flag = 1


if __name__ == '__main__':
    s = Solution()

    target_num = 50
    rlist = s.get_random_list(10, 100)

    print("Before:")
    print(rlist)
    s.sort(rlist, target_num)
    print("After:")
    print(rlist)

    s.check(rlist, target_num)
