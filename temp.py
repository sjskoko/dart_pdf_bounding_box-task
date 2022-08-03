import pickle

with open('sample_img_file\[삼성바이오로직스]사업보고서(2022.03.21)\[삼성바이오로직스]사업보고서(2022.03.21)_text.pickle', 'rb') as fr:
    data = pickle.load(fr)


data[4]