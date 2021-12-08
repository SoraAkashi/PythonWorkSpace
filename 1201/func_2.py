def tax_included(price, tax=10):
    '''税込金額を計算する。税率を省略した場合は10％になる'''
    if tax < 0: 
        return None 
    else:
        return int(price * (1+tax/100))

#main


#5000の税込金額は5500円
print('{}の税込金額は{}円'.format(5000,tax_included(5000)))
#5000の消費税8％の税込金額は5400円
print('{}の税込金額は{}円'.format(5000,tax_included(5000,8)))
#5000の消費税-5％の税込金額はNone円
print('{}の税込金額は{}円'.format(5000,tax_included(5000,-5)))