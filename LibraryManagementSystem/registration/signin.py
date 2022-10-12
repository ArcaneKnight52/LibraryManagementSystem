#signup
def SignIn():
    import mysql.connector as v
    from auxillary import Menu
    con=v.connect(host="localhost",user="root",password="root",database="LibraryOg")
    cur=con.cursor()
    um=input("Enter username : ")
    p=input("Enter password : ")
    flag=0
    cur.execute("select * from user")
    record = cur.fetchall()
    try:
        for row in record:
            if(um==row[1] and p==row[3]):
                print("Sign In Succesful!!")
                print("Opening main page...")
                Menu.Menu()
                flag=1
            else:
                pass
    except EOFError :
        pass
    if(flag==0):
        print("Invalid Credentials")
    
    con.close()   
