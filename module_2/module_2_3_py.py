my_list = [42, 69, 322, 13, 0, 99, 9, 8, 7, 5]
index_lst = 0

while index_lst < len(my_list):
    elem = my_list[index_lst]
    index_lst += 1
    if elem == 0:

        continue
    elif elem < 0:
        break
    else:
        print(elem)
