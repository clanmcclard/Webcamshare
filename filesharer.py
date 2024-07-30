from filestack import Client

class Filesharer:
    def __init__(self, filepath, api_key="AgMV4aLUGTR2ckOgyZnnxz"):
        self.filepath = filepath
        self.API_KEY = api_key

    def share(self):
        client = Client(self.API_KEY)
        new_file_link = client.upload(filepath=self.filepath)
        return new_file_link.url