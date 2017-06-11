from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)
filelist=""
def fld(pre):
	global filelist
	global file_list
	for f in file_list:
		if f['mimeType']=='application/vnd.google-apps.folder': # if folder
			filelist=filelist+"\n"+pre+"/"+str(f['title'])+"/"#,"list":ListFolder(f['id'])})
			file_list=drive.ListFile({'q': "'%s' in parents and trashed=false" % f['id']}).GetList()
			fld(pre+"/"+str(f['title']))
		else:
			filelist=filelist+"\n"+pre+"/"+str(f['title'])
def list():
	global filelist
	global file_list
	filelist=""
	file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
	fld("")
	tmp=""
	for line in filelist.splitlines():
		if line!="":
			if tmp=="":
				tmp=line
			else:
				tmp=tmp+"\n"+line
	filelist=tmp
	print filelist
	return filelist
#file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
#print file_list
print "--------"
#for file1 in file_list:
#	print('title: %s, id: %s' % (file1['title'], file1['id']))
#filelist=""
#file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
#for f in file_list:
#	if f['mimeType']=='application/vnd.google-apps.folder': # if folder
#		filelist=filelist+"\n"+str(f['title'])+"/"#,"list":ListFolder(f['id'])})
#		file_list2=drive.ListFile({'q': "'%s' in parents and trashed=false" % f['id']}).GetList()
#		pre=f['title']
#		for f in file_list2:
#			if f['mimeType']=='application/vnd.google-apps.folder':
#				filelist=filelist+"\n"+str(f['title'])+"/"#,"list":ListFolder(f['id'])})
#				file_list3=drive.ListFile({'q': "'%s' in parents and trashed=false" % f['id']}).GetList()
#				pre2=f['title']
#				for f in file_list3:
#					filelist=filelist+"\n"+pre2+"/"+str(f['title'])
#			else:
#				filelist=filelist+"\n"+pre+"/"+str(f['title'])
#	else:
#		filelist=filelist+"\n"+str(f['title'])
#print filelist
list()
