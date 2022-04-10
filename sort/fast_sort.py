"""
快速排序v1

1. 以数组最后一位x进行荷兰国旗排序，得到[<=x, >x, x]
2. 交换x与>x区域首位元素得到[<=x, x, >x]
3. 对<=x及>x区域递归进行处理
"""
import copy

from sort import SortCheckAble


class Solution(SortCheckAble):

    def sort(self, arr):
        if len(arr) < 2:
            return arr

        if len(arr) == 2:
            if arr[1] < arr[0]:
                arr[0], arr[1] = arr[1], arr[0]
            return arr

        target = len(arr) - 1
        left = -1
        right = len(arr) - 1

        idx = 0
        while right > idx:
            if arr[idx] < arr[target]:
                arr[idx], arr[left+ 1] = arr[left + 1], arr[idx]
                left += 1
                idx += 1

            elif arr[idx] == arr[target]:
                idx += 1


            elif arr[idx] > arr[target]:
                arr[idx], arr[right - 1] = arr[right - 1], arr[idx]
                right -= 1

            print(arr)

        arr[target], arr[right] = arr[right], arr[target]
        print(arr)

        arr[:left + 1] = self.sort(arr[:left + 1])
        arr[right + 1:] = self.sort(arr[right + 1:])
        return arr


if __name__ == '__main__':
    s = Solution()
    s.sort([1, 6, 1, 7, 6])

    for i in range(10):
        print('---- %d ----' % i)
        random_list = s.get_random_list(10, 10)
        copied_rlist = copy.deepcopy(random_list)

        if s.sort(random_list) == s.comparator(copied_rlist):
            print("success!")
        else:
            print("fail!")
            print(random_list)
            print(s.sort(random_list))
            raise Exception
