#=====================================================================================                   
#update
def Update_Bks() :
    import mysql.connector as v
    pwd=input("Enter pwd to authenticate:")
    print("Authenticating....")
    print(".")
    print(".")
    print(".")
    if(pwd=="Mukesh_Bohra" or pwd=="ak"):
        key=int(input("Enter book_id of  whose record is to be updated : "))
        print("=====================================================================")
        con=v.connect(host="localhost",user="root",password="root",database="LibraryOg")
        cur=con.cursor()
        x=False
        try:
            cur.execute("select * from books")
            record = cur.fetchall()
            for row in record:
                if(row[0]==key):
                    choice=input("Enter  what values is to be updated:")
                    x=True
                    if(choice.lower()=="book_id"):
                        a=input("Enter new book_id: "+" ")
                        sql="update books set book_id=%s where book_id=%s"
                        val=(a,key)
                        cur.execute(sql,val)
                        con.commit()
                    elif(choice.lower()=="book_name"):
                        b=input("Enter new book_name: "+" ")
                        sql="update books set book_name=%s where book_id=%s"
                        val=(b,key)
                        cur.execute(sql,val)
                        con.commit()
                    elif(choice.lower()=="author"):
                        c=input("Enter new author: "+" ")
                        sql="update books set author=%s where book_id=%s"
                        val=(c,key)
                        cur.execute(sql,val)
                        con.commit()
                    elif(choice.lower()=="genre"):
                        d=input("Enter new genre: "+" ")
                        sql="update books set genre=%s where book_id=%s"
                        val=(d,key)
                        cur.execute(sql,val)
                        con.commit()
                    elif(choice.lower()=="price"):
                        e=input("Enter new price: "+" ")
                        sql="update books set price=%s where book_id=%s"
                        val=(e,key)
                        cur.execute(sql,val)
                        con.commit()
                    else:
                        print("Pls enter correct column values!!")
                        
                    
                else:
                    pass
        except EOFError :
            pass
        
        if(x==False):
            print("No such record exists having Book_Id",key)
            print("=================================================================")
            con.close()
        elif(x==True):
            con.close()
            print("Updated succesfully!!!")
    else:
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("Not authorized to update the contents of Library_Database.To Gain authorization contact admin!!")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

