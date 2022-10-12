#search

#------------------------------------------------------------------------
#b)search by bookid
def Bid_Bks():
    import mysql.connector as v
    con=v.connect(host="localhost",user="root",password="root",database="LibraryOg")
    cur=con.cursor()
    key=int(input("Enter book_id whose record is to be displayed : "))
                
            
    flag=0
    try:
        cur.execute("select * from books")
        record = cur.fetchall()
        for row in record:
            if(row[0]==key):
                print("RECORD FOUND."+"")
                print("-----------------------------------------------------------------------")
                print("The book having id",key,"is : ",row)
                flag=1
            else:
                pass
                
    except EOFError :
        pass
    if(flag==0):
        print("No such record exists with book_id being",key)
    print("-----------------------------------------------------------------------------")                
    con.close()
#---------------------------------------------
#a)search by name
def NameSearch_Bks():
    import mysql.connector as v
    con=v.connect(host="localhost",user="root",password="root",database="LibraryOg")
    cur=con.cursor()
    key=input("Enter name of the book whose record is to be displayed : ")
                               
    w=key.lower()
    flag=0
    cnt=0
    try:
        cur.execute("select * from books")
        record = cur.fetchall()
        for row in record:
            if(row[1].lower()==w):
                print("RECORD FOUND.")
                print("-----------------------------------------------------------------")
                print("The record of the book",key,"is : ",row)
                flag=1
                cnt+=1
            else:
                pass
                
    except EOFError :
        pass
    if(flag==0):
        print("No such record exists with book name being",key)
        print("-----------------------------------------------------------------------------")
    elif(flag!=0 and cnt>1):
        choice=input("There appears to be multiple records by same name. Would you like to search by admno.?? {yes/no}")
        if(choice in ("Y","y","YES","yes","Yes")):
            Bid_Bks()

    con.close()
#-----------------------------------------------------------------
#menu for search
def Search_Menu():
    print("Enter the mode of searching..")
    print("------------------------------")
    print("a.Search by book_name")
    print("b.Search by book_id")
    choice=input("Enter your choice (a/b) : ")
    k=0
    while(k==0):
        if(choice.lower()=="a"):
            NameSearch_Bks()
            k+=1
        elif(choice.lower()=="b"):
            Bid_Bks()
            k+=1
        elif(choice.lower not in ("a","b")):
            print("Please retry with correct values!!")
            choice=input("Enter your choice (a/b) : ")

