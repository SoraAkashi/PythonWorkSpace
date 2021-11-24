DATA_FILENAME='sentence.txt'

word_dic = {}
with open(DATA_FILENAME) as f:          
    for word in f:
        word = word.strip()
        if word in word_dic:            #辞書のキーに単語が存在するのか
        #if word in word_dic.keys():    #別の書き方
            word_dic[word] += 1         #カウントアップ
        else:
            word_dic[word] = 1          #初めての単語なので初期値は１

print(word_dic)