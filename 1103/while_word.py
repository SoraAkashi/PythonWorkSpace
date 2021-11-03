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
else:
    pass