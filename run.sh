#!/bin/bash
IMAGE_PATH = "./images"

# .mp4 파일을 이미지 슬라이스로 변경
python video2pdfslides.py ./input/output.mp4

if [ -e  $IMAGE_PATH ]; then
    # 슬라이스 이미지들을 pdf로 변환
    python png2pdf-ocr.py
fi

