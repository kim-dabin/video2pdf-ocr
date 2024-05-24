import os
import pytesseract as ta
from PyPDF2 import PdfWriter
import io
import uuid


def main():
    merger = PdfWriter()
    # output_filename = "./output_2/pdf/lecture.pdf"
    output_filename = f"./output/{str(uuid.uuid4())}.pdf"
    img_path = "./output/output"

    config = '--psm 4 -c preserve_interword_spaces=1'
    languages = 'kor+eng'

    try:
        img_list = os.listdir(img_path)
        img_list.sort()
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
    
        merger.write(output_filename)
        os.system("rm -rf ./images")
        print(" success ")
    except Exception as e:
        print("image files to PdfWriter: ", e)
    finally:
        merger.close()


if __name__ == "__main__":
    main()