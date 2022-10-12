
#menu programm of  project
def Menu():
    from body import Add, Read_Print, Search, Export, Count, update, Delete
    from auxillary import Book_issual
    while True:
        print("\t\t ||Welcome to Library Management System||  VERSION 1.0")
        print("--------------------------------------------------------")
        print("MENU:")
        print("1. To add details of new book.")
        print("2. To display information about books .")
        print("3. To search a book.")
        print("4. To export book details to a text file.")
        print("5. To count the no. of  records in database.")
        print("6. To update details for a book.")
        print("7. To delete the entry for a book.")
        print("8. To issue a book.")
        print("--------------------------------------------------------")
        print("Enter your choice: (at next line)")
        choice=int(input())
        if(choice==1):
            Add.PCAdd_Bks()
        elif(choice==2):
            Read_Print.Read_Bks()
        elif(choice==3):
            Search.Search_Menu()
        elif(choice==4):
            Export.Export_Menu()
        elif(choice==5):
            Count.count_Bks()
        elif(choice==6):
            update.Update_Bks()
        elif(choice==7):
            Delete.Delete_Bks()
        elif(choice==8):
            Book_issual.Add_user()
        check=input("Do you want to return to main menu? {Yes/No}  : ")
                    
        if(check not in("Y","y","YES","yes","Yes")):
            break

                
                
            
    print("Thank you for your valuable time at Library Management System :-). \nWe hope you have a wonderful day ahead")

        

