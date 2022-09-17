from datetime import datetime
import time
import re

# python filez
from module import *
from input import client



class JimuBot:

    """ 領収書、請求書を作成するクラス

    Attributes:
        client (obj: ):　クライアントのデータ
        date (date):日付け
        item (obj:): 商品名や価格のオブジェクト
    """

    def __init__(self, client, company, date=""):

        self.__client = {
            'A6':client[0],
            'A8':client[1],
            'A9':client[2],
            'A10':client[3],
            'A11':client[4],
        }

        self.__company = {
            'W6':company[0],
            'W8':company[1],
            'W9':company[2],
            'W10':company[3],
            'W11':company[4],
        }

        self.__date = date
        self.__created_date = ""
        self.__item = []


        self.__sheet = 'Sheet1'

        #出来上がりディレクトリ
        self.__finished_dir = 'FINISHED/'

        self.__address_file = 'files/address.pdf'
        self.__invoice_file = 'files/invoice.xlsx'
        self.__receipt_file = 'files/receipt.pdf'

        self.__fontname = "HeiseiKakuGo-W5"

        self.__tax_rate = 0.1
        self.__keisho = '御中'

  

        # 日付の処理
        self.date()

    @property
    def finished_dir(self):
        pass

    @finished_dir.setter
    def finished_dir(self, arg):
        self.__finished_dir = arg


    @property
    def address_file(self):
        pass

    @address_file.setter
    def address_file(self, arg):
        self.__address_file = arg


    @property
    def invoice_file(self):
        pass

    @invoice_file.setter
    def invoice_file(self, arg):
        self.__invoice_file = arg


    @property
    def receipt_file(self):
        pass

    @receipt_file.setter
    def receipt_file(self, arg):
        self.__receipt_file = arg


    @property
    def tax_rate(self):
        pass

    @tax_rate.setter
    def tax_rate(self, arg):
        self.__tax_rate = arg


    @property
    def keisho(self):
        pass

    @keisho.setter
    def keisho(self, arg):
        self.__keisho = arg


    @property
    def fontname(self):
        pass

    @fontname.setter
    def fontname(self, arg):
        self.__fontname = arg


    def date(self):
        """日付の処理
        """

        if self.__date == "":
            self.__date = ""
            self.__date = datetime.now().strftime("%Y年%m月%d日")
            self.__created_date = datetime.now().strftime("%Y%m%d")
        else:
            self.__created_date = ""
            self.__created_date = re.sub(r'\D', '', self.__date)


    def invoice(self, item):
        """請求書を作成

        Args:
            item (_type_): _description_
            tadashi (_type_): _description_
        """
        
        self.__item = item

        # 領収書 ファイル名

        file_name = self.__created_date + self.__client['A6']

        write_exl(1, self.__invoice_file, self.__sheet, self.__client, self.__item, self.__date, self.__finished_dir, file_name)

        print('請求書を作成しました!')
        
    
    def receipt(self, item, tadashi):
        """領収書を作成

        """

        self.__item = item
        self.__tadashi = tadashi

        self.RECEIPT_NUM = int(time.time())

        file_name = self.__created_date + self.__client['A6']

        self.PRINTRECEIPT = self.__finished_dir + '領収書' + file_name +'.pdf'


        self.TOTALFEE, self.TAX = calculate_fee.cal_fee(self.__item, self.__tax_rate)

        write_pdf_receipt(1, self.__receipt_file, self.PRINTRECEIPT, self.__date, self.RECEIPT_NUM, self.__client, self.__keisho, self.TOTALFEE, self.TAX, self.__tadashi, self.__fontname)

        print('領収書を作成しました!')


    def address(self):
        """送付先を作成
        """
        write_pdf_address(1, self.__address_file, self.__client, self.__fontname, self.__finished_dir)
        print('送付先を作成しました!')



