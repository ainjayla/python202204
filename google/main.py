from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
drive = GoogleDrive(gauth)

list_files = drive.ListFile({'q': "'root' in parents"}).GetList()

for file in list_files:
    if file['title'] == 'alfabeet.txt':
        print(file.GetContentString())
    #print(file['title'])
