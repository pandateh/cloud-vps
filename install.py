import os
from pathlib import Path

Path("/my/directory").mkdir(parents=True, exist_ok=True)

WORKING_DIR = "/root/work"
PORTAPPS_DIR = "Apps"
PORTDATA_DIR = "Data"

Path(os.path.join(WORKING_DIR, PORTAPPS_DIR)).mkdir(parents=True, exist_ok=True)
Path(os.path.join(WORKING_DIR, PORTDATA_DIR)).mkdir(parents=True, exist_ok=True)

print("Installation Done.")
