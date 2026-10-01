
print("! This is shit calculator !")
print("---------------------------")
print("! This is shit calculator !")
print("1. Celcious to farenheigth")
print("2. fareheight to Celcious")

user = int(input("Enter 1/2 :  "))


def ctf(x):
    print("the temp is :",(x*9/5)+ 3)
    
def ftc(y):
    print("the tempreature is :",(y-32)*5/9)

if user == 1:
    c = int(input("Enter tempeture in celcious"))
    ctf(c)

if user == 2:
    f = int(input("Enter temp in farenheight"))
    ftc(f)






