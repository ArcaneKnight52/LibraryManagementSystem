#to add new book
def Add_user():
    """accepts information and adds them into database."""
    import mysql.connector as v
    con=v.connect(host="localhost",user="root",password="root",database="LibraryOg")
    cur=con.cursor()
    print("MENU:")
    print("1. To issue new books.")
    print("2. To return issued books.")
    print("3. To see what books user has issued.")
    choice=int(input("Enter choice :"))
    if(choice==1):
        k=int(input("Enter uid:"))
        cur.execute("select * from user")
        record = cur.fetchall()
        try:
            for row in record:
                if(row[0]==k):
                    a=int(input("Enter book id which has been issued:"))
                    b=input("Enter date of issue: ")
                    sql1 = "update user set book_id=%s where uid=%s"
                    val1=(a,k)
                    cur.execute(sql1,val1)
                    con.commit()
                    sql2 = "update user set DOI=%s where uid=%s"
                    val2=(b,k)
                    cur.execute(sql2,val2)
                    con.commit()
                    print("updated succesfully!!")
                else:
                    pass
        except EOFError:
            pass
    elif(choice==2):
        k=int(input("Enter uid:"))
        cur.execute("select * from user")
        record = cur.fetchall()
        try:
            for row in record:
                if(row[0]==k):
                    v=int(input("Enter book id which is to be returned:"))
                    c=input("Enter date of return:")
                    sql1 = "update user set book_id=%s where uid=%s"
                    val1=(v,k)
                    cur.execute(sql1,val1)
                    con.commit()
                    sql2 = "update user set DOR=%s where uid=%s"
                    val2=(c,k)
                    cur.execute(sql2,val2)
                    con.commit()
                    print("updated succesfully!!")
                else:
                    pass
        except EOFError:
            pass
    elif(choice==3):
        d=input("Enter user id of the person of whom u wish to see the book issue:")
        sql="select %s,user.book_id,username,book_name,price from books,user where books.book_id=user.book_id"
        val=(d,)
        cur.execute(sql,val)
        k=cur.fetchone()
        print(k)
          
    
    con.close()

