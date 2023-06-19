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
   		<br/><br/>
             <form method="post">
             <table cellspacing="3"cellpadding="6">
             <td align="center" colspan="2">
             <h2>Faculty Login here!!!</h2>
             </td>
             <tr>
             <td class="frmlbl">Name</td>
             <td><input name="fname" class="frmfld" type="text" placeholder="Enter Faculty Name"/></td>
             </tr>
              <tr>
             <td class="frmlbl">Faculty ID</td>
             <td><input name="fid" class="frmfld" type="text" placeholder="Enter Faculty ID"/></td>
             </tr>
              <tr>
             <td colspan="2">
             <input type="checkbox"/>
             Remember me?
             </td>
             </tr>
             
              <tr>
             <td colspan="2">
             <input type="submit" id="frmbtn" name="s" value="Submit"/>
			<!-- <button name="s" id="frmbtn" type="submit">Submit</button>-->
             
             </td>
             </tr>
             </table>
             </form>
         </center> 
		  </div>

"""

fp=open("footer.py","r")
print fp.read()
fp.close()


import cgi,mysql.connector

form=cgi.FieldStorage()
s=form.getvalue("s")

db=mysql.connector.connect(user="root",password="",host="localhost",database="exam_schedule")
cursor=db.cursor()


if s!=None:
	fname=form.getvalue("fname")
	fid=form.getvalue("fid")
	
	query="select * from faculty where faculty_id='%s'" %(fid)
	cursor.execute(query)
	data=cursor.fetchone()
	if len(data)>0:
		print "<script>alert('Login successfully...')</script>"
		print "<script>window.location='faculty_info.py?exam_id="+str(data[1])+"'</script>"
        




















