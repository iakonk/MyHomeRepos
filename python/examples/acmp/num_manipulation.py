# https://acmp.ru/index.asp?main=task&id_task=9
#   INPUT.TXT:
# 5
# -7 5 -1 3 9
#  = 17 -15
# 10
# -5 1 2 3 4 5 6 7 8 -3
#  = 36 5040
# 8
# 3 14 -9 4 -5 1 -12 4
#  = 26 180
#   ID	        Дата	            Язык	Результат	    Тест	Время	Память
#   12407733	19.02.2020 22:16:31	Python	Accepted	 	        0,031	718 Кб


with open('INPUT.TXT') as rfd:
    size, array = rfd.readlines()
    size, array = int(size), array.split()


max_num_ind = 0
min_num_ind = 0
positive_sum = 0
for i in range(0, size):
    num = int(array[i])
    if num > 0:
        positive_sum += num
    if num <= int(array[min_num_ind]):
        min_num_ind = i
    if num >= int(array[max_num_ind]):
        max_num_ind = i

multiplication_res = 1
start_pos = (min_num_ind if min_num_ind < max_num_ind else max_num_ind) + 1
end_pos = max_num_ind if max_num_ind > min_num_ind else min_num_ind
for i in range(start_pos, end_pos):
    multiplication_res *= int(array[i])

with open('OUTPUT.TXT', 'w') as wfd:
    wfd.write('{0} {1}'.format(positive_sum, multiplication_res))
