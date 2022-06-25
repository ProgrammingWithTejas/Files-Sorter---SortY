import os

def createIfFolderNotExists(folder):
    if not os.path.exists(folder):
        os.mkdir(folder)

def move(filename, folderName):
    for item in filename:
        os.replace(item, f"{folderName}/{item}")
        
createIfFolderNotExists("Images")
createIfFolderNotExists("Videos")
createIfFolderNotExists("Audios")
createIfFolderNotExists("Docs")
createIfFolderNotExists("Others")
createIfFolderNotExists("Apps")

files = os.listdir()
files.remove("main.py")

ImgExts = [".png", ".jpg", ".jpeg", ".gif"]
VidExts = [".mp4", ".mkv", ".mov", ".avi"]
AudioExts = [".mp3", ".wav", ".m4a", ".aac"]
AppExts = [".exe", ".msi"]
DocExts = [".pdf", ".xlsx", ".docx", ".html", ".htm", ".xls", ".ppt", ".pptx", ".txt"]

Images = [file for file in files if os.path.splitext(file)[1].lower() in ImgExts]
Videos = [file for file in files if os.path.splitext(file)[1].lower() in VidExts]
Audio = [file for file in files if os.path.splitext(file)[1].lower() in AudioExts]
Docs = [file for file in files if os.path.splitext(file)[1].lower() in DocExts]
Apps = [file for file in files if os.path.splitext(file)[1].lower() in AppExts]
Others = []

for file in files:
    extSplit = os.path.splitext(file)[1].lower()
    if (extSplit not in ImgExts) and (extSplit not in VidExts) and (extSplit not in AudioExts) and (extSplit not in DocExts) and (extSplit not in AppExts) and os.path.isfile(file):
        Others.append(file)

move("Images", Images)
print(f"{len(Images)} Image Files Were Sorted Successfully!")

move("Videos", Videos)
print(f"{len(Videos)} Video Files Were Sorted Successfully!")

move("Audios", Audio)
print(f"{len(Audio)} Audio Files Were Sorted Successfully!")

move("Docs", Docs)
print(f"{len(Docs)} Documents Were Sorted Successfully!")

move("Apps", Apps)
print(f"{len(Apps)} Apps Were Sorted Successfully!")

move("Others", Others)
print(f"{len(Others)} Other Files Were Sorted Successfully!")

totalFiles = len(Images) + len(Videos) + len(Audio) + len(Docs) + len(Apps) + len(Others)
print(f"\nTotal {totalFiles} Files were sorted successfully!")

exitInp = input('\nPress "Enter" To Exit: ')