def out_csvdata(**kwargs): 
    out_list = []
    for token in ['B','L','D']:
        out_list.append(kwargs[token])
    else:
        out_list.append('-')
    #print(out_list)
    print(",".join(out_list))
# main 
eat = {} 
while True: 
    menu = input("朝食(B) 昼食(L) 夕食(D)と食べたものを入力してください：") 
    if menu == '': 
        break 
    token, menu = menu.split(',') 
    if token in ['B', 'L', 'D']:
        eat[token] = menu 
    else: 
        print('記号が間違っています。登録しません') 
        continue 
out_csvdata(**eat)