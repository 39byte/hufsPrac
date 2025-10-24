import os

path = os.getcwd()
files = os.listdir(".")
for file in files:
    print("파일 경로 합치기:", os.path.join(path, file))