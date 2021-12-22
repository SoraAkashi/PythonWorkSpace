calc = []
kigou = True # True→次の入力は数字 False→次の入力は記号

while True:
    in_str = input('calc :')
    if in_str == '':
        break
    elif in_str == '=':
        break
    elif kigou == True and in_str.isnumeric():
        calc.append(in_str)
        kigou = False
    elif kigou == False and in_str in ['+','-','*','/']:
        calc.append(in_str)
        kigou = True
    else:
        print('入力が正しくありません')
        continue
formula = ''.join(calc)#文字列を結合
print(f'入力した計算式:{formula}\n計算結果:{eval(formula)}')
# eval() イーバル 文字列を式として評価