import dropbox
class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token
    def uploadFile(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)
        f=open(file_from,'rb')
        dbx.files_upload(f.read(),file_to)

def main():
    access_token='sl.ArUcKxZP9zlH0EmTsGnc1B_vE5I_O2ut1R36oZRhn8cN2wzOBg5WSciB0xcVP2yVSMoBSlXmezKtJKturhB-gMaYG-lpzYPeg9hJTrWP5arXibAcNEBDoaZSmDK1sZwObvHM-2A'
    TransferData1=TransferData(access_token)
    file_from=input("Enter the file path to transfer")
    file_to=input("Enter the file path to upload to dropbox")
    TransferData1.uploadFile(file_from,file_to)
    print("File has been moved")

main()