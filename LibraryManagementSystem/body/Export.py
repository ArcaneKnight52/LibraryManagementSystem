#to export
#-----------------------------------------------------------------------
#b)specific records
def ExportSpecific_Bks():
    import mysql.connector as v
    con=v.connect(host="localhost",user="root",password="root",database="LibraryOg")
    cur=con.cursor()
    cur.execute("select * from books")
    record = cur.fetchall()
    fn=open("Export_details.txt","w")
    w=int(input("Enter book_id of  whose record is to be exported : "))
    flag=0
    try:
        for row in record:
            if(row[0]==w): 
                fn.write("\t\t || Details of "+row[1]+"||")
                a=row[0]
                b=row[4]
                fn.write("\n"+"=========================================================")
                fn.write("\n"+"book_id : "+str(a)+"\n")
                fn.write("name : "+row[1]+"\n")
                fn.write("author : "+row[2]+"\n")
                fn.write("genre : "+row[3]+"\n")
                fn.write("price : "+str(b)+"\n")
                fn.write("----------------------------------------------------------")
                flag=1    
            else:
                pass
    except EOFError:
        pass
    if(flag==0):
        print("NO such record having b00k_id",w)
    elif(flag==1):
        print("Record exported succesfully!")
    print("---------------------------------------------------------------------------")
    con.close()
    fn.close()
#---------------------------------------------------------------
#a)export all stu

def ExportAll_Bks():
    import mysql.connector as v
    con=v.connect(host="localhost",user="root",password="root",database="LibraryOg")
    cur=con.cursor()
    cur.execute("select * from books")
    record = cur.fetchall()
    fn=open("exported_stu_details.txt","w")
    flag=0
    fn.write("=========================================================")
    try:
        for row in record:
            fn.write("\t\t || Details of "+row[1]+"||")
            a=row[0]
            b=row[4]
            fn.write("\n"+"=========================================================")
            fn.write("\n"+"book_id : "+str(a)+"\n")
            fn.write("name : "+row[1]+"\n")
            fn.write("author : "+row[2]+"\n")
            fn.write("genre : "+row[3]+"\n")
            fn.write("price : "+str(b)+"\n")
            fn.write("----------------------------------------------------------")
            flag=1    
    except EOFError:
        pass
    if(flag==1):
        print("Succesfully exported details of all records.")
        print("The records  has been exported to file: exported_stu_details")
    else:
        print("Export coudn't be completed due to server issues!!")
        print("Pls try again later!!")
    con.close()
    fn.close()

#-------------------------------------------------------

#Export menu
def Export_Menu():
    print("Enter the mode of exporting..")
    print("------------------------------")
    print("a.export all details")
    print("b.export details of specific Book")
    choice=input("Enter your choice (a/b) : ")
    k=0
    while(k==0):
        if(choice.lower()=="a"):
            ExportAll_Bks()
            k+=1
        elif(choice.lower()=="b"):
            ExportSpecific_Bks()
            k+=1
        elif(choice.lower() not in ("a","b")):
            print("Please retry with correct values!!")
            choice=input("Enter your choice (a/b) : ")


              
