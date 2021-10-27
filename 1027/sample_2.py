fruits = ['バナナ','リンゴ','オレンジ']

while True:

    input_fruits = input("果物をカタカナで入力してください:")

    if input_fruits == '':
        break

    if input_fruits in fruits:
        print(f'{input_fruits}は知っています！。')
    else:
        print(f'{input_fruits}は知りませんでした。覚えておきます')
        fruits.append(input_fruits)

print('知っている果実')
print(fruits)
