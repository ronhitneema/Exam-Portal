#!C:/Python27/python.exe
print "Content-type:text/html"
print ""


fp=open("header.py","r")
print fp.read()
fp.close()


fp=open("loginnav.py","r")
print fp.read()
fp.close()


import cgi,mysql.connector

form=cgi.FieldStorage()
exam_id=form.getvalue("exam_id")

db=mysql.connector.connect(user="root",password="",host="localhost",database="exam_schedule")
cursor=db.cursor()

query="select * from e_info where exam_id='%s'" %(exam_id)
cursor.execute(query)
data=cursor.fetchone()


print """

            <div id="content">
			
			<center>
			<br/>
			<h1>Exam Schedule</h1>
			<table border="2" cellspacing="5" cellpadding="10">
			 <tr>
			  <th>Exam ID</th>
			  <th>Exam Venu</th>
			  <th>Exam Date</th>
			  <th>Exam Time</th>
			 </tr>
"""

print "<tr>"

print "<td>",data[0],"</td>"
print "<td>",data[1],"</td>"
print "<td>",data[2],"</td>"
print "<td>",data[3],"</td>"

print "</tr>"

print """			
			
			</table>
			</center>
            
            </div>

"""

fp=open("footer.py","r")
print fp.read()
fp.close()





if s!=None:
	sname=form.getvalue("sname")
	sid=form.getvalue("sid")
	
	
	if len(data)>0:
		print "<script>alert('Login successfully...')</script>"
		print "<script>window.location='exam_info.py?exam_id="+str(data[1])+"'</script>"
        




















