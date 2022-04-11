from random import randint


class SortCheckAble:

    @staticmethod
    def comparator(data: list) -> list:
        data.sort()
        return data

    @staticmethod
    def get_random_list(maxsize=100, maxvalue=100):
        return [randint(0, maxvalue) for _ in range(randint(0, maxsize))]
