# Дан список чисел. Создайте список, в который попадают числа,
# описываемые возрастающую последовательность. Порядок элементов менять нельзя.
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

with open('array.txt', 'r') as data:
    array = data.read()
print(coded_text)
decoded_string = ''

for i in range(0, len(coded_text) - 1, 2):
    decoded_string += coded_text[i + 1] * int(coded_text[i])

with open('decoded_file.txt', 'w') as decoded:
    decoded.writelines(decoded_string)
print("Текст декодирован: ", decoded_string)