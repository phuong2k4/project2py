from PyPDF2 import PdfReader, PdfWriter
from getpass import getpass

def protect_pdf(input_pdf,output_pdf):
    reader = PdfReader('filelockbypython.pdf')
    writer = PdfWriter()

    for page in reader.pages:
        print(page)
        writer.add_page(page)

    password = getpass("Enter your password: ")
    writer.encrypt(password)
    with open(output_pdf, "wb") as output_file:
        writer.write(output_file)
    print(f"The PDF has password.")
protect_pdf('filelockbypython.pdf', 'filesecure.pdf')
