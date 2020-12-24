f = open("C:\\text.txt", 'r', encoding="utf-8")
text1 = f.read()

# text1 = text1.lower()

del_chars = '.,!-?:;<>—«»'
for i in del_chars:
    text1 = text1.replace(i, ' ')

words_list = text1.split()
words_list = list(map(str.lower,words_list))

dict1=dict.fromkeys(words_list,0)

for el in words_list:
    if el in dict1.keys():
        dict1[el] +=1
print(dict1)

value_list = list(dict1.values())
value_list.sort(reverse=True)


dict2 = dict1.copy()

for i in range(5):
    for el in dict2.keys():
        if dict2[el] == value_list[i]:
            dict2[el] = 0
            print(el, ' - встречается в тексте ', dict1[el], ' раз')

words_set = set(words_list)
print('Количество разных слов в тексте =', len(words_set))

f.close()
