import re

text = 'Hello, hello how are you. you and you?!/.'.lower() # input('Введите текст: ').lower()

text_words = [word for word in re.findall(r'\w+', text)]

word_count = {}

for word in text_words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

list_word_count = []

for key, value in word_count.items():
    list_word_count += [{key:value}]

len_list_word_count = len(list_word_count)

for i in range(len_list_word_count):
    max_elem_index = i

    for j in range(i+1, len_list_word_count):
        current_elem_value, = list_word_count[j].values()
        max_elem, = list_word_count[max_elem_index].values()

        if max_elem < current_elem_value:
            max_elem_index = j

    list_word_count[i], list_word_count[max_elem_index] = list_word_count[max_elem_index], list_word_count[i]

elems_out = 0
for elem in list_word_count:
    if elems_out < 5:
        print(elem)
        elems_out += 1
