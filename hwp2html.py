# -*- coding: utf-8 -*- 
# from tkFileDialog import askopenfilename 
# from pdfminer.pdfdocument import PDFDocument 
# from pdfminer.pdfparser import PDFParser 
# from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter 
# from pdfminer.pdfdevice import PDFDevice, TagExtractor 
# from pdfminer.pdfpage import PDFPage 
# from pdfminer.converter import XMLConverter, HTMLConverter, TextConverter 
# from pdfminer.cmapdb import CMapDB 
# from pdfminer.layout import LAParams 
# from pdfminer.image import ImageWriter 
# 
password = '' 
pagenos = set() 
maxpages = 0 
# output option 
outfile = None 
outtype = None 
imagewriter = None 
rotation = 0 
layoutmode = 'normal' 
codec = 'utf-8' 
codec = 'euc-kr' 
pageno = 1 
scale = 1 
caching = True 
showpageno = True 
laparams = LAParams() 
fpname = askopenfilename() 
fp = file(fpname, 'rb') 
outfpname = 'pdf2output' 
rsrcmgr = PDFResourceManager(caching=caching) 
outfp = file(outfpname + '.txt', 'w') 
device = TextConverter(rsrcmgr, outfp, codec=codec,
laparams=laparams, imagewriter=imagewriter) 
interpreter = PDFPageInterpreter(rsrcmgr, device) 

for page in PDFPage.get_pages(fp, pagenos,
                                maxpages=maxpages, password=password,
                                caching=caching, check_extractable=True):
    page.rotate = (page.rotate+rotation) % 360
    interpreter.process_page(page)      
outfp.close() 

rsrcmgr = PDFResourceManager(caching=caching) outfp = file(outfpname + '.html', 'w') device = HTMLConverter(rsrcmgr, outfp, codec=codec, scale=scale,                        layoutmode=layoutmode, laparams=laparams,                        imagewriter=imagewriter) interpreter = PDFPageInterpreter(rsrcmgr, device) for page in PDFPage.get_pages(fp, pagenos,                               maxpages=maxpages, password=password,                               caching=caching, check_extractable=True):     page.rotate = (page.rotate+rotation) % 360     interpreter.process_page(page) outfp.close() fp.close()

출처: https://dgkim5360.tistory.com/entry/python-pdfminer-convert-pdf-to-html-txt [개발새발로그]