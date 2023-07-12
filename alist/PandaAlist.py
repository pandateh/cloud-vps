import os
from pathlib import Path
import tarfile

def startInstall():
  print("Installing [alist]...")

  tarball = tarfile.open('alist/alist-linux-amd64.tar.gz')
  tarball.extractall('/root/work/Apps/AList')
  tarball.close()

  print("Installing [alist] DONE")
