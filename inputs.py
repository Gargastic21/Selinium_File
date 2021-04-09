# Python program to count the 
# number of lines in a text file  
def file__len(filename):
    # Opening a file
    f = open(filename,"r")
    Counter = 0
    # Reading from file
    Content = f.read()
    CoList = Content.split("\n")
    for i in CoList:
        if i:
            Counter += 1
    return Counter

def convert(str):
    l1=list(str.split())
    return l1

def click(l):
    return ("{0}.click()".format(l[0]))

def send(l):
    return ("{0}.send({1})".format(l[0],l[2]))


file_name="req.txt"
len = file__len(file_name)
f=open(file_name,"r")
print(len)


for i in f:
    #print("{0}".format(i.strip()))
    str = i.strip()
    l=convert(str)
    if l[1] == "click":
        print(click(l))
        
    elif l[1] == "send":
        print(send(l))



# def file__read(filename):
#     # Opening a file
#     f = open(filename,"r")
#     # f = f.read()
#     f = f.read()
    
#     return f

# print(file__read("req.txt"))

    