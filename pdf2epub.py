import fitz  # PyMuPDF
import subprocess
import os
import io

# PDF에서 텍스트 추출
def extract_text_from_pdf(pdf_path):
    text = ""
    images = []
    doc = fitz.open(pdf_path)
    for page in doc:
        text += page.get_text()
        images += page.get_images()  # 페이지의 이미지를 가져옴
    return text, images

# PDF를 EPUB으로 변환
def convert_pdf_to_epub(pdf_path, epub_path):
    # PDF에서 텍스트와 이미지 추출
    text, images = extract_text_from_pdf(pdf_path)
    
    # 텍스트를 임시 파일에 저장
    for img in images:
        img.show()
        # with open("temp.xhtml", "w", encoding="utf-8") as file:
        #     file.write(img)
    
    # # 이미지를 EPUB 디렉토리에 복사
    # image_dir = "images"
    # os.makedirs(image_dir, exist_ok=True)
    # for index, img in enumerate(images):
    #     image_ext = "jpg"  # 기본적으로 jpg로 설정
    #     image_name = os.path.join(image_dir, f"image_{index}.{image_ext}")
    #     image_data = img[0]
    #     if not isinstance(image_data, bytes):
    #       # 이미지 데이터가 bytes 형식이 아닌 경우 변환
    #       print(img)
    #       image_data = io.BytesIO(image_data)
       
    #     with open(image_name, "wb") as image_file:
    #         image_file.write(image_data)  # 튜플의 첫 번째 요소만 사용
    
    # # XHTML 파일을 EPUB으로 변환
    # subprocess.run(["ebook-convert", "temp.xhtml", epub_path])

    # # 임시 파일 제거
    # subprocess.run(["rm", "temp.xhtml"])

# 실행
if __name__ == "__main__":
    pdf_path = "documents/merged-pdf.pdf"
    epub_path = "output.epub"
    convert_pdf_to_epub(pdf_path, epub_path)