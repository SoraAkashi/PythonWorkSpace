# 関数を辞書で渡し、実行する
def func1():
    print("Hello")

def func2():
    print("Goodbye")

#main
run_list = {'a':func1, 'b':func2}

while True:
    select = input('どちらを実行しますか')
    #P.104 制御構文について
    if select =='':  #入力された文字が空文字だった時
        break

    if select in run_list.keys(): #run_list(辞書)のkeyに入力値が存在する時
        run_list[select]()
    else:
        print('どちらかを選択してください')

print(run_list.keys()) #dict_keys(['a','b'])