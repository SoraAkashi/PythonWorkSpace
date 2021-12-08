my_list = [1,2,'ab','xyz',5,6,7,'zz']
#filter
#リストなどから抽出条件をもとに抽出する

new_list = list(filter(lambda x :type(x) == str,my_list))
print(my_list) 
print(new_list)