"""
領収書用に金額を計算
"""
import math


def cal_fee(ITEMS, TAX_RATE):
    # 辞書を計算しやすくすルために、リストに変更
    lists = []
    for l in ITEMS:
        lists.append(list(l.values()))

    v = []
    for i in lists:
        del i[0]
        v.append(i)

    # 計算する
    s = []
    for i in range(len(v)):
        s.append(v[i][0] * v[i][1])

    FEE = sum(s)

    TAX = math.floor(FEE * TAX_RATE)

    TOTALFEE = FEE + TAX

    return TOTALFEE, TAX