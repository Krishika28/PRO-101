import dropbox

class TransferData:
    def init(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        openFile = open(file_from, 'rb')
        dbx.files_upload(openFile.read(), file_to)

def main():
    access_token = 'sl.AzQyBr2OneqFFekTG5aDpZVHmLUHW2WmyXuTV5QTlZpBPNypGi6L5fO8B9l4B_B-UvhDR-DQx5E-uhNTAZ8fDgG-01lLmYsuU71GbK6gVontTLmPTC-Pvy3ILG_lxMy3X_92I_pOw3uY'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer : -")
    file_to = input("Enter the full path to upload to dropbox:- ")  
    transferData.upload_file(file_from, "/backup_folder/" + file_to)
    print("File has been moved !!!")


main()