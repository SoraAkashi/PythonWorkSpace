DATA_FILENAME='word_list.txt'

word_dic = {}
with open(DATA_FILENAME) as f:          #空の辞書を作成
    #word_dic = {}                      #ここに書いてもいい
    for word in f:
        word = word.strip()             #改行コードを取り除く
        if word in word_dic:            #辞書のキーに単語が存在するのか
        #if word in word_dic.keys():    #別の書き方
            word_dic[word] += 1         #カウントアップ
        else:
            word_dic[word] = 1          #初めての単語なので初期値は１

print(word_dic)