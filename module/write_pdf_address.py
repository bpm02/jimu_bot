from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.lib.pagesizes import A4, landscape
from PyPDF2 import PdfFileReader, PdfFileWriter
import io

def write_pdf_address(ADDRESS_ON, ADDRESS_FILE, CLIENT, FONTNAME, FINISHED_DIR):

    if ADDRESS_ON == 1:
        pdfmetrics.registerFont(UnicodeCIDFont(FONTNAME))

        packet = io.BytesIO()
        # create a new PDF with Reportlab
        c = canvas.Canvas(packet, bottomup=False,pagesize=landscape(A4))
        c.setFont(FONTNAME, 13)

        c.drawString(90, -137, CLIENT['A6'] + ' 御中')
        c.drawString(90, -187, CLIENT['A8'])
        c.drawString(90, -170, CLIENT['A9'])
        c.drawString(90, -155, CLIENT['A11'])

        c.save()

        # move to the beginning of the StringIO buffer
        packet.seek(0)
        new_pdf = PdfFileReader(packet)
        # read your existing PDF
        existing_pdf = PdfFileReader(open(ADDRESS_FILE, "rb"))
        output = PdfFileWriter()
        # add the "watermark" (which is the new pdf) on the existing page
        page = existing_pdf.getPage(0)
        page.mergePage(new_pdf.getPage(0))
        output.addPage(page)

        # set password
        # output.encrypt("password")

        # finally, write "output" to a real file
        output_stream = open(FINISHED_DIR + CLIENT['A6']+'送付先.pdf', "wb")
        output.write(output_stream)
        output_stream.close()
