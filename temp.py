from pdf2jpg import pdf2jpg


inputpath = r"sample_pdf_file\[삼성바이오로직스]사업보고서(2022.03.21).pdf"
outputpath = r""
result = pdf2jpg.convert_pdf2jpg(inputpath,outputpath, pages="ALL")