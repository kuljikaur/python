# nested if 
cgpa = float(input("enter your cgpa : "))
if(cgpa>=7.5):
    print("congs you are eligible :  ")

    b = float(input("enter your pending backlog :"))
    if(b==0):
        print("well done go ahead : ")

        c = float(input("enter your 10th percentage : "))
        if(c >= 85):
            print("great")

            d= float(input("enter +2 percenatge :"))

            if(d>85):
                print("you are eligible for job : ")

else:
    print("try next time ")
    