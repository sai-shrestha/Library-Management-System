from read import read_
from dict import dic_
import datetime


x={}
y=dic_(x)
d=y.copy()
def main():
    menu_()
    
def dateTime_(dateNtime):
    todaysDate=datetime.date.today()
    now=datetime.datetime.now()
    currentTime=now.strftime("%Y-%M-%D %H:%M:%S")
    return currentTime
def morebooks():
    sa=input("Do you want to borrow more books [y/n]: ")
    if sa=='y' or sa=='Y' :
        borrowbooks()
     
    elif sa=='n' or sa=='N' :
        print("Thank you. ")
    else:
        print("PLease enter a valid option.")
        morebooks()

def nameValidity(user_name):
    if user_name.isalpha():
        return user_name
    else:
        print("Please write a proper name.")
        return askname_()
def askname_():
    f_name=input("Enter your first name:")
    l_name=input("Enter your last name:")
    fvalid=nameValidity(f_name)
    lvalid=nameValidity(l_name)
    full_name=fvalid+(" ")+lvalid
    return full_name
def borrowbooks():
    time=0
    
    nameofborrower=[]
    
    bookID=int(input("Enter the bookID : "))
    if bookID in d.keys():
        print("The book is available. Please fill out the information below.")
                 
        name=askname_()
        quant=int(input("Enter the quantity of the books : "))
        if quant<=int(d[bookID][2]) and quant!=0:
            print("Name :",name,"\n The book you have borrowed:",d[bookID][0],"\n Date and Time:",dateTime_(time))
            price=quant*float(d[bookID][3])
            print("Total Price: " ,"$",price)
            date1=dateTime_(time)
            aaa=int(d[bookID][2])-quant
            d[bookID][2]=aaa
            nameofborrower.append(name)
            saveFile=open("bills.txt","a")
            saveFile.write("\n")
            saveFile.write(name)
            saveFile.write(",")
            saveFile.write(d[bookID][0])
            saveFile.write(",")
            saveFile.write(str(quant))
            saveFile.write(",")
            saveFile.write(str(price))
            saveFile.write(",")
            saveFile.write(dateTime_(time))
            saveFile.write("\n")
            saveFile.close()
            morebooks()
            import bill
            s=bill.bills_()
            file2=open("bills.txt","w")
            file2.write("")
            FilE=open("books.txt","w")
            FilE.write("")
         
            for values in d.values():
                eFile=open("books.txt","a")
                eFile.write(str(values[0])+","+str(values[1])+","+str(values[2])+","+str(values[3]))
                eFile.write("\n")
            eFile.close()
            
            
        elif quant==0:
            print("Please input a valid option.")
            menu_()
        else:
            print("Sorry, we don't have", quant , "books.")
            menu_()
    else :
        print("Sorry, the book you asked for is unavailable.")
        menu_()
    return nameofborrower
    


def menu_():
    
    choice=0
    done=False
    while done==False:
                
        try:
            print("""\n
========LIBRARY MENU======
1.Request a book
2.Return a book

3.Exit
===========================""")
            choice= int(input("Enter a number : "))
            if choice==1:
                read_()
                nameofborrower=borrowbooks()
                
                
            elif choice==2:
                time=int(input("Enter the days you returned the books in  : "))
                do=True
                while do==True:
                    if time>=10 and time!=0:
                        timed=time-10
                        fine=timed*2
                        print("You have been fined $",fine,"for not returning the books in time.")
                        do=False
                     
                    elif time==0 or time<0:
                        print("Please enter a valid option")
                    
                    else:
                        print("You have returned the book in time. ")
                        do=False

                nameb=askname_()
                bookIDb=int(input("Enter the bookID:"))
                quant1=int(input("Enter the quantity of books : "))
                      
                for i in range(len(nameofborrower)):
                    if nameb==nameofborrower[i]:
                        print("You have borrowed a book.")
                        cc=quant1
                        print("The quantity of books that you borrowed : ",cc)
                        added= cc+int(d[bookIDb][2])
                        d[bookIDb][2]=str(added)
                        File3=open("books.txt","w")
                        File3.write("")
                        
                     
                        for values in d.values():
                            File4=open("books.txt","a")
                            File4.write(str(values[0])+","+str(values[1])+","+str(values[2])+","+str(values[3]))
                            File4.write("\n")
                        File4.close()
                        read_()
                         
                         
                    else:
                        print("You have not borrowed a book.")
                
            elif choice==3:
                print("Thank you ")                       
                done=True
            else:
                print("The option is invalid. Please chose a valid number")
                menu_()
            
        except :
            print("The option is invalid. Please choose a valid number")
          



menu_()
                    
       

                

    
    
