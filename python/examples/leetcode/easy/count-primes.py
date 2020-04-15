class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return False

        def is_prime(n):
            for num in range(2, n):
                if n % num == 0:
                    return False
            return True

        ans = [num for num in range(2, n) if is_prime(num)]
        return len(ans)


ans = Solution().countPrimes(10)
print(ans)


# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
class Solution(object):
    def countPrimes(self, n):
        """"""
        if n <= 1:
            return 0

        res = [False, False] + [True] * (n - 2)
        for ind in range(2, n):
            if res[ind]:
                for every_i_th in range(ind + ind, n, ind):
                    res[every_i_th] = False
        return any(res)


ans = Solution().countPrimes(2)
print(ans)
