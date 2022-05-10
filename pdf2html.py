# -*- coding: utf-8 -*- 


#import 해주기
import pdftotree
#-------------------------------------------

# [파일 이름 읽어오기]
import os
# path_dir할 때 \ -> / 바꿔주기
# 이 코드가 위치 한 디렉토리로 설정해주기!
path_dir=r'C:\Users\TFG256XG\Documents\GitHub\hwp_bounding_box-task\pdf_file'
file_list=os.listdir(path_dir)
print(file_list)
#-------------------------------------------

# [ pdf 파일만 골라서 html로 ]
for f_name_pdf in file_list:
    idx=file_list.index(f_name_pdf)    
    
    # 파일명 (.pdf) '' 인 것들만 고르기!
    fn=f_name_pdf.split('.pdf')
    if(len(fn)<2 or fn[1]!=''): # .oldPdf 이렇게 확장자 다른 애들은 len(fn)==1
        print('continue: ',fn)
        continue
    f_name_html=fn[0]+'.html'
    
    try:
        result = pdftotree.parse(f_name_pdf,html_path=None, model_type='table',model_path=None,visualize=False)
    except:
        print('continue')
        continue 
        
    with open('out.html','w',-1,'utf-8') as f:
        f.write(result)
    
    #전처리 코드
    import re
    file = open('out.html', 'r', encoding='utf-8')
    text = file.read()

    text = text.replace('\\n\\t', ' ')
    text = text.replace('\\t', '')

    text = text.replace('<table', '<table border=\'1\'')
	
    # f_name_html.html파일에 출력
    new_file = open(f_name_html, 'w', encoding='utf-8')
    new_file.write(text)
    new_file.close()

    file.close()