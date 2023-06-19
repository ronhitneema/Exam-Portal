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
             <div id="content1">
             <span id="new">Latest News</span>
             <img src="image/new.gif" height="30" width="50"/>
             <marquee direction="up" height="290">
             <ul id="newsli"> 
             <li>latest product is to be released on 10/10/2017</li>
             <br/>
             <li>latest product is to be released on 10/10/2017</li>
             <br/>
             <li>latest product is to be released on 10/10/2017</li>
             <br/>
             <li>latest product is to be released on 10/10/2017</li>              
             <ul>
             </marquee>
             </div>
             <div id="content2">
             <h1>Home page</h1>
             </div>
             <div id="content3">
             <br/><br/>
             <form method="post">
             <table cellspacing="3"cellpadding="6">
             <td align="center" colspan="2">
             <h2>Student Login here!!!</h2>
             </td>
             <tr>
             <td class="frmlbl">Name</td>
             <td><input name="sname" class="frmfld" type="text" placeholder="Enter Student Name"/></td>
             </tr>
              <tr>
             <td class="frmlbl">Student ID</td>
             <td><input name="sid" class="frmfld" type="text" placeholder="Enter Student ID"/></td>
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
             </div>
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
	sname=form.getvalue("sname")
	sid=form.getvalue("sid")
	
	query="select * from exam where student_id='%s'" %(sid)
	cursor.execute(query)
	data=cursor.fetchone()
	if len(data)>0:
		print "<script>alert('Login successfully...')</script>"
		print "<script>window.location='exam_info.py?exam_id="+str(data[1])+"'</script>"
        




















