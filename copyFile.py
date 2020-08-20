import shutil

# copy file from here to there
mySrc = "c:/temp/basic steps.txt.bak"
myDst = "f:/tmp/basic steps.txt-4.bak"

try:
    shutil.copyfile(mySrc, myDst)
except:
    print('Error: copyfile failed')

# copy directory from here to there
mySrcDir = "c:/temp/tmp"
myDstDir = "f:/tmp/tmp"
try:
    shutil.copytree(mySrcDir, myDstDir)
except:
    print('Error: copytree failed')
