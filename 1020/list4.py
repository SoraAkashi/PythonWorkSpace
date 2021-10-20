n=input("整数を入力してください")
#入力した値を整数にしないといけないnum = int(n)
numbres = range(1,int(n) + 1)

total = 0
average = 0
num = int(n)
i = 0

while i <= num:
    total += i
    i += 1
average = total / num

print ("1~{n}までの合計:{total}")
print("平均:{average}")