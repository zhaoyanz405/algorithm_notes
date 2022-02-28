"""
二分法 - 在一个有序数组中找某个数是否存在
"""
import copy
from random import randint


class Solution:

    def is_exist(self, arr, num):
        return self.bisection(arr, 0, len(arr) - 1, num)

    def bisection(self, arr, left, right, num):
        if left == right:
            return arr[left] == num

        mid = int((left + right + 1) / 2)  # len(arr[left:right])
        if arr[mid] == num:
            return True

        if arr[mid] > num:
            return self.bisection(arr, left, mid - 1, num)

        if arr[mid] < num:
            return self.bisection(arr, mid + 1, right, num)

    @staticmethod
    def get_sorted_list(maxsize=8, maxvalue=100):
        rlist = [randint(0, maxvalue) for _ in range(maxsize)]
        rlist.sort()
        return rlist

    def comparator(self, arr: list, num: int):
        for x in arr:
            if x == num:
                return True

        return False


if __name__ == '__main__':
    solution = Solution()

    test_list = solution.get_sorted_list(maxsize=randint(0, 100), maxvalue=1024)
    copied_list = copy.deepcopy(test_list)

    query_value = randint(1, 100)
    res = solution.is_exist(test_list, query_value)
    comparator_res = solution.comparator(copied_list, query_value)

    for i in range(10000):
        if res == comparator_res:
            print("succeed~")
        else:
            print("Error, stopped!")
            break
