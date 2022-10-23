# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

file = open('file.txt', 'r')
text = file.read()
file.close()

text_array = text.split()

print(text_array)
