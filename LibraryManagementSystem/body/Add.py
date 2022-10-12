#to add new book
def Add_Bks():
    """accepts information and adds them into database."""
    import mysql.connector as v
    con=v.connect(host="localhost",user="root",password="root",database="LibraryOg")
    cur=con.cursor()
    pwd=input("Enter the password to authenticate into the database:")
    print("Authenticating....")
    print(".")
    print(".")
    print(".")
    if(pwd=="Mukesh_Bohra" or pwd=="ak"):
        a=input("Enter book id:")
        b=input("Enter name of the book: ")
        c=input("Enter the author of the book: ")
        d=input("Enter genre : ")
        e=input("Enter price of the book : ")
        sql = "INSERT INTO books(book_id,book_name,author,genre,price) VALUES (%s, %s, %s, %s, %s)"
        val=(a,b,c,d,e)
        cur.execute(sql,val)
        con.commit()
        print(cur.rowcount , "record inserted")
        print("Student details added.")
        print("Thank you for your valued contribution!")
          
    else:
        print("Sorry, your password is wrong hence you cannot be authenticated. Contact admin for authorization.")
    con.close()
#=========================================================================
def PCAdd_Bks():
    import mysql.connector as v
    dcon=v.connect(host="localhost",user="root",password="root",database="LibraryOg")
    key=int(input("Enter book_id of whose record is to be confirmed: "))
    flag=0
    cur=dcon.cursor()
    cur.execute("select * from books")
    record = cur.fetchall()
    try:
        for row in record:
            if(row[0]==key):
                flag+=1
                break
            
    except EOFError:
        pass
    if(flag==0):
            Add_Bks()
    else:
        print("There already exists a record with book_id being",key)
        
    print("-----------------------------------------------------------------------------")
    dcon.close

