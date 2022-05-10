import aspose.words as aw
import os

# [파일 이름 읽어오기]
path_dir=r'C:\Users\TFG256XG\Documents\GitHub\hwp_bounding_box-task\pdf_file'
out_path_dir=r'C:\Users\TFG256XG\Documents\GitHub\hwp_bounding_box-task\html_file'
file_list=os.listdir(path_dir)
print(file_list)
# Load the PDF file
doc = aw.Document(path_dir + '\\' + file_list[0])

# Save the document as HTML
doc.save(out_path_dir + '\\' + file_list[0][:-4] + '.html')