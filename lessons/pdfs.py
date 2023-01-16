import PyPDF4
from fpdf import FPDF, XPos, YPos


def get_pdf_info(path):
    with open(file=path, mode='rb') as file:
        pdf = PyPDF4.PdfFileReader(file)
        information = pdf.getDocumentInfo()
        number_of_pages = pdf.getNumPages()

    print(information)
    print(number_of_pages)


def modify_pdf(path, file_name):
    new_pdf = PyPDF4.PdfFileWriter()
    original_pdf = PyPDF4.PdfFileReader(path)

    # Rotate page 90 degrees to the right
    page_0 = original_pdf.getPage(0).rotateClockwise(90)
    new_pdf.addPage(page_0)

    pdf_reader = PyPDF4.PdfFileReader(path)

    # Rotate page 90 degrees to the left
    page_1 = pdf_reader.getPage(0).rotateCounterClockwise(90)
    new_pdf.addPage(page_1)

    with open(file=file_name, mode="wb") as new_file:
        new_pdf.write(new_file)


def create_pdf(path):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font(family='times', style='I', size=14)
    pdf.cell(w=1, txt="hello world!")
    pdf.cell(w=1, h=1, txt="I am the first line at the left", border=0, new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="L")
    pdf.cell(w=1, h=1, txt="I am the centered line", border=0, new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")
    pdf.output(path)


if __name__ == '__main__':
    # get_pdf_info(r'..\supplemental\pdf\dummy.pdf')
    # modify_pdf(r'..\supplemental\pdf\dummy.pdf', r'..\supplemental\pdf\rotate_page.pdf')
    create_pdf(r'..\supplemental\pdf\new_pdf.pdf')


