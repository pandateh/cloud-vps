import os
from pathlib import Path
import tarfile

ALIAS_IND_STR = "# PANDA_CLOUD_VPS - Exiftool Aliases (AUTO GENERATED)"

def registerAliases():
  isExiftoolAliasesRegistered = True;
  with open(Path().home() / ".bashrc", "r") as f:
    bashrcContent = f.read()
    if bashrcContent.find(ALIAS_IND_STR) < 0:
      isExiftoolAliasesRegistered = False

  if not isExiftoolAliasesRegistered:
    with open(Path().home() / ".bashrc", "a") as f:
      f.write("\n")
      f.write(ALIAS_IND_STR + "\n")
      f.write("alias exiftool='/root/work/Apps/Exiftool/Image-ExifTool-11.92/exiftool'\n")
      f.write("alias exiftool-clr='/root/work/Apps/Exiftool/Image-ExifTool-11.92/exiftool -all= -overwrite_original -r'\n")

def startInstall():
  print("Installing [exiftool]...")

  tarball = tarfile.open('exiftool/Image-ExifTool-11.92.tar.gz')
  tarball.extractall('/root/work/Apps/Exiftool')
  tarball.close()

  registerAliases()

  print("Installing [exiftool] DONE")
