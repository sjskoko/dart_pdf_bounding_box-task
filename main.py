import argparse
from dartplumber import Extractor
from util import *

def main(args):

    pdf_extractor = Extractor(args)
    image_result = pdf_extractor.create_bbox_with_img_save()

    return image_result

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Argparse Tutorial')

    parser.add_argument('--table', '-t', action='store_true', default=False)
    parser.add_argument('--image', '-i', action='store_true', default=False)
    parser.add_argument('--caption', '-c', action='store_true', default=False)

    parser.add_argument('--pdf_dir', '-dir', type=str, default='sample_pdf_file')
    parser.add_argument('--save_dir', '-save', type=str, default='img_file')

    args = parser.parse_args()

    main(args)
