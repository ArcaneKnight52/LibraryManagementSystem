#count:
def count_Bks():
    import mysql.connector as v
    con=v.connect(host="localhost",user="root",password="root",database="LibraryOG")
    cur=con.cursor()
    cnt=0
    cur.execute("select * from books")
    record = cur.fetchall()
    try:
        for row in record:
            cnt+=1
    except EOFError:
        pass
    print("The number of records are : ",cnt)
    con.close()
