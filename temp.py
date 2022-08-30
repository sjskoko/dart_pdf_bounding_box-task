from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)
from pdf2image import convert_from_bytes, convert_from_path



images = convert_from_path('sample_pdf_file/[삼성바이오로직스]사업보고서(2022.03.21).pdf')


images[0].save('01.jpg', 'JPEG')