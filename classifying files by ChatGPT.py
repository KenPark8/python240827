import os
import shutil

# 다운로드 폴더 경로
download_folder = r'C:\Users\student\Downloads'

# 이동할 폴더 경로 설정
image_folder = r'C:\Users\student\Downloads\images'
data_folder = r'C:\Users\student\Downloads\data'
docs_folder = r'C:\Users\student\Downloads\docs'
archive_folder = r'C:\Users\student\Downloads\archive'

# 폴더가 없으면 생성
os.makedirs(image_folder, exist_ok=True)
os.makedirs(data_folder, exist_ok=True)
os.makedirs(docs_folder, exist_ok=True)
os.makedirs(archive_folder, exist_ok=True)

# 파일 이동 함수
def move_files(extension_list, destination_folder):
    for filename in os.listdir(download_folder):
        if any(filename.lower().endswith(ext) for ext in extension_list):
            src_path = os.path.join(download_folder, filename)
            dest_path = os.path.join(destination_folder, filename)
            shutil.move(src_path, dest_path)
            print(f"Moved: {filename} to {destination_folder}")

# 이미지 파일 이동 (.jpg, .jpeg)
move_files(['.jpg', '.jpeg'], image_folder)

# 데이터 파일 이동 (.csv, .xlsx)
move_files(['.csv', '.xlsx'], data_folder)

# 문서 파일 이동 (.txt, .doc, .pdf)
move_files(['.txt', '.doc', '.pdf'], docs_folder)

# 압축 파일 이동 (.zip)
move_files(['.zip'], archive_folder)
