from cgi import test
import streamlit as st
import pandas as pd
import numpy as np
import img2pdf
from util import *
from caption_extraction import *

st.title('PDF Object Extractor')


#########

uploaded_file = st.file_uploader('Drop the pdf', type='pdf')

# display document


if uploaded_file is not None:

    with open(uploaded_file.name, 'wb') as f:
        f.write(uploaded_file.getbuffer())
    f.close()

    uploaded_file_name = uploaded_file.name
    # with pdfplumber.open(uploaded_file_name) as pdf:
    #     pages = pdf.pages
    pdf = pdfplumber.open(uploaded_file_name)
    pages = pdf.pages

    # 저장용 pdf 별 object dictionary 생성
    text_dict = {}
    image_dict = {}
    table_dict = {}
    
    # 이미지 모음
    img_list = []

    # 각 page 루프
    for i, page in tqdm(enumerate(pages)):

        # text, image 객체 추출
        text = get_text(page)
        image = get_image(page)
        # tableobject 객체 딕셔너리로 변환
        table_obj = get_table(page)
        table = []
        for tboj in table_obj:
            table.append(table_object_to_dict(tboj))

        # page 별로 저장
        text_dict[i] = text
        image_dict[i] = image
        table_dict[i] = table
        st.header('This is table summary')
        st.caption(table)

        
        im = page.to_image(resolution=400)

        if table:
            table_bbox_list = [i.bbox for i in table_obj]
            print(i, 'page Table', table_bbox_list)
            for bbox in bbox_padding(table_bbox_list):
                im.draw_rect(bbox, stroke='red')



        if image:
            page_height = page.height

            img_bbox_list = [(image['x0'], page_height - image['y1'], image['x1'], page_height - image['y0']) for image in image]
            print(i, 'page Image', img_bbox_list)
            for bbox in bbox_padding(img_bbox_list):
                im.draw_rect(bbox, stroke='blue')
        
        img_list.append(im)

    st.image(img_list[0])
    output_pdf = img2pdf.convert(img_list)






    options = st.multiselect(
        'Choose Object',
        ['Table', 'Image'],
        ['Table'])

    if 'Table' in options:
        pass

    st.download_button(label="Export_Report",
                        data=output_pdf,
                        file_name="test.pdf")

    # streamlit run sample_code.py