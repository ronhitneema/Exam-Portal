#!C:/Python27/python.exe
print "Content-type:text/html"
print ""


fp=open("header.py","r")
print fp.read()
fp.close()


fp=open("nav.py","r")
print fp.read()
fp.close()

print """

            <div id="content">
             <center>
			  <h1>Contact page</h1>
			 </center>
            </div>

"""

fp=open("footer.py","r")
print fp.read()
fp.close()