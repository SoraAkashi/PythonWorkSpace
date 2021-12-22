"""
カードから、5枚のカードをランダムに選択する。
カードを数字の大きい方から並べ、出力する。
sortのkeyに関してはテキスト P.183を良く理解しよう
"""
# 初期化
from random import random


marks = ('S','H','C','D')	# 4種類のマーク
cards = []                  # デッキ用リスト

for m in marks:
    for n in range(1,14):
        t = (m,n)           # タプルでカード生成
        cards.append(t)     # リストに追加
#5枚選択
select_cards = random.sample(cards,5)
#並び替え
select_cards.sort(reverse=True, key=lambda x: x[1])
#出力
print(select_cards)