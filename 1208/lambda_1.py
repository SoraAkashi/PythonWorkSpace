my_list = [1, 3, 5, 7, 2, 4, 6, 8] 
#list 
# 受け取ったイミテータを基にリストを作成する
#map
# 繰り返し処理をシンプルにする
new_list = list(map(lambda x :x*10,my_list))
print(my_list) 
print(new_list)