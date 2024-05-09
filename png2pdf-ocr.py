import os
import pytesseract as ta
from PyPDF2 import PdfWriter
import io

merger = PdfWriter()


img_path = "./output_3/book"
# output_path = "./output_2/pdf/lecture.pdf"

config = '--psm 4 -c preserve_interword_spaces=1'
languages = 'kor+eng'
# languages = 'eng'

img_list = os.listdir(img_path)
img_list.sort()
# print(len(img_list))
# print(sorted(img_list))
idx = 0
for img in img_list:
    filename = os.path.join(img_path, img)
    print(filename)
    pdf = ta.image_to_pdf_or_hocr(
        filename, 
        extension='pdf', 
        lang=languages, 
        config=config
        )
    pdf_file_in_memory = io.BytesIO(pdf)
    merger.append(pdf_file_in_memory)
    idx = idx + 1
    print(f"num: {idx}, image: {filename}")

merger.write("그림으로배우는인프라구조.pdf")
print("end!!!!")
merger.close()
# with open(f'{output_path}.pdf', 'w+b') as f:
#     f.write(pdf)

# print(ta.get_languages(config=''))
# print(ta.get_tesseract_version())