import os
from pathlib import Path
from alist import PandaAlist
from exiftool import PandaExiftool

# ALIAS_INDICATOR_STR = "# Panda CLOUD_VPS Custom Aliases"
WORKING_DIR = "/root/work"
PORTAPPS_DIR = "Apps"
PORTDATA_DIR = "Data"
# VPSCLOUD_ALIAS_DIR = "vpscloud_bash_aliases"

Path(os.path.join(WORKING_DIR, PORTAPPS_DIR)).mkdir(parents=True, exist_ok=True)
Path(os.path.join(WORKING_DIR, PORTDATA_DIR)).mkdir(parents=True, exist_ok=True)
# Path(os.path.join(WORKING_DIR, VPSCLOUD_ALIAS_DIR)).mkdir(parents=True, exist_ok=True)

# isCloudAliasesRegistered = True;
# with open(Path().home() / ".bashrc", "r") as f:
#     bashrcContent = f.read()
#     if bashrcContent.find(ALIAS_INDICATOR_STR) < 0:
#       isCloudAliasesRegistered = False
# if not isCloudAliasesRegistered:
#   with open(Path().home() / ".bashrc", "a") as f:
#     f.write("\n")
#     f.write(ALIAS_INDICATOR_STR + "\n")
#     f.write("if [ -d $HOME/work/" + VPSCLOUD_ALIAS_DIR + " ]; then\n")
#     f.write("\tfor f in $HOME/work/" + VPSCLOUD_ALIAS_DIR + "/*; do\n")
#     f.write("\t\t. \"$f\";\n")
#     f.write("\tdone\n")
#     f.write("fi\n")

PandaExiftool.startInstall()
PandaAlist.startInstall()

print("Installation Done.")

# Reload the BASH at the end of installation
os.system("exec bash")
