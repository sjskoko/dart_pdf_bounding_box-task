from fileinput import filelineno, filename
import pdfplumber
import os

## pdf folder path
folder_path = 'pdf_file'

## bounding box img save path
save_path = 'img_file'

## list file name
pdf_file_list = os.listdir(folder_path)
pdf_file_path = [folder_path + '/' + file_name for file_name in pdf_file_list]
# print(pdf_file_path)

## loop of saving img
for i in range(len(pdf_file_list)):

    pdf = pdfplumber.open(pdf_file_path[i]) # open ith file
    pages = pdf.pages # define each page

    file_name = pdf_file_list[i]
    pdf_save_directory = save_path + '/' + file_name[:-4]

    ## make directory for file
    if not os.path.exists(pdf_save_directory):
        os.makedirs(pdf_save_directory)

    ## loop of each page
    for j in range(len(pages)):
        
        page = pages[j]
        page_height = page.height

        tabel_objects = page.find_tables()
        img_objects = page.images
        im = page.to_image(resolution=400)

        if tabel_objects:
            table_bbox_list = [i.bbox for i in tabel_objects]

            for bbox in table_bbox_list:
                im.draw_rect(bbox, stroke='red')

        if img_objects:
            img_bbox_list = [(image['x0'], page_height - image['y1'], image['x1'], page_height - image['y0']) for image in img_objects]

            for bbox in img_bbox_list:
                im.draw_rect(bbox, stroke='blue')

        im.save(pdf_save_directory + '/' + file_name[:-4] + '_' + str(j) + '.png', format='PNG')
            





# pdf = pdfplumber.open(file_path[0])
# pdf = pdfplumber.open('sample.pdf')
# page = pdf.pages[1]
# page.show()

# page.extract_tables()
# image_in_page_89 = page.images
# page_height = page.height
# image = image_in_page_89[1] # assuming images_in_page has at least one element, only for understanding purpose. 
# image_bbox = (image['x0'], page_height - image['y1'], image['x1'], page_height - image['y0'])
# # cropped_page = page.crop(image_bbox)
# #image_obj = cropped_page.to_image(resolution=400)
# image_obj.save('sample_img2.png')

# ################
# a= page.find_tables()

# a.bbox

# im = page.to_image(resolution=150)

# im.draw_rect(image_bbox, stroke='red', fill=False)

# im.save('sample.png', fornat='PNG')

