import os
import sys
from subprocess import run
from os import walk as walk

#Arguments -> python3 installer.py SRC_FOLDER COM-PORT


if(len(sys.argv)<3):
	print("Missing Arguments: python3 installer.py SRC_FOLDER COM-PORT\nExample: python3 installer.py ~/Documents/uPyRest/src /dev/ttyUSB1")
	exit()

fileList = []

for (root,dirnames,filenames) in walk(sys.argv[1]):
	print("!!ROOT!"+root)
	for g in os.listdir(root):
		if(os.path.isdir(g) == False):
			print(root+"/"+g)
			fileList.append(root+"/"+g)
#Remove files...
for fname in fileList:
	command = "ampy --port "+ sys.argv[2] +" rm " + fname.replace("src/","/")
	print(command)
	os.system(command)

#Add files...
for fname in fileList:
	command = "ampy --port "+ sys.argv[2] +" put " + fname + " " + fname.replace("src/","/")
	print(command)
	os.system(command)

command = "ampy --port "+ sys.argv[2] +" ls "
print("LIST FILES: \n\n"+command)
os.system(command)

#Start Putty
command = "putty -serial "+sys.argv[2]+" -sercfg 115200,R"
print("\n\nConnecting via Putty: \n\n"+command)
os.system(command)
 
