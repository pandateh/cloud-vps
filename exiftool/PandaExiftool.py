import tarfile

def startInstall():
  print("Installing [exiftool]...")
  file = tarfile.open('exiftool/Image-ExifTool-11.92.tar.gz')
  file.extractall('/root/work/App/Exiftool')
  file.close()
  print("Installing [exiftool] DONE")
