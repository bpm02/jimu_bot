# coding:utf-8

from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.lib.pagesizes import A4, landscape, portrait
from PyPDF2 import PdfFileReader, PdfFileWriter
import io
import locale  # カンマ３桁


def write_pdf_receipt(RECEIPT_ON, RECEIPT, PRINTRECEIPT, DAYZ, RECEIPT_NUM, CLIENT, KEISHO, TOTALFEE, TAX, TADASHI, FONTNAME):
    if RECEIPT_ON == 1:
        pdfmetrics.registerFont(UnicodeCIDFont(FONTNAME))

        packet = io.BytesIO()
        # create a new PDF with Reportlab
        can = canvas.Canvas(packet, bottomup=False,pagesize=landscape(A4))
        can.setFont(FONTNAME, 9)


        # カンマ３桁
        locale.setlocale(locale.LC_ALL, 'en_US')
        RECEIPT_NUM = locale.format("%d", RECEIPT_NUM, grouping=False)
        TAX = locale.format("%d", TAX, grouping=True)
        TOTALFEE = locale.format("%d", TOTALFEE, grouping=True)


        # jupyter noteの場合はここで区切る

        can.drawString(83, 70, DAYZ)
        can.drawString(287, 70, RECEIPT_NUM)
        can.drawString(70, 95, CLIENT["A6"] + '  ' + KEISHO)
        can.drawString(110, 127, '¥'+ str(TOTALFEE) +'-')
        can.drawString(313, 128, '¥'+ str(TAX))
        can.drawString(80, 154, TADASHI)

        can.save()

        # move to the beginning of the StringIO buffer
        packet.seek(0)
        new_pdf = PdfFileReader(packet)
        # read your existing PDF
        existing_pdf = PdfFileReader(open(RECEIPT, "rb"))
        output = PdfFileWriter()
        # add the "watermark" (which is the new pdf) on the existing page
        page = existing_pdf.getPage(0)
        page.mergePage(new_pdf.getPage(0))
        output.addPage(page)

        #set password
        # output.encrypt("password")

        # finally, write "output" to a real file
        outputStream = open(PRINTRECEIPT, "wb")
        output.write(outputStream)
        outputStream.close()

# set password
# reference https://stackoverflow.com/questions/43475295/encrypt-pdfs-in-python