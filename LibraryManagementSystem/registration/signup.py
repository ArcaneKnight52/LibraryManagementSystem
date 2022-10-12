#sign up
def SignUp():
     import mysql.connector as v, random
     from registration import signin
     con=v.connect(host="localhost",user="root",password="root",database="LibraryOg")
     cur=con.cursor()
     print("Are you")
     print("A.new user")
     print("b.Registered user")
     choice=input("Enter your choice (a/b) : ")
     if(choice.lower()=="a"):
          print("**********************************************************")
          print("\t\t ||REGISTRATION FORUM||")
          print("=======================================================")
          fn=input("Enter your first name : ")
          l=input("Enter your last name : ")
          email=input("Enter your email : ")
          d=input("Enter DOB : ")
          r=str(random.randint(100,999))
          uid=random.randint(0,9999)
          u=fn+r
          print(u,"This will be used as your username")
          p=input("Create strong password : ")
          cp=input("Confirm password : ")
          if(p!=cp):
               print("Password did not match")
               print("try again")
          else:
               print("Congrats")
               print("Registration Succesful!!")
               
          sql="insert into user(uid,username,email_id,user_pwd) vAlues(%s,%s,%s,%s)"
          val=(uid,u,email,cp)
          cur.execute(sql,val)
          con.commit()
     elif(choice.lower()=="b"):
          signin.SignIn()
     else:
          print("Invalid choice!!")
     con.close()
                             
     
