import PyPDF2
from PyPDF2 import PageObject
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import io

def create_watermark(watermark_text, page_size):
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=page_size)
    can.setFont("Helvetica", 40)
    can.setFillColorRGB(0.5, 0.5, 0.5, alpha=0.3)  # 半透明

    # 获取页面的宽度和高度
    width, height = page_size

    # 设置水印间隔
    x_interval = 200
    y_interval = 100

    # 以对角线方式添加多个水印
    for x in range(0, int(width), x_interval):
        for y in range(0, int(height), y_interval):
            can.saveState()
            can.translate(x, y)
            can.rotate(45)
            can.drawString(0, 0, watermark_text)
            can.restoreState()

    can.save()
    packet.seek(0)
    return packet

def add_watermark_to_pdf(input_pdf_path, output_pdf_path, watermark_text):
    with open(input_pdf_path, "rb") as input_pdf_file:
        input_pdf = PyPDF2.PdfReader(input_pdf_file)
        output_pdf = PyPDF2.PdfWriter()

        for page_number in range(len(input_pdf.pages)):
            page = input_pdf.pages[page_number]
            packet = create_watermark(watermark_text, page.mediabox.upper_right)
            watermark_pdf = PyPDF2.PdfReader(packet)
            watermark_page = watermark_pdf.pages[0]

            page.merge_page(watermark_page)
            output_pdf.add_page(page)

        with open(output_pdf_path, "wb") as output_pdf_file:
            output_pdf.write(output_pdf_file)

# 使用示例
input_pdf_path = '/Users/tao/Downloads/UBC/2022WT1_TL_Events_Vol_Certificate_Part1.pdf'
output_pdf_path = '/Users/tao/Downloads/UBC/2.pdf'
watermark_text = 'Python'
add_watermark_to_pdf(input_pdf_path, output_pdf_path, watermark_text)
