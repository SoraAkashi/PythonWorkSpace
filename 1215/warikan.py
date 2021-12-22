import math
from typing import Coroutine
def input_int(message):

    """messageを標示 入力値を返す"""
    value = input(f'{message}を入力してください')
    if value.isnumeric():
        value = int(value)
    else:
        value = 0
    return value

def calc_payment(total, num_people):
    """合計金額と人数から金額を計算する。戻り値は、参加者の金額と幹事の金額を[リスト]で返す"""
    pay_pepole = total/num_people
    pay_pepole = math.ceil(pay_pepole / 100)*100
    pay_coodinator = total - pay_pepole * (num_people -1)
    return [pay_pepole,pay_coodinator]
"""
参加者の支払い金額、幹事の支払い金額
参加人数を書式化して出力(戻り値なし)
"""
print(f'支払い:{pay_people}円({num_people}人)')
print(f'幹事金額:{pay_coodinator}円')
#maint
total = input_int('支払い合計金額')
num_people = input_int('参加者人数')
[pay_people,pay_coodinator] = calc_payment(total,num_people)
output_payment(pay_people,pay_coodinator,num_people)
