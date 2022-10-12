#delete
def Delete_Bks() :
    "to delete a record"
    import mysql.connector as v
    pwd=input("Enter pwd to authenticate:")
    print("Authenticating....")
    print(".")
    print(".")
    print(".")
    if(pwd=="Mukesh_Bohra" or pwd=="ak"):
        key=int(input("Enter book_id of  whose record is to be deleted: "))
        print("=====================================================================")
        con=v.connect(host="localhost",user="root",password="root",database="LibraryOg")
        cur=con.cursor()
        cur.execute("select * from books")
        record = cur.fetchall()
        x=o=False
        try:
            for row in record:
                if(row[0]==key):
                    o=True
                    cnfm=input("Are you sure to delete this record ? :")
                    if(cnfm.lower() in ("yes","y")):
                        sql="delete from books where book_id=%s"
                        val=(key,)
                        cur.execute(sql,val)
                        con.commit()
                        x=True
                    else:
                        break
                else:
                    pass
        except EOFError :
            pass
        
        if(o==False):
            print("No such record exists having book_id",key)
            print("-----------------------------------------------------------------")
            con.close()
        
        elif(x==True):
            con.close()
            print("Record deleted succesfully!!!")
            print("==================================================================")
    else:
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("Not authorized to update the contents of stu_records.To Gain authorization contact admin!!")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

