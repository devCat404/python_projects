import os

# 📌 원하는 디렉토리 설정 (절대 경로)
target_dir = r"url here"

# 디렉토리 생성 (이미 존재하면 무시)
os.makedirs(target_dir, exist_ok=True)

# N개 파일 생성
for i in range(1, (N+1)):
    file_path = os.path.join(target_dir, f"filename.extend_name")
    with open(file_path, "w") as f:
        f.write(f"""
    
                
              >>  wrtie here

""")

print(f"파일이 '{target_dir}'에 생성되었습니다.")