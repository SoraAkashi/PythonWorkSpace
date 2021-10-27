while True:
    num = int(input("整数を入力してください(終了 -> 0 )"))
    #P.74 inputについて
    #p.48 キャストについて

    if num == 0:
        break

#if文　javaと同じ考え方。
    if num % 2 == 0:
        print("偶数です。")
    else:
        print("奇数です。")