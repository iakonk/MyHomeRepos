class Solution:
    def generateParenthesis(self, n):
        brackets = {'(': 1, ')': -1}
        result = [('', 0)]

        for i in range(2 * n):

            for accS, accV in result:
                print((accS, accV))
                for s, v in brackets.items():
                    print('s: ', s, 'v:' , v)
            # result = [(accS + s, accV + v) for accS, accV in result
            #           for s, v in brackets.items() if accV + v >= 0 and (i < n or accV + v <= 2 * n - 1 - i)]

        return list(map(lambda x: x[0], result))


ans = Solution().generateParenthesis(3)
print(ans)