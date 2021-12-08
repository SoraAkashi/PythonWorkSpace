def combine_list(list1, list2):
    '''2つのリストを結合し、リストで返す''' 
    if type(list) is list and type(list) is list:
        # return list1 + list2
        list3 = []
        for i in list1:      #[a,b,c]
            list3.append(i)  
        for i in list2:      #[d,e,f]
            list3.append(i)
        return list3    #[a,b,c,d,e,f]
    else:
        print('引数がリストにありません')
        return[list1,list2]

# main 
# 正常な引数 
print(combine_list([1, 2, 3], [4, 5, 6]))
print(combine_list(list2=[1, 2, 3], list1=[4, 5, 6]))
# 誤った引数
print(combine_list('a', [1, 2, 3]))
print(combine_list([1, 2, 3], 'xyz')) 
print(combine_list(10, 'abc'))