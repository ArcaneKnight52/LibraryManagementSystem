#usersXbooks #Admin
def Admin(s):
    import mysql.connector as v
    if(s=="ak"):
        con=v.connect(host="localhost",user="root",password="root",database="LibraryOg")
        cur=con.cursor()
        print("--------------------------------------------------------")
        print("MENU:")
        print("1. To see all records of corresponding books and users.")
        print("2. To see all records about users .")
        print("3. To delete table books.")
        print("4. To delete from user.")
        print("5. To delete table user.")
        print("6. To delete database.")
        print("--------------------------------------------------------")
        print("Enter your choice: (at next line)")
        choice=int(input())
        if(choice==1):
            cur.execute("select * from books,user where books.book_id=user.book_id")
            s=cur.fetchall()
            print(s)
        elif(choice==2):
            cur.execute("select * from user")
            p=cur.fetchall()
            print(p)
        elif(choice==3):
            cur.execute("delete  from books")
            con.commit()
            print("deletion succesful !!")
        elif(choice==4):
            key=int(input("Enter uid of  whose record is to be deleted: "))
            cur.execute("select * from user")
            record = cur.fetchall()
            x=False
            try:
                for row in record:
                    if(row[0]==key):
                        x=True
                        cnfm=input("Are you sure to delete this record ? :")
                        if(cnfm.lower() in ("yes","y")):
                            sql="delete from user where uid=%s"
                            val=(key,)
                            cur.execute(sql,val)
                            con.commit()
                        else:
                            pass
                    else:
                        pass
            except EOFError :
                pass
            
            if(x==False):
                print("No such record exists having uid",key)
                print("-----------------------------------------------------------------")
                con.close()
            
            elif(x==True):
                con.close()
                print("Record deleted succesfully!!!")
                print("==================================================================")

        elif(choice==5):
            cur.execute("delete  from user")
            con.commit()
            print("deletion succesful !!")
        elif(choice==6):
            cur.execute("drop database LibraryOg")
            con.commit()
            print("deletion succesful !!")
        
        con.close()
    else:
        print("Contact admin for authorization")
