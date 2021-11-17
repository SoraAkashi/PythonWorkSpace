import os
import pickle

DATA_FILENAME = 'word.txt'

if os.path.isfile(DATA_FILENAME):
    with open(DATA_FILENAME,'rb') as f:
        words_list = pickle.load(f)
else:
    words_list = []


while True:
    input_word = input('単語を入力してください:')
    if input_word == "":
        break
    if input_word == 'LIST':
        print('単語リスト:',words_list)
        continue
    if input_word in words_list:
        print('既に登録済みです')
        continue
    else:
        words_list.append(input_word)


print('終了します')
print('これまでに覚えた単語:', words_list)

with open(DATA_FILENAME, 'w') as f:
    pickle.dump(words_list,f)