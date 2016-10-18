#!C:\Users\Rohan\AppData\Local\Programs\Python\Python35\python.exe

import cgi, os
# import cgitb; cgitb.enable()

form = cgi.FieldStorage()

# Get filename here.
fileitem = form['file']

# Test if the file was uploaded
if fileitem.filename:
   # strip leading path from file name to avoid
   # directory traversal attacks
   fn = os.path.basename(fileitem.filename)
   # fn = os.path.basename(fileitem.filename.replace("\\", "/" ))
   open( fn, 'wb').write(fileitem.file.read())

   message = 'The file "' + fn + '" was uploaded successfully' 

else:
   message = 'No file was uploaded'

print ("""\
Content-Type: text/html\n
<html>
<body>
   <p>%s</p>
</body>
</html>
""" % (message,))
