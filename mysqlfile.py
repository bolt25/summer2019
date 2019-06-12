import mysql.connector
class database:
	def __init__(self):
		self.con=mysql.connector.connect(host='localhost',user='root',password='your_password_here',database='bitdemo')
	def insert_details(self,roll,name,standard,dob,gender):
		query="insert into student(roll,Name,standard,DoB,Gender)values (%d,'%s','%s','%s','%s')"%(roll,name,standard,dob,gender)
		cr=self.con.cursor()
		cr.execute(query)
		self.con.commit()
	def update_details(self,roll,standard):
		query="update student set standard='%s' where roll=%d"%(standard,roll)
		cr=self.con.cursor()
		cr.execute(query)
		self.con.commit()
	def delete_details(self,roll):
		query="delete from student where roll=%d"%(roll)
		cr=self.con.cursor()
		cr.execute(query)
		self.con.commit()
	def view_details(self):
		query="select * from student"
		cr=self.con.cursor()
		cr.execute(query)
		return cr
	def enter_marks(self,roll,maths,chemistry,physics):
		query="insert into marks(roll,maths,chemistry,physics) values (%d,%d,%d,%d)"%(roll,maths,chemistry,physics)
		cr=self.con.cursor()
		cr.execute(query)
		self.con.commit()
	def view_marks(self):
		query="select * from marks"
		cr=self.con.cursor()
		cr.execute(query)
		return cr
	def join(self):
		query="select s.Name,s.standard,s.Gender,m.physics,m.chemistry,m.maths from student s join marks m on s.roll=m.roll"
		cr=self.con.cursor()
		cr.execute(query)
		return cr
