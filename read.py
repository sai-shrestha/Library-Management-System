def read_():
    print("--------------------------------------------------------------------")
    print("BookID   Book name        Author           Quantity         Price       ")
    print("--------------------------------------------------------------------")
    file=open("books.txt","r")
    a=1

    for line in file:
        print("  ",a,"\t"+line.replace(",","\t"))
        a=a+1
        print("--------------------------------------------------------------------")




