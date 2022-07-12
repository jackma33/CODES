import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


def gdrive_upload():
    CF = os.getcwd()
    os.chdir(CF + "/Drive")

    gauth = GoogleAuth()
    drive = GoogleDrive(gauth)

    team_drive_id = "0ANvhWNu2X8WLUk9PVA"
    folder_id = "1RaVVP4hPXWpQaWItMiEeotfgY8r9QibS"

    try:
        directory = os.getcwd() + "/Py_Drive_Upload"
        for f in os.listdir(directory):
            filename = os.path.join(directory, f)
            gfile = drive.CreateFile({
                'title':
                f,
                'parents': [{
                    'teamDriveId': team_drive_id,
                    'id': folder_id
                }]
            })
            gfile.SetContentFile(filename)
            gfile.Upload(param={'supportsTeamDrives': True})

            try:
                os.remove(filename)
            except:
                pass
    except Exception as e:
        with open("ERRORS", 'a+') as f:
            f.write(str(e))

    os.chdir(CF)


if __name__ == '__main__':
    gdrive_upload()
