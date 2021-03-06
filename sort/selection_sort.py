"""
ιζ©ζεΊ
"""
from copy import deepcopy

from sort import SortCheckAble


class Solution(SortCheckAble):

    @staticmethod
    def sort(data: list) -> list:
        if len(data) < 2:
            return data

        for i in range(len(data) - 1):
            mindex = i
            for j in range(i + 1, len(data)):
                if data[j] < data[mindex]:
                    mindex = j

            if i != mindex:
                data[i], data[mindex] = data[mindex], data[i]

        return data


if __name__ == "__main__":
    solution = Solution()

    random_data = solution.get_random_list(10, 100)
    copied_data = deepcopy(random_data)

    res = solution.sort(random_data)
    com = solution.comparator(copied_data)
    if res == com:
        print("Succeed!")
        print(res)
        print(com)
    else:
        print("Error, expected %s\n, but%s\n", res, com)
