from PIL import Image
import os

# 변환 함수 정의
def convert_to_jpg(file_path):
    # 이미지 열기
    image = Image.open(file_path)

    # 파일 확장자 변경
    new_file_path = os.path.splitext(file_path)[0] + ".jpg"

    # JPG로 저장
    image.save(new_file_path, "JPEG")
    image.close()

    # 원본 파일 삭제
    os.remove(file_path)

# 디렉토리 탐색
def convert_images_in_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            print(file_path)
            file_ext = os.path.splitext(file_path)[1].lower()
            if file_ext == ".bmp" or file_ext == ".wmf":
                try:
                    convert_to_jpg(file_path)
                    print(f"변환 완료: {file_path}")
                except Exception as e:
                    print(f"변환 실패: {file_path}\n에러 메시지: {str(e)}")

# 변환할 디렉토리 지정
directory = "./"

# 변환 실행
convert_images_in_directory(directory)
print("tyest")