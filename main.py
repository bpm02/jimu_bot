from input import *
from library.jimu_bot import JimuBot

date = "" # 作成日を任意で設定する場合は入力する 2022年01月01日

#請求書の商品名
items = [
    {  # 0
        'A17': "商品名", #商品名
        'W17': 10000, #単価
        'AA17': 1, #個数
    },
]


if __name__ == '__main__':

    j = JimuBot(client['会社名'], company)
    #j.address()
    #j.invoice(items)
    #j.receipt(items, "但し書き名")