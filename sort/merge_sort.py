import copy

from sort import SortCheckAble


class Solution(SortCheckAble):
    def sort(self, arr):
        return self.merge_sort(arr)

    def merge_sort(self, arr):
        if len(arr) < 2:
            return arr

        mid = int(len(arr) >> 1)
        left = self.merge_sort(arr[:mid])
        right = self.merge_sort(arr[mid:])
        return self.merge(left, right)

    def merge(self, arr1, arr2):
        p1 = 0
        p2 = 0

        final_arr = []

        while p1 != len(arr1) or p2 != len(arr2):

            if p1 != len(arr1) and p2 != len(arr2):
                if arr1[p1] <= arr2[p2]:
                    item = arr1[p1]
                    p1 += 1
                else:
                    item = arr2[p2]
                    p2 += 1

            elif p1 != len(arr1) and p2 == len(arr2):
                item = arr1[p1]
                p1 += 1

            elif p1 == len(arr1) and p2 != len(arr2):
                item = arr2[p2]
                p2 += 1

            final_arr.append(item)

        return final_arr


def test_solution_merge():
    s = Solution()

    list1 = s.comparator(s.get_random_list(100, 100))
    list2 = s.comparator(s.get_random_list(100, 100))

    assert s.comparator(list1 + list2) == s.merge(list1, list2)


if __name__ == '__main__':
    s = Solution()

    for i in range(1000):
        random_list = s.get_random_list(100, 100)
        copied_list = copy.deepcopy(random_list)

        assert s.sort(random_list) == s.comparator(copied_list)
