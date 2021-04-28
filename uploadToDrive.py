import os
from Google import Create_Service
from googleapiclient.http import MediaFileUpload

# CREATE SERVICE
CLIENT_SECRET_FILE = 'client_secret.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

# UPLOAD CSV FILE TO GOOGLE DRIVE
def export_csv(file_path: str, parents: list=None):
    if not os.path.exists(file_path):
        print(f"{file_path} not found")
        return
    try:
        file_metadata = {
            'name': os.path.basename(file_path).replace('.csv', " "),
            'mimeType': "application/vnd.google-apps.spreadsheet",
            'parents': parents
        }

        media = MediaFileUpload(filename=file_path, mimetype='text/csv')

        response = service.files().create(
            media_body =media,
            body =file_metadata,
        ).execute()

        print(response)
        return response
    
    except Exception as e:
        print(e)
        return

# UPLOAD THE CSV FILES IN DIRECTORY
csv_files = os.listdir("upload")

for csv_file in csv_files:
    print(f"uploading {csv_file} now...")
    export_csv(os.path.join('upload', csv_file))
print("drive upload completed")