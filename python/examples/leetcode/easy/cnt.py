def find_num_freq(k, n):
     def digits(num):
         """ :returns an array of digits, example: [3, 5] for 35 """
         res = []
         while num:
            num, last = divmod(num, 10)
            res.append(last)
         return res

     freq = 0
     for i in range(k, n+1):
         # count a number of occurrences k in a number
         freq += sum([True for num in digits(i) if num == k])
     return freq


print(find_num_freq(2, 35))