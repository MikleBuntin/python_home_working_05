# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

file = open('file.txt', 'r')
text = file.read()
file.close()

text_array = text.split()

print("old: ", text)
new_text_array = []
for i in range(0, len(text_array)):
    if text_array[i].find("абв") < 0:
        new_text_array.append(text_array[i])


new = str(new_text_array[0])
for i in range(1, len(new_text_array)):
    new = new + " " + str(new_text_array[i])

print("new: ", new)