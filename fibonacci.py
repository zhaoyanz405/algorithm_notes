import time


def fib(n):
    """
    f(n) = f(n-1) + f(n-2)
    :param n:
    :return:
    """
    if n == 0:
        return 0

    if n == 1:
        return 1

    return fib(n - 1) + fib(n - 2)


memory = {0: 0, 1: 1}


def fib_with_memory(n):
    if n in memory:
        return memory[n]
    else:
        res = fib_with_memory(n - 1) + fib_with_memory(n - 2)
        memory[n] = res
        return res


def fib_dp(n):
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[-1]


if __name__ == '__main__':
    n = 35
    t1 = time.time()
    print(fib(n))

    t2 = time.time()
    print("fib cost", t2 - t1)
    print(fib_with_memory(n))
    t3 = time.time()
    print("fib with memory cost", t3 - t2)

    print(fib_dp(n))
    t4 = time.time()
    print("fib dp cost", t4 - t3)
