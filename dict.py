def dic_(x):
    file1=open("books.txt","r")
    d={}
    b=1
    for line in file1:
        line=line.replace("\n","")
        line=line.replace("$","")
        d[b]=line.split(",")
        b=b+1
    return d
