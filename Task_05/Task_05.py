# Дан список чисел. Создайте список, в который попадают числа,
# описываемые возрастающую последовательность. Порядок элементов менять нельзя.
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
import random
with open('array.txt', 'r') as data:
    array = data.read()
print(array)
array = array.replace('[', '')
array = array.replace(']', '')
array = array.split(', ')
# print(type(array))
# print(array)

with open('new_array_list.txt', 'w') as new_array_list:
    for count in range(len(array)):
        new_array = [array[count]]
        new_array_add = [array[count]]
        for count_2 in range(count, len(array)):
            if array[count_2] > array[count]:
                new_array_add = [array[count]]
                new_array_add.append(array[count_2])
                print(new_array_add)
                # print(new_array)
                new_array_list.writelines(new_array_add)
                new_array_list.writelines('\n')
                # new_array_list.writelines(new_array)
                # new_array_list.writelines('\n')
                # last = array[count_2]
                for i in range(count_2, len(array)):
                    # new_array = [array[count]]
                    if array[i] > array[count_2]:
                        new_array_add.append(array[i])
                        print(new_array_add)
                        new_array_list.writelines(new_array_add)
                        new_array_list.writelines('\n')

                        new_array.append(array[i])
                        print(new_array)
                        new_array_list.writelines(new_array)
                        new_array_list.writelines('\n')
                        new_array = [array[count]]
                # last = array[i]



#     new_array = []
#     index = random.randint(0, len(array))
#     new_array.append(array[index])
#     new_index = index
#     last = array[index]
#     for new_index < len(array):
#         new_index = random.randint(index + 1, len(array) - 1)
#         if array[new_index] > last:
#             new_array.append(array[new_index])
#             last = array[new_index]


    # decoded_string += coded_text[i + 1] * int(coded_text[i])
#
# with open('decoded_file.txt', 'w') as decoded:
#     decoded.writelines(decoded_string)
# print("Текст декодирован: ", decoded_string)