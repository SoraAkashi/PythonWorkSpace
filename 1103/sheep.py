import time

while True:
    max_num = int(input('何匹に見えますか？:'))
    if max_num > 100:
        print('多すぎます')
        continue
    else:
        break

my_count = 1
while my_count <= max_num:
    print('羊が{}匹'.format(my_count))
    time.sleep(my_count/10)
    my_count += 1