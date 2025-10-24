import re

text = input('Введите текст: ')

text_words = [word for word in re.findall(r'\w+', text)]

max_word_len = 0
eng_uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
eng_lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'

for word in text_words:
    word_len = len(word)

    if word_len > max_word_len:
        max_word_len = word_len

print(max_word_len)

encoded_text = ''
alphabet_len = len(eng_uppercase_letters)

for symbol in text:
    if symbol in eng_uppercase_letters:
        symbol_index = eng_uppercase_letters.index(symbol)
        encoded_text += eng_uppercase_letters[symbol_index + max_word_len - alphabet_len]
    elif symbol in eng_lowercase_letters:
        symbol_index = eng_lowercase_letters.index(symbol.lower())
        encoded_text += eng_lowercase_letters[symbol_index + max_word_len - alphabet_len]
    else:
        encoded_text += symbol

print(encoded_text)
