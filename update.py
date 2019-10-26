import urllib,urllib2,sys,platform,os
class bcolors:
	HEADER = '\033[95m'
	OKGREEN = '\033[92m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
PyGDrive=open("pygdrive","r")
code=PyGDrive.read()
PyGDrive.close()
ln=1
for line in code.splitlines():
	if ln==11:
		line=line.replace(" ","").replace("#","").replace("v","")
		av=line
		break
	else:
		ln=ln+1
vl="https://raw.githubusercontent.com/Bytezz/PyGDrive/master/version.html"
print "Connecting..."
try:
	urllib2.urlopen(vl)
	print "Success."
	site=urllib.urlopen(vl)
	page=site.read()
	page=page.replace(" ","\n").replace("<","\n").replace(">","\n")
	for line in page.splitlines():
		if "." in line:
			print "Actual version:",bcolors.BOLD+bcolors.OKGREEN+line+bcolors.ENDC
			if line==av:
				print "Your version:",bcolors.BOLD+bcolors.OKGREEN+av
				print "Your software is at the latest version."+bcolors.ENDC
			else:
				print "Your version:",bcolors.BOLD+bcolors.FAIL+av+bcolors.ENDC
				while True:
					up=raw_input("Update? [y or n]: ")
					if up=="y" or up=="yes":
						if platform.system()=="Linux":
							try:
								print "Update..."
								os.system("git clone https://github.com/Bytezz/PyGDrive temp && cd temp/ && mv ../temp/* .. && rm -rf ../temp && make reinstall")
								print "(If reinstall not completed, type:)"
								print "sudo make reinstall"
								print "Completed."
							except:
								print "Git not installed."
								print "Go here for download:"
								print "https://github.com/Bytezz/PyGDrive"
							sys.exit()
						else:
							print "Go here for download:"
							print "https://github.com/Bytezz/PyGDrive"
							sys.exit()
					elif up=="n" or "no":
						print "Don't update."
						sys.exit()
					else:
						print "Error. Retry."
except urllib2.HTTPError, e:
	print "Error:"
	print(e.code)
except urllib2.URLError, e:
	print bcolors.FAIL+bcolors.BOLD+"Error:"+bcolors.ENDC
	print(e.args)
