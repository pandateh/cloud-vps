import os
from pathlib import Path
from exiftool import PandaExiftool

WORKING_DIR = "/root/work"
PORTAPPS_DIR = "Apps"
PORTDATA_DIR = "Data"

#Path(os.path.join(WORKING_DIR, PORTAPPS_DIR)).mkdir(parents=True, exist_ok=True)
#Path(os.path.join(WORKING_DIR, PORTDATA_DIR)).mkdir(parents=True, exist_ok=True)
PandaExiftool.startInstall()

print("Installation Done.")
