# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

file = open('file.txt', 'r')
text = file.read()
file.close()
text += ' '

new_string = ''
t = 1
for i in range(len(text) - 1):

    if text[i] == text[i + 1]:
        t += 1
    else:
        new_string += str(t) + text[i]
        t = 1

print("Текст из файла: ", text)
print("Закодирован в: ", new_string)

with open('coded_file.txt', 'w') as data:
    data.write(new_string)

print("и записан в файл: coded_file.txt")
next = int(input("Для продолжения введите 1: "))
if next == 1:

    with open('coded_file.txt', 'r') as data_2:
        coded_text = data_2.read() + ' '
    print(coded_text)
    decoded_string = ''

    for i in range(0, len(coded_text) - 1, 2):
       decoded_string += coded_text[i + 1] * int(coded_text[i])

    with open('decoded_file.txt', 'w') as decoded:
        decoded.writelines(decoded_string)
    print("Текст декодирован: ", decoded_string)

else:
    print("Досвидания!")