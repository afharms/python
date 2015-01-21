# example-ftp.py

import ftplib

ftp = ftplib.FTP('ftp.cornerbakerycafe.com')
ftp.login('xpient','Sheesfes52')
ftp.cwd('/Misc')

remotefile = 'Delta Build 1207 Release.docx'
outfile = 'c:\\install\\' + remotefile

#with open(outfile, 'wb') as file:
#    ftp.retrbinary("RETR " + remotefile, file.write)

ftp.quit()
