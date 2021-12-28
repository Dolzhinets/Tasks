num = int(input('Enter the length of the string '))
new_text = []

#Проверка условия длины строки текста
while True:
    if num > 35:
        break
    elif num  <= 35:
        num = int(input('Try again '))

with open('text.txt', 'r') as file:
    file1 = file.readlines() #читаем все содержимое файла и возвращаем список строк.

# форматирование текста согласно заданной ширины строки  текста
for line in file1:
    number = num
    while True:  
        if len(line) > number: 
            if line[number] != ' ': 
                number -= 1  
            else:
                new_text.append(line[:number]) 
                line = line.replace(line[:number + 1], '') 
                number = num
        else:
            new_text.append(line.rstrip())
            break

 
# выравнивание текста по ширине
text_1 = []
for line in new_text:
    s = line
    i = 0
    for i in range(len(s)):
        if num > len(line):
            if line[i] == ' ':
                line = line[:i] + ' ' + line[i:]
            else:
                if i == int(len(s)):
                    text_1.append(line)
        else:
            text_1.append(line)
            break


with open("text_1.txt", 'w+', encoding = "utf-8") as new_file:
     new_file.writelines('\n'.join(text_1))


