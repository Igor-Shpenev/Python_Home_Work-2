# Реализуйте алгоритм перемешивания списка.

list = [1, 3, 5, 7, 9, 2, 4, 6, 8]
i = 0
temp = 0
while i < (len(list)+1)/3:
    temp = list[i]
    list[i] = list[-i]
    list[-i] = temp
    i += 1
print(list)
