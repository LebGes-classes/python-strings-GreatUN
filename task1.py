import re

text = 'язык программирования Python' # input('Введите текст: ')

text_words = [word for word in re.findall(r'\w+', text)]

reversed_text = ''
for i in range(len(text_words)-1, -1, -1):
    reversed_text += text_words[i] + ' '

print(f'Текст с обратным порядком слов: {reversed_text}')

mirrored_text = ''
for i in range(len(text)-1, -1, -1):
    mirrored_text += text[i]

print(f'Зеркальный текст: {mirrored_text}')
