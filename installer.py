import os
import sys
from subprocess import run

for file in os.listdir(sys.argv[1]+"/"):
	print(sys.argv[1]+"/"+file)
	command = "ampy --port "+ sys.argv[2] +" put "+ sys.argv[1]+"/"+file
	os.system(command)
