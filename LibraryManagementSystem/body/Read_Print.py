#to read bks
def ReadForUser_Bks():
    import mysql.connector as v
    con=v.connect(host="localhost",user="root",password="root",database="LibraryOg")
    cur=con.cursor()
    cur.execute("select * from books")
    record = cur.fetchall()
    try:
        for row in record:
            print("-----------------------------------------------------------------------------")
            print("\t\t || Details of "+row[1]+"||")
            a=row[0]
            b=row[4]
            print("\n"+"=========================================================")
            print("\n"+"book_id : "+str(a)+"\n")
            print("name : "+row[1]+"\n")
            print("author : "+row[2]+"\n")
            print("genre : "+row[3]+"\n")
            print("price : "+str(b)+"\n")
            print("----------------------------------------------------------")
            

    except EOFError:
        pass
    
            
    print("-----------------------------------------------------------------------------")
    con.close()
#========================================================
def ReadForcoAdmin_Bks():
    import mysql.connector as v
    con=v.connect(host="localhost",user="root",password="root",database="LibraryOg")
    cur=con.cursor()
    cur.execute("select * from books")
    record = cur.fetchall()
    try:
        for row in record:
            print(row)
            

    except EOFError:
        pass
    
            
    print("-----------------------------------------------------------------------------")
    con.close()

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def Read_Bks():
    print("Enter the mode of viewing..")
    print("------------------------------")
    print("a.View for user")
    print("b.View for admin")
    p=0
    choice=input("Enter your choice (a/b) : ")
    while(p==0):
        if(choice.lower()=="a"):
            ReadForUser_Bks()
            p+=1
        elif(choice.lower()=="b"):
            ReadForcoAdmin_Bks()
            p+=1
        else:
            print("Please enter correct values!!!!!")
            choice=input("Enter your choice (a/b) : ")
            


