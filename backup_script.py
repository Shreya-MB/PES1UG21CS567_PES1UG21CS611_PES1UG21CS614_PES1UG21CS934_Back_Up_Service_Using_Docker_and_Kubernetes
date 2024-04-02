import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# Define the scopes needed for authorization
SCOPES = ['https://www.googleapis.com/auth/drive']

def authenticate():
    """Authenticate and return the Drive service."""
    # Load credentials from the token file or create new ones if not available
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file(
            "client_secret_327876089488-pgm04er5f267f131h2kn6uj15a8qfb8v.apps.googleusercontent.com.json", SCOPES
        )
        creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    # Return the Drive service
    return build('drive', 'v3', credentials=creds)

def upload_file(drive_service, file_path, folder_id=None):
    """Upload a file to Google Drive."""
    file_name = os.path.basename(file_path)
    file_metadata = {'name': file_name}
    if folder_id:
        file_metadata['parents'] = [folder_id]

    media = MediaFileUpload(file_path, resumable=True)
    file = drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    print(f'File uploaded: {file_name} (ID: {file.get("id")})')

def main():
    # Authenticate with Google Drive
    drive_service = authenticate()

    # Path to the file you want to upload
    file_path = 'J_PES1UG21CS567_SHREYA_M_B_E1.pdf'

    # Optional: ID of the folder in Google Drive where you want to upload the file
    # folder_id = 'your_folder_id'
    
    # Upload the file
    upload_file(drive_service, file_path)

if __name__ == "__main__":
    main()
