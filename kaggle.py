import zipfile
import os
import pandas as pd

# In the Terminal Window, enter the following commands
# 1. mkdir ~/.kaggle
# 2. cp kaggle.json ~/.kaggle/kaggle.json
# 3. chmod 600 ~/.kaggle/kaggle.json
# 3. For the current project - chmod 600 /home/sid/kaggle-titanic_spaceship/kaggle.json
# 4. Copy the API key from the Kaggle DATASET by clicking on the three dots

class Kaggle:

    def __init__(self, API_command):
        os.system(API_command)
        self.name = API_command.split('/')
        self.Open()
        os.remove(self.name[1] + ".zip")


    def Open(self):
        self.dataset = []
        with zipfile.ZipFile(self.name[1] + ".zip", "r") as zip:
            filenames = zip.namelist()
            zip.extractall()
        for _ in filenames:
            self.dataset.append(pd.read_csv(_))

        self.filenames = filenames