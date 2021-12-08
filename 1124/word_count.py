def word_Lower(string):
    '''文字列の中の大文字を小文字に変換し、文字列を返す'''
    return string.lower()

def delete_char(string):
    '''NG Listの記号をスペースに置き換え、文字列を返す'''
    ng_list = '.,:()"[]'
    for c in ng_list:
        string = string.replace(c,' ')
    return string

def word_split(string):
    '''文字列をスペースで切り分け、リストを返す'''
    words = string.split(' ')
    return words

def remove_null(words_list):
    '''空のkeyの要素を削除する。辞書を返す'''
    if '' in words_list:
        del words_list['']
    if ' ' in words_list:
        del words_list[' ']
    return words_list

DATA_FILENAME='word_list.txt'

word_dic = {}
with open(DATA_FILENAME) as f:
    for line in f:
        line = line.strip()
        line = line.strip()
        line = word_Lower(line)
        line = delete_char(line)
        print(line) #上記の処理
        words = word_split(line)
        for word in words:
            word = word.strip()
            if word in word_dic:
                word_dic[word] += 1
            else:
                word_dic[word] = 1
        word_dic = remove_null(word_dic)
len_max = 0

for word in word_dic.keys():
    len_max = max(len_max,len(word))
for word in sorted(word_dic):
