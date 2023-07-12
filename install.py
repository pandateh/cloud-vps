import os

WORKING_DIR = "/root/work"
PORTAPPS_DIR = "Apps"
PORTDATA_DIR = "Data"

os.mkdir(os.path.join(WORKING_DIR, PORTAPPS_DIR))
os.mkdir(os.path.join(WORKING_DIR, PORTDATA_DIR))
print("Installation Done."")
