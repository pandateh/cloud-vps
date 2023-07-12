from pathlib import Path
import tarfile

def startInstall():
  print("Installing [exiftool]...")

  tarball = tarfile.open('exiftool/Image-ExifTool-11.92.tar.gz')
  tarball.extractall('/root/work/App/Exiftool')
  tarball.close()

  with open(Path().home() / ".bashrc", "a") as f:
    f.write("\n")
    f.write("alias exiftool='/root/work/App/Exiftool/Image-ExifTool-11.92/exiftool'\n")
    f.write("alias exiftool-clr='/root/work/App/Exiftool/Image-ExifTool-11.92/exiftool -all= -overwrite_original -r'\n")

  print("Installing [exiftool] DONE")
