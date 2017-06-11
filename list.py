import os
pre=os.getcwd()+"/"
for path, subdirs, files in os.walk(os.getcwd()):
	for name in files:
		print os.path.join(path, name).replace(pre,"")
