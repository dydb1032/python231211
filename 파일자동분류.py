import os
import shutil

# 다운로드 경로 설정
download_path = 'C:\\Users\\student\\Downloads'

# 이미지 파일들을 이동할 폴더
image_folder = 'C:\\Users\\student\\Downloads\\images'
if not os.path.exists(image_folder):
    os.makedirs(image_folder)

# PDF, xlsx, csv, txt 파일들을 이동할 폴더
dataset_folder = 'C:\\Users\\student\\Downloads\\datasets'
if not os.path.exists(dataset_folder):
    os.makedirs(dataset_folder)

# 다운로드 폴더 내 파일들 가져오기
files = os.listdir(download_path)

for file in files:
    file_path = os.path.join(download_path, file)
    if os.path.isfile(file_path):
        # 이미지 파일 체크 (확장자로)
        if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            shutil.move(file_path, image_folder)
            print(f"{file}을(를) images 폴더로 이동했습니다.")
        # PDF, xlsx, csv, txt 파일 체크 (확장자로)
        elif file.lower().endswith(('.pdf', '.xlsx', '.csv', '.txt')):
            shutil.move(file_path, dataset_folder)
            print(f"{file}을(를) datasets 폴더로 이동했습니다.")
        else:
            print(f"{file}은(는) 처리하지 않은 파일 형식입니다.")

