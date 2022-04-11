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

        self.quick_sort(arr, 0, len(arr) - 1)

    def partition(self, arr, L, R):
        less = L - 1  # 左边界
        more = R  # 右边界
        while L < more:
            if arr[L] < arr[R]:
                less += 1
                arr[less], arr[L] = arr[L], arr[less]
                L += 1
            elif arr[L] == arr[R]:
                L += 1
            elif arr[L] > arr[R]:
                more -= 1
                arr[more], arr[L] = arr[L], arr[more]

        arr[more], arr[R] = arr[R], arr[more]
        return less + 1, more

    def quick_sort(self, arr, L, R):
        if L >= R:
            return

        less, more = self.partition(arr, L, R)
        self.quick_sort(arr, L, less - 1)
        self.quick_sort(arr, more + 1, R)


if __name__ == '__main__':
    s = Solution()

    for i in range(1000):
        print('---- %d ----' % i)
        origin_list = s.get_random_list(10000, 100000)
        list1 = copy.deepcopy(origin_list)
        list2 = copy.deepcopy(origin_list)

        s.sort(list1)

        if list1 == s.comparator(list2):
            print("success!")
        else:
            print("fail!")
            print(origin_list)
            print(list1)
            print(list2)
            raise Exception
